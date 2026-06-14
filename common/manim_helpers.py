# -*- coding: utf-8 -*-
"""Reusable Manim helpers for educational Arabic/Darija projects."""

from __future__ import annotations

import os
from functools import lru_cache
from typing import Iterable

from manim import *
import manimpango

try:
    import arabic_reshaper
    from bidi.algorithm import get_display
except ImportError:  # Manim/Pango can still render Arabic on many systems.
    arabic_reshaper = None
    get_display = None


BG = "#0B0F19"
WHITE = "#F8FAFC"
MUTED = "#94A3B8"
PRESSURE = "#F97316"
CALM = "#38BDF8"
SUCCESS = "#22C55E"
YELLOW = "#FACC15"


@lru_cache(maxsize=1)
def _installed_fonts() -> set[str]:
    try:
        import manimpango

        return set(manimpango.list_fonts())
    except Exception:
        return set()
    

def load_fonts(path: str) -> None:
    """Load all fonts from the given path into Manim/Pango."""
    fonts = _installed_fonts()
    for file in os.listdir(path):
        if file.lower().endswith((".ttf", ".otf")):
            font_name = os.path.splitext(file)[0]
            if font_name not in fonts:
                manimpango.register_font(os.path.join(path, file))


def pick_font(candidates: Iterable[str], fallback: str = "Arial") -> str:
    """Return the first installed font from candidates, otherwise fallback."""

    load_fonts("assets/fonts")

    fonts = _installed_fonts()
    for font in candidates:
        if not fonts or font in fonts:
            return font
    return fallback


ARABIC_FONT = pick_font(
    ("Noto Kufi Arabic", "Noto Naskh Arabic", "Amiri", "Arial", "DejaVu Sans"),
)
LATIN_FONT = pick_font(("Montserrat", "Inter", "Poppins", "Arial", "DejaVu Sans"))


def ar(text: str) -> str:
    """Return Arabic text in the form Manim/Pango expects.

    Manim CE renders Text through Pango, which already handles Arabic joining
    and RTL layout when it receives logical Unicode text. A reshaper fallback is
    left as an opt-in for unusual render stacks that need pre-shaped text.
    """

    if os.environ.get("MANIM_USE_ARABIC_RESHAPER") == "1":
        if arabic_reshaper is not None and get_display is not None:
            return get_display(arabic_reshaper.reshape(text))
    return text


def fit_to_frame(
    mobject: Mobject,
    max_width: float | None = None,
    max_height: float | None = None,
) -> Mobject:
    """Scale a mobject down until it fits the requested bounds."""

    if max_width and mobject.width > max_width and mobject.width > 0:
        mobject.scale(max_width / mobject.width)
    if max_height and mobject.height > max_height and mobject.height > 0:
        mobject.scale(max_height / mobject.height)
    return mobject


def make_ar_text(
    content: str,
    font_size: float = 40,
    color: str = WHITE,
    weight: str = "NORMAL",
    max_width: float | None = None,
    max_height: float | None = None,
    **kwargs,
) -> Text:
    text = Text(
        ar(content),
        font=ARABIC_FONT,
        font_size=font_size,
        color=color,
        weight=weight,
        line_spacing=0.85,
        **kwargs,
    )
    return fit_to_frame(text, max_width=max_width, max_height=max_height)


def make_latin_text(
    content: str,
    font_size: float = 60,
    color: str = WHITE,
    weight: str = "NORMAL",
    max_width: float | None = None,
    max_height: float | None = None,
    **kwargs,
) -> Text:
    text = Text(
        content,
        font=LATIN_FONT,
        font_size=font_size,
        color=color,
        weight=weight,
        **kwargs,
    )
    return fit_to_frame(text, max_width=max_width, max_height=max_height)


