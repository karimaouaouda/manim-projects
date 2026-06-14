# -*- coding: utf-8 -*-
"""Reusable Arabic Tex helper for Manim scenes.

This helper uses LuaLaTeX with Babel Arabic support so Arabic text is shaped
and ordered by LaTeX instead of relying on Manim's default text renderer.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from manim import *


ROOT = Path(__file__).resolve().parents[1]
AMIRI_FONT_DIR = (ROOT / "assets" / "fonts" / "Amiri").as_posix()
CAIRO_FONT_DIR = (ROOT / "assets" / "fonts" / "Cairo").as_posix()
DEFAULT_ARABIC_FONT = "cairo"  # "amiri" is also supported


FONT_CONFIGS = {
    "amiri": {
        "family": "Amiri",
        "path": AMIRI_FONT_DIR,
        "upright": "*-Regular",
        "bold": "*-Bold",
        "italic": "*-Italic",
        "bold_italic": "*-BoldItalic",
    },
    "cairo": {
        "family": "Cairo",
        "path": CAIRO_FONT_DIR,
        "upright": "*-Regular",
        "bold": "*-Bold",
        "italic": "*-Regular",
        "bold_italic": "*-Bold",
    },
}


@lru_cache(maxsize=None)
def get_arabic_tex_template(font: str = DEFAULT_ARABIC_FONT) -> TexTemplate:
    """Return a cached LuaLaTeX template configured for the requested font."""

    font_key = font.lower()
    if font_key not in FONT_CONFIGS:
        available = ", ".join(sorted(FONT_CONFIGS))
        raise ValueError(f"Unknown Arabic font '{font}'. Choose one of: {available}.")

    font_config = FONT_CONFIGS[font_key]
    template = TexTemplate()
    template.tex_compiler = "lualatex"
    template.output_format = ".pdf"
    template.preamble = rf"""
\usepackage[bidi=basic,layout=sectioning.tabular,provide=*]{{babel}}
\babelprovide[import,main]{{arabic}}
\babelprovide[import]{{english}}
\babelfont{{rm}}[
    Path={{{font_config["path"]}/}},
    Extension=.ttf,
    UprightFont={font_config["upright"]},
    BoldFont={font_config["bold"]},
    ItalicFont={font_config["italic"]},
    BoldItalicFont={font_config["bold_italic"]}
]{{{font_config["family"]}}}
\usepackage{{amsmath}}
\usepackage{{amssymb}}
"""
    return template


ARABIC_TEX_TEMPLATE = get_arabic_tex_template(DEFAULT_ARABIC_FONT)


class ArabicTex(Tex):
    """Tex subclass that avoids Manim substring grouping for Babel Arabic.

    Manim wraps normal ``Tex`` strings in dvisvgm ``raw`` group markers so it can
    split a formula back into tex parts. Babel's Arabic output can drop those
    markers, producing noisy "Could not find SVG group" log messages despite a
    valid rendered SVG. Arabic labels in this project are treated as single text
    blocks, so skipping those markers is safer and quieter.
    """

    def _join_tex_strings_with_unique_deliminters(
        self,
        tex_strings: list[str],
        substrings_to_isolate,
    ) -> str:
        return self.arg_separator.join(tex_strings)

    def _break_up_by_substrings(self):
        return self


def _escape_latex_text(text: str) -> str:
    """Escape plain text for safe use inside LaTeX text commands."""

    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def _arabic_tex_body(text: str) -> str:
    """Wrap one or more plain Arabic lines for Babel/LuaLaTeX."""

    lines = [line.strip() for line in text.splitlines()]
    wrapped_lines = [rf"\foreignlanguage{{arabic}}{{{_escape_latex_text(line)}}}" for line in lines if line]
    return r"\\[0.18em]".join(wrapped_lines) if wrapped_lines else r"\foreignlanguage{arabic}{}"


def get_arabic_text(
    text: str,
    size: float = 40,
    color=WHITE,
    font: str = DEFAULT_ARABIC_FONT,
    **kwargs,
) -> ArabicTex:
    """Return an Arabic-aware Manim Tex object.

    Args:
        text: Arabic or mixed Arabic text content.
        size: Manim font size.
        color: Manim color for the rendered text.
        font: Arabic font key. Supported values are ``"amiri"`` and ``"cairo"``.
        **kwargs: Extra keyword arguments passed directly to ``Tex``.
    """

    return ArabicTex(
        _arabic_tex_body(text),
        tex_template=get_arabic_tex_template(font),
        font_size=size,
        color=color,
        **kwargs,
    )


# Example usage in a Manim scene:
#
# from manim import *
# from common.arabic_text_helper import get_arabic_text
#
#
# class ArabicExample(Scene):
#     def construct(self):
#         title = get_arabic_text("السلام عليكم", size=56, color=WHITE, font="cairo")
#         self.play(Write(title))
#         self.wait()