def create_check_icon(color: str = SUCCESS, size: float = 0.22) -> VGroup:
    first = Line(
        LEFT * size * 0.9,
        LEFT * size * 0.2 + DOWN * size * 0.75,
        stroke_color=color,
        stroke_width=5,
    )
    second = Line(
        LEFT * size * 0.2 + DOWN * size * 0.75,
        RIGHT * size,
        stroke_color=color,
        stroke_width=5,
    )
    return VGroup(first, second)


def create_glow_circle(radius: float = 1.6, color: str = CALM) -> VGroup:
    rings = VGroup()
    for index, opacity in enumerate((0.26, 0.14, 0.07)):
        ring = Circle(radius=radius + index * 0.28)
        ring.set_stroke(color=color, width=max(1.0, 3.0 - index), opacity=opacity)
        rings.add(ring)
    return rings


def create_student_icon(
    color: str = WHITE,
    accent: str = CALM,
    scale_factor: float = 1.0,
    stroke_width: float = 5.0,
) -> VGroup:
    head = Circle(
        radius=0.28,
        stroke_color=color,
        stroke_width=stroke_width,
        fill_color=BG,
        fill_opacity=1,
    ).shift(UP * 0.52)
    torso = Line(
        UP * 0.22,
        DOWN * 0.72,
        stroke_color=color,
        stroke_width=stroke_width,
    )
    arms = Line(
        LEFT * 0.42 + DOWN * 0.12,
        RIGHT * 0.42 + DOWN * 0.12,
        stroke_color=color,
        stroke_width=stroke_width,
    )
    legs = VGroup(
        Line(DOWN * 0.72, DOWN * 1.15 + LEFT * 0.28, stroke_color=color, stroke_width=stroke_width),
        Line(DOWN * 0.72, DOWN * 1.15 + RIGHT * 0.28, stroke_color=color, stroke_width=stroke_width),
    )
    chest = Circle(radius=0.055, color=accent, fill_color=accent, fill_opacity=1)
    chest.move_to(DOWN * 0.18)
    student = VGroup(head, torso, arms, legs, chest)
    student.scale(scale_factor)
    return student


def create_paper(
    title: str = "Relevé de notes",
    width: float = 3.2,
    height: float = 4.1,
    color: str = WHITE,
    accent: str = CALM,
    fill: str = "#111827",
) -> VGroup:
    page = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.16,
        stroke_color=color,
        stroke_width=3,
        fill_color=fill,
        fill_opacity=0.92,
    )
    label = make_latin_text(title, font_size=25, color=color, weight="BOLD", max_width=width - 0.45)
    label.move_to(page.get_top() + DOWN * 0.42)
    header = Line(
        page.get_left() + RIGHT * 0.35 + UP * (height * 0.32),
        page.get_right() + LEFT * 0.35 + UP * (height * 0.32),
        stroke_color=accent,
        stroke_width=3,
    )
    lines = VGroup()
    for offset in (0.65, 0.25, -0.15, -0.55):
        line = Line(
            LEFT * (width * 0.33),
            RIGHT * (width * 0.33),
            stroke_color=MUTED,
            stroke_width=2,
        )
        line.move_to(page.get_center() + DOWN * offset)
        lines.add(line)
    return VGroup(page, label, header, lines)


def create_card(
    content: str,
    width: float = 5.8,
    height: float = 1.12,
    color: str = CALM,
    font_size: float = 31,
    fill_opacity: float = 0.12,
) -> VGroup:
    box = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.16,
        stroke_color=color,
        stroke_width=2.5,
        fill_color=color,
        fill_opacity=fill_opacity,
    )
    icon = create_check_icon(color=color, size=0.2)
    icon.move_to(box.get_right() + LEFT * 0.48)
    label = make_ar_text(content, font_size=font_size, color=WHITE, max_width=width - 1.25)
    label.next_to(icon, LEFT, buff=0.24)
    label.align_to(box, UP).shift(DOWN * (height * 0.28))
    return VGroup(box, icon, label)
