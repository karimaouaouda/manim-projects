# -*- coding: utf-8 -*-
"""Cinematic bilingual Manim journey teaser.

Render from the project root:
    manim -pqh projects/manim_journey_teaser.py ManimJourneyTeaser

Root wrapper, if using main.py:
    manim -pqh main.py ManimJourneyTeaser

Music:
    Manim renders the visual story only. Add license-safe motivational
    background music during editing, or mux it afterward with ffmpeg.
"""

from __future__ import annotations

import math
import os
import random
import sys
from pathlib import Path
from typing import Sequence

import numpy as np
from manim import *


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common import (
    BLACK,
    CYAN,
    GOLD,
    GREEN,
    MUTED,
    NAVY,
    SOFT_WHITE,
    SURFACE,
    WHITE,
    cinematic_background,
    create_glow_circle,
    fit_to_frame,
    make_ar_text,
    make_latin_text,
    pick_font,
    safe_ar_text,
)


config.pixel_width = 1080
config.pixel_height = 1350
config.frame_width = 8
config.frame_height = 10
config.frame_rate = 30


BACKGROUND = NAVY
DEEP = BLACK
BLUE = "#60A5FA"
RED_SOFT = "#FB7185"

SAFE_WIDTH = 7.1
SAFE_HEIGHT = 8.9


class ManimJourneyTeaser(MovingCameraScene):
    """A brandless cinematic short about code-based visual explanation."""

    def construct(self) -> None:
        self.rng = random.Random(32)
        self.setup_style()
        self.scene_1_hook()
        self.scene_2_code_to_motion()
        self.scene_3_static_vs_animated()
        self.scene_4_learning_potential()
        self.scene_5_experiment_process()
        self.scene_6_closing_question()

    def setup_style(self) -> None:
        self.camera.background_color = BACKGROUND
        self.use_tex_arabic = os.environ.get("MANIM_JOURNEY_USE_TEX_ARABIC") == "1"
        self.mono_font = self.pick_font(("Cascadia Code", "Consolas", "JetBrains Mono", "Courier New", "DejaVu Sans Mono"))
        self.background = cinematic_background(seed=12)
        self.add(self.background)

    def pick_font(self, candidates: Sequence[str]) -> str:
        return pick_font(candidates, fallback="DejaVu Sans Mono")

    def reset_camera(self) -> None:
        self.camera.frame.move_to(ORIGIN)
        self.camera.frame.set(width=config.frame_width)

    def clear_scene(self, run_time: float = 0.58, shift: np.ndarray = DOWN * 0.12) -> None:
        self.reset_camera()
        removable = [mobject for mobject in self.mobjects if mobject is not self.background]
        if removable:
            self.play(FadeOut(Group(*removable), shift=shift), run_time=run_time, rate_func=smooth)

    def latin_text(
        self,
        content: str,
        size: float = 42,
        color: str = WHITE,
        weight: str = "NORMAL",
        max_width: float | None = None,
        max_height: float | None = None,
        font: str | None = None,
    ) -> Mobject:
        if font is None:
            return make_latin_text(
                content,
                font_size=size,
                color=color,
                weight=weight,
                max_width=max_width,
                max_height=max_height,
            )

        text = Text(
            content,
            font=font,
            font_size=size,
            color=color,
            weight=weight,
        )
        return fit_to_frame(text, max_width=max_width, max_height=max_height)

    def arabic_text(
        self,
        content: str,
        size: float = 34,
        color: str = WHITE,
        weight: str = "NORMAL",
        max_width: float | None = None,
        max_height: float | None = None,
    ) -> Mobject:
        if self.use_tex_arabic:
            try:
                return safe_ar_text(
                    content,
                    font_size=size,
                    color=color,
                    weight=weight,
                    max_width=max_width or SAFE_WIDTH,
                    max_height=max_height,
                )
            except Exception:
                self.use_tex_arabic = True

        return make_ar_text(
            content,
            font_size=size,
            color=color,
            weight=weight,
            max_width=max_width,
            max_height=max_height,
        )

    def bilingual_text(
        self,
        english: str,
        arabic: str,
        en_size: float = 42,
        ar_size: float = 32,
        color: str = WHITE,
        en_weight: str = "BOLD",
        ar_weight: str = "NORMAL",
        gap: float = 0.20,
        max_width: float = SAFE_WIDTH,
    ) -> VGroup:
        en = self.latin_text(english, size=en_size, color=color, weight=en_weight, max_width=max_width)
        ar_line = self.arabic_text(arabic, size=ar_size, color=color, weight=ar_weight, max_width=max_width)
        group = VGroup(en, ar_line).arrange(DOWN, buff=gap)
        return fit_to_frame(group, max_width=max_width)

    def emphasized_build_text(self) -> VGroup:
        en_left = self.latin_text("I wanted to", size=42, color=WHITE, weight="BOLD")
        en_build = self.latin_text("build", size=42, color=CYAN, weight="BOLD")
        en_right = self.latin_text("explanations.", size=42, color=WHITE, weight="BOLD")
        english = VGroup(en_left, en_build, en_right).arrange(RIGHT, buff=0.13)
        fit_to_frame(english, max_width=SAFE_WIDTH)

        ar_left = self.arabic_text("شروحات تتحرك.", size=32, color=WHITE)
        ar_build = self.arabic_text("بناء", size=32, color=CYAN, weight="BOLD")
        ar_right = self.arabic_text("أردت", size=32, color=WHITE)
        arabic = VGroup(ar_left, ar_build, ar_right).arrange(RIGHT, buff=0.12)
        fit_to_frame(arabic, max_width=SAFE_WIDTH)

        group = VGroup(english, arabic).arrange(DOWN, buff=0.20)
        group.build_targets = VGroup(en_build, ar_build)
        return group

    def create_glow_dot(
        self,
        point: Sequence[float],
        color: str = CYAN,
        radius: float = 0.055,
        glow_scale: float = 3.3,
    ) -> VGroup:
        point_array = np.array(point, dtype=float)
        halo = create_glow_circle(radius=radius * glow_scale, color=color)
        halo.move_to(point_array)
        halo.scale(0.34)
        halo.set_opacity(0.48)
        dot = Dot(point_array, radius=radius, color=color)
        return VGroup(halo, dot)

    def make_idea_network(self, center: np.ndarray = ORIGIN, scale: float = 1.0) -> tuple[VGroup, VGroup, VGroup]:
        center_dot = self.create_glow_dot(center, CYAN, radius=0.060 * scale)
        offsets = [
            LEFT * 1.28 + UP * 0.35,
            RIGHT * 1.22 + UP * 0.52,
            LEFT * 0.54 + DOWN * 0.90,
            RIGHT * 0.88 + DOWN * 0.82,
            UP * 1.22,
        ]
        nodes = VGroup(center_dot)
        lines = VGroup()
        for index, offset in enumerate(offsets):
            color = GOLD if index == 4 else CYAN if index % 2 == 0 else BLUE
            node = self.create_glow_dot(center + offset * scale, color, radius=0.038 * scale)
            line = Line(center, node[-1].get_center())
            line.set_stroke(color=color, width=1.6, opacity=0.48)
            nodes.add(node)
            lines.add(line)

        cross_lines = VGroup()
        for first, second in ((1, 2), (2, 4), (3, 5)):
            line = Line(nodes[first][-1].get_center(), nodes[second][-1].get_center())
            line.set_stroke(MUTED, width=1.0, opacity=0.22)
            cross_lines.add(line)

        return nodes, lines, cross_lines

    def make_panel(
        self,
        width: float,
        height: float,
        title: str,
        accent: str = CYAN,
        fill: str = SURFACE,
    ) -> VGroup:
        shell = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.15,
            stroke_color=accent,
            stroke_width=1.7,
            stroke_opacity=0.52,
            fill_color=fill,
            fill_opacity=0.88,
        )
        top = Line(shell.get_left() + UP * (height / 2 - 0.48), shell.get_right() + UP * (height / 2 - 0.48))
        top.set_stroke(accent, width=1.4, opacity=0.50)
        title_text = self.latin_text(title, size=15, color=MUTED, weight="BOLD", max_width=width - 0.8)
        title_text.move_to(shell.get_top() + DOWN * 0.25)

        lights = VGroup()
        for index, color in enumerate((RED_SOFT, GOLD, GREEN)):
            dot = Dot(radius=0.035, color=color)
            dot.move_to(shell.get_top() + DOWN * 0.25 + LEFT * (width / 2 - 0.30 - index * 0.16))
            lights.add(dot)

        return VGroup(shell, top, title_text, lights)

    def create_code_panel(self, lines: Sequence[str]) -> tuple[VGroup, VGroup]:
        panel = self.make_panel(3.50, 4.55, "Python + Manim", accent=CYAN, fill=SURFACE)
        code_lines = VGroup()
        start = panel[0].get_top() + DOWN * 0.86 + LEFT * 1.47
        colors = (BLUE, GOLD, CYAN, GREEN, RED_SOFT)
        for index, line in enumerate(lines):
            label = self.latin_text(
                line,
                size=15,
                color=colors[index % len(colors)] if index in (0, 1, 3, 4) else SOFT_WHITE,
                weight="NORMAL",
                max_width=3.04,
                font=self.mono_font,
            )
            label.move_to(start + DOWN * 0.48 * index, aligned_edge=LEFT)
            code_lines.add(label)

        return VGroup(panel, code_lines), code_lines

    def make_label_pill(self, english: str, arabic: str | None = None, color: str = CYAN) -> VGroup:
        if arabic:
            label = self.bilingual_text(english, arabic, en_size=17, ar_size=15, color=WHITE, max_width=1.65, gap=0.06)
        else:
            label = self.latin_text(english, size=17, color=WHITE, weight="BOLD", max_width=1.8)
        pill = RoundedRectangle(
            width=max(1.35, label.width + 0.36),
            height=max(0.42, label.height + 0.17),
            corner_radius=0.11,
            stroke_color=color,
            stroke_width=1.4,
            fill_color=color,
            fill_opacity=0.10,
        )
        label.move_to(pill)
        return VGroup(pill, label)

    def make_logic_node(
        self,
        english: str,
        arabic: str,
        color: str = CYAN,
        width: float = 1.22,
        height: float = 0.74,
        en_size: float = 17,
        ar_size: float = 14,
        fill_opacity: float = 0.10,
    ) -> VGroup:
        label = self.bilingual_text(
            english,
            arabic,
            en_size=en_size,
            ar_size=ar_size,
            color=WHITE,
            en_weight="BOLD",
            max_width=width - 0.18,
            gap=0.04,
        )
        box = RoundedRectangle(
            width=max(width, label.width + 0.32),
            height=max(height, label.height + 0.22),
            corner_radius=0.12,
            stroke_color=color,
            stroke_width=1.55,
            fill_color=color,
            fill_opacity=fill_opacity,
        )
        label.move_to(box)
        return VGroup(box, label)

    def create_process_diagram(
        self,
        labels: Sequence[tuple[str, str]],
        color: str = CYAN,
        muted: bool = False,
        scale_factor: float = 1.0,
    ) -> tuple[VGroup, VGroup, VGroup]:
        nodes = VGroup()
        for index, (english, arabic_label) in enumerate(labels):
            node_color = GOLD if index == len(labels) - 1 else color
            node = self.make_logic_node(
                english,
                arabic_label,
                color=node_color,
                width=0.98 * scale_factor,
                height=0.62 * scale_factor,
                en_size=14 * scale_factor,
                ar_size=12 * scale_factor,
                fill_opacity=0.075 if muted else 0.12,
            )
            nodes.add(node)
        nodes.arrange(RIGHT, buff=0.23 * scale_factor)

        arrows = VGroup()
        for left, right in zip(nodes, nodes[1:]):
            arrow = Arrow(
                left.get_right() + RIGHT * 0.03,
                right.get_left() + LEFT * 0.03,
                buff=0,
                stroke_width=2.0 * scale_factor,
                color=MUTED if muted else CYAN,
                max_tip_length_to_length_ratio=0.20,
            )
            arrow.set_opacity(0.45 if muted else 0.78)
            arrows.add(arrow)

        diagram = VGroup(nodes, arrows)
        if muted:
            diagram.set_opacity(0.48)
        return diagram, nodes, arrows

    def create_icon(self, kind: str, color: str = CYAN) -> VGroup:
        shell = Circle(
            radius=0.43,
            stroke_color=color,
            stroke_width=1.8,
            fill_color=color,
            fill_opacity=0.075,
        )
        glow = Circle(radius=0.58, stroke_opacity=0, fill_color=color, fill_opacity=0.035)
        icon = VGroup()

        if kind == "programming":
            icon.add(self.latin_text("</>", size=23, color=WHITE, weight="BOLD", font=self.mono_font))
        elif kind == "math":
            sigma = self.latin_text("Σ", size=29, color=WHITE, weight="BOLD")
            curve = VMobject()
            curve.set_points_smoothly([LEFT * 0.26 + DOWN * 0.20, LEFT * 0.07, RIGHT * 0.13 + UP * 0.18, RIGHT * 0.30 + DOWN * 0.05])
            curve.set_stroke(GOLD, width=2.0, opacity=0.72)
            icon.add(sigma, curve)
        elif kind == "ai":
            points = [LEFT * 0.22 + UP * 0.16, LEFT * 0.22 + DOWN * 0.16, RIGHT * 0.22 + UP * 0.18, RIGHT * 0.22 + DOWN * 0.18]
            dots = VGroup(*[Dot(point, radius=0.035, color=WHITE) for point in points])
            links = VGroup()
            for a in points[:2]:
                for b in points[2:]:
                    links.add(Line(a, b, stroke_color=color, stroke_width=1.1, stroke_opacity=0.58))
            icon.add(links, dots)
        elif kind == "physics":
            nucleus = Dot(radius=0.043, color=GOLD)
            orbits = VGroup()
            for angle in (0, 60, -60):
                orbit = Ellipse(width=0.72, height=0.25, stroke_color=WHITE, stroke_width=1.4, stroke_opacity=0.72)
                orbit.rotate(angle * DEGREES)
                orbits.add(orbit)
            icon.add(orbits, nucleus)
        else:
            dots = VGroup()
            positions = (LEFT * 0.24 + UP * 0.16, RIGHT * 0.21 + UP * 0.18, LEFT * 0.05 + DOWN * 0.21)
            for point in positions:
                dots.add(Dot(point, radius=0.04, color=WHITE))
            links = VGroup(
                Line(positions[0], positions[1], stroke_color=color, stroke_width=1.4, stroke_opacity=0.62),
                Line(positions[1], positions[2], stroke_color=color, stroke_width=1.4, stroke_opacity=0.62),
                Line(positions[2], positions[0], stroke_color=color, stroke_width=1.4, stroke_opacity=0.62),
            )
            icon.add(links, dots)

        icon.move_to(shell)
        return VGroup(glow, shell, icon)

    def scene_1_hook(self) -> None:
        self.clear_scene(run_time=0.05)
        nodes, lines, cross_lines = self.make_idea_network(center=DOWN * 0.34, scale=1.02)
        first_text = self.bilingual_text(
            "I didn't want to make normal videos.",
            "لم أرد صنع فيديوهات عادية.",
            en_size=35,
            ar_size=29,
            max_width=6.8,
        )
        first_text.move_to(UP * 2.35)

        second_text = self.emphasized_build_text()
        second_text.move_to(first_text)

        self.play(FadeIn(nodes[0], scale=0.58), run_time=0.55, rate_func=smooth)
        self.play(
            LaggedStart(*[Create(line) for line in lines], lag_ratio=0.13),
            LaggedStart(*[FadeIn(node, scale=0.60) for node in nodes[1:]], lag_ratio=0.13),
            run_time=1.05,
            rate_func=smooth,
        )
        self.play(Create(cross_lines), FadeIn(first_text, shift=UP * 0.12), run_time=0.80, rate_func=smooth)
        self.wait(1.25)
        self.play(ReplacementTransform(first_text, second_text), run_time=0.75, rate_func=smooth)
        self.play(
            LaggedStart(
                *[Circumscribe(target, color=CYAN, buff=0.08) for target in second_text.build_targets],
                lag_ratio=0.18,
            ),
            run_time=0.90,
        )
        self.wait(0.55)

        self.scene_1_line = Line(LEFT * 3.46 + UP * 2.05, LEFT * 0.06 + UP * 2.05)
        self.scene_1_line.set_stroke(CYAN, width=2.0, opacity=0.70)
        network = VGroup(nodes, lines, cross_lines)
        self.play(
            FadeOut(second_text, shift=UP * 0.08),
            ReplacementTransform(network, self.scene_1_line),
            run_time=0.82,
            rate_func=smooth,
        )

    def scene_2_code_to_motion(self) -> None:
        title = self.bilingual_text(
            "What if ideas could move?",
            "ماذا لو استطاعت الأفكار أن تتحرك؟",
            en_size=34,
            ar_size=27,
            max_width=6.7,
        )
        title.move_to(UP * 4.10)

        code_lines_raw = [
            "idea = Circle()",
            'question = Text("Why?")',
            "self.play(Create(idea))",
            "self.play(idea.animate.shift(RIGHT))",
            "self.play(Transform(idea, explanation))",
        ]
        code_panel, code_lines = self.create_code_panel(code_lines_raw)
        code_panel.move_to(LEFT * 2.05 + DOWN * 0.10)

        preview_panel = self.make_panel(3.42, 4.55, "Visual Explanation", accent=GOLD, fill=SURFACE)
        preview_panel.move_to(RIGHT * 2.08 + DOWN * 0.10)

        left_label = self.make_label_pill("Python + Manim", color=CYAN)
        left_label.next_to(code_panel[0][0], UP, buff=0.20)
        right_label = self.make_label_pill("Visual Explanation", "شرح بصري", color=GOLD)
        right_label.next_to(preview_panel[0], UP, buff=0.20)

        code_shell = VGroup(code_panel[0][0], code_panel[0][2], code_panel[0][3])
        code_top = code_panel[0][1]

        self.play(FadeIn(title, shift=UP * 0.12), run_time=0.58, rate_func=smooth)
        self.play(
            Transform(self.scene_1_line, code_top),
            FadeIn(code_shell, shift=RIGHT * 0.16),
            FadeIn(left_label, shift=UP * 0.08),
            FadeIn(preview_panel, shift=LEFT * 0.18),
            FadeIn(right_label, shift=UP * 0.08),
            run_time=0.88,
            rate_func=smooth,
        )

        preview_center = preview_panel[0].get_center() + DOWN * 0.16
        idea_circle = Circle(radius=0.42, stroke_color=CYAN, stroke_width=2.4, fill_color=CYAN, fill_opacity=0.08)
        idea_circle.move_to(preview_center + LEFT * 0.50 + DOWN * 0.05)
        question = self.latin_text("Why?", size=26, color=GOLD, weight="BOLD", max_width=1.0)
        question.move_to(preview_center + RIGHT * 0.65 + UP * 0.58)
        motion_arrow = Arrow(
            idea_circle.get_right() + RIGHT * 0.15,
            idea_circle.get_right() + RIGHT * 0.78,
            buff=0,
            stroke_width=2.4,
            color=CYAN,
            max_tip_length_to_length_ratio=0.22,
        )

        diagram, diagram_nodes, diagram_arrows = self.create_process_diagram(
            (("Idea", "فكرة"), ("Why", "لماذا؟"), ("Motion", "حركة")),
            color=CYAN,
            scale_factor=0.92,
        )
        diagram.move_to(preview_center + DOWN * 0.08)
        diagram.scale(0.95)

        connector_guides = VGroup()
        for index, code_line in enumerate(code_lines):
            highlight = SurroundingRectangle(code_line, color=GOLD if index == 4 else CYAN, buff=0.045)
            highlight.set_stroke(width=1.2, opacity=0.42)
            self.play(Write(code_line), FadeIn(highlight), run_time=0.34, rate_func=smooth)

            if index == 0:
                connector = Line(code_line.get_right() + RIGHT * 0.08, idea_circle.get_left() + LEFT * 0.15)
                connector.set_stroke(CYAN, width=1.2, opacity=0.36)
                self.play(Create(connector), Create(idea_circle), run_time=0.50, rate_func=smooth)
                connector_guides.add(connector)
            elif index == 1:
                connector = Line(code_line.get_right() + RIGHT * 0.08, question.get_left() + LEFT * 0.12)
                connector.set_stroke(GOLD, width=1.2, opacity=0.36)
                self.play(Create(connector), FadeIn(question, scale=0.84), run_time=0.45, rate_func=smooth)
                connector_guides.add(connector)
            elif index == 2:
                self.play(Indicate(idea_circle, color=CYAN, scale_factor=1.08), run_time=0.38)
            elif index == 3:
                self.play(GrowArrow(motion_arrow), idea_circle.animate.shift(RIGHT * 0.55), run_time=0.56, rate_func=smooth)
            else:
                self.play(
                    ReplacementTransform(VGroup(idea_circle, question, motion_arrow), diagram),
                    FadeOut(connector_guides),
                    run_time=0.72,
                    rate_func=smooth,
                )

            self.play(FadeOut(highlight), run_time=0.10)

        self.wait(0.65)

        full_preview_frame = RoundedRectangle(
            width=6.95,
            height=5.25,
            corner_radius=0.20,
            stroke_color=GOLD,
            stroke_width=1.5,
            stroke_opacity=0.34,
            fill_color=SURFACE,
            fill_opacity=0.18,
        )
        full_preview_frame.move_to(DOWN * 0.05)

        code_side = VGroup(code_panel, left_label, self.scene_1_line)
        self.play(
            FadeOut(code_side, shift=LEFT * 0.26),
            FadeOut(right_label, shift=UP * 0.06),
            Transform(preview_panel[0], full_preview_frame),
            FadeOut(preview_panel[1:]),
            diagram.animate.scale(1.18).move_to(DOWN * 0.08),
            title.animate.to_edge(UP, buff=0.70).scale(0.86).set_opacity(0.78),
            run_time=1.05,
            rate_func=smooth,
        )
        self.scene_2_title = title
        self.scene_2_preview_frame = preview_panel[0]
        self.scene_2_diagram = diagram
        self.wait(0.45)

    def scene_3_static_vs_animated(self) -> None:
        intro_text = self.bilingual_text(
            "Some concepts are hard to understand...",
            "بعض الأفكار يصعب فهمها...",
            en_size=29,
            ar_size=23,
            max_width=6.8,
        )
        intro_text.move_to(UP * 4.20)

        next_text = self.bilingual_text(
            "until you see the process.",
            "إلى أن ترى العملية أمامك.",
            en_size=31,
            ar_size=24,
            max_width=6.8,
        )
        next_text.move_to(intro_text)

        labels = (("Idea", "فكرة"), ("Step 1", "خطوة ١"), ("Step 2", "خطوة ٢"), ("Result", "نتيجة"))
        left_diagram, _, _ = self.create_process_diagram(labels, color=MUTED, muted=True, scale_factor=0.80)
        right_diagram, right_nodes, right_arrows = self.create_process_diagram(labels, color=CYAN, muted=False, scale_factor=0.80)
        left_diagram.move_to(LEFT * 2.05 + DOWN * 0.52)
        right_diagram.move_to(RIGHT * 2.05 + DOWN * 0.52)

        left_title = self.bilingual_text("Static", "ثابت", en_size=23, ar_size=20, color=MUTED, max_width=1.7)
        right_title = self.bilingual_text("Animated", "متحرك", en_size=23, ar_size=20, color=WHITE, max_width=1.9)
        left_title.move_to(LEFT * 2.05 + UP * 1.65)
        right_title.move_to(RIGHT * 2.05 + UP * 1.65)
        divider = Line(UP * 2.45, DOWN * 2.92, stroke_color=MUTED, stroke_width=1.1, stroke_opacity=0.36)

        self.play(
            FadeOut(self.scene_2_title, shift=UP * 0.08),
            FadeOut(self.scene_2_preview_frame, scale=1.02),
            ReplacementTransform(self.scene_2_diagram, left_diagram),
            FadeIn(intro_text, shift=UP * 0.10),
            run_time=0.95,
            rate_func=smooth,
        )
        self.play(FadeIn(left_title, shift=UP * 0.08), Create(divider), run_time=0.50)
        self.wait(0.65)
        self.play(FadeIn(right_title, shift=UP * 0.08), run_time=0.34)

        self.play(FadeIn(right_nodes[0], scale=0.82), run_time=0.42, rate_func=smooth)
        for arrow, node in zip(right_arrows, right_nodes[1:]):
            pulse = Dot(arrow.get_start(), radius=0.032, color=GOLD)
            self.play(GrowArrow(arrow), FadeIn(pulse), MoveAlongPath(pulse, arrow), run_time=0.46, rate_func=smooth)
            self.play(FadeOut(pulse), FadeIn(node, scale=0.82), run_time=0.28, rate_func=smooth)

        self.play(ReplacementTransform(intro_text, next_text), run_time=0.62, rate_func=smooth)
        result_glow = Circle(radius=0.52, stroke_opacity=0, fill_color=GOLD, fill_opacity=0.12)
        result_glow.move_to(right_nodes[-1])
        result_glow.set_z_index(-1)
        self.play(FadeIn(result_glow, scale=0.55), Circumscribe(right_nodes[-1], color=GOLD, buff=0.08), run_time=0.75)
        self.wait(0.95)

        self.scene_3_group = VGroup(left_diagram, left_title, divider, right_title, next_text, result_glow)
        self.scene_3_right_diagram = VGroup(right_nodes, right_arrows)

    def scene_4_learning_potential(self) -> None:
        statement = self.bilingual_text(
            "This could help people learn what static slides can't show.",
            "قد يساعد الناس على فهم ما لا توضحه الشرائح الثابتة.",
            en_size=26,
            ar_size=21,
            max_width=6.9,
        )
        statement.move_to(UP * 4.12)

        center = self.bilingual_text("Learning", "التعلّم", en_size=31, ar_size=25, max_width=2.6, color=WHITE)
        center.move_to(ORIGIN + DOWN * 0.15)
        center_glow = create_glow_circle(radius=0.94, color=CYAN)
        center_glow.move_to(center)
        center_glow.set_opacity(0.42)

        icon_specs = [
            ("programming", "Programming", "البرمجة", CYAN, 90),
            ("math", "Math", "الرياضيات", GOLD, 18),
            ("ai", "AI", "الذكاء الاصطناعي", BLUE, -54),
            ("physics", "Physics", "الفيزياء", GREEN, -126),
            ("systems", "Systems", "الأنظمة", CYAN, 162),
        ]
        icons = VGroup()
        for kind, english, arabic_label, color, angle in icon_specs:
            icon = self.create_icon(kind, color=color)
            label = self.bilingual_text(english, arabic_label, en_size=14, ar_size=12, max_width=1.38, gap=0.02)
            label.next_to(icon, DOWN, buff=0.11)
            item = VGroup(icon, label)
            radians = angle * DEGREES
            item.move_to(np.array([math.cos(radians) * 2.28, math.sin(radians) * 1.88 - 0.12, 0]))
            icons.add(item)

        fields = self.bilingual_text(
            "Programming • Math • AI • Physics • Systems",
            "البرمجة • الرياضيات • الذكاء الاصطناعي • الفيزياء • الأنظمة",
            en_size=16,
            ar_size=14,
            color=MUTED,
            en_weight="BOLD",
            max_width=6.9,
            gap=0.05,
        )
        fields.move_to(DOWN * 4.05)

        icon_seeds = VGroup()
        for item in icons:
            seed = self.create_glow_dot(item.get_center(), color=CYAN, radius=0.028, glow_scale=4.0)
            icon_seeds.add(seed)

        self.play(
            FadeOut(self.scene_3_group, shift=DOWN * 0.10),
            ReplacementTransform(self.scene_3_right_diagram, icon_seeds),
            FadeIn(statement, shift=UP * 0.10),
            FadeIn(center_glow, scale=0.72),
            FadeIn(center, scale=0.86),
            run_time=1.05,
            rate_func=smooth,
        )
        for seed, icon in zip(icon_seeds, icons):
            self.play(ReplacementTransform(seed, icon), run_time=0.20, rate_func=smooth)
        self.play(Rotate(icons, angle=10 * DEGREES, about_point=center.get_center()), run_time=1.6, rate_func=smooth)
        self.play(LaggedStart(*[Indicate(icon[0][1], color=GOLD, scale_factor=1.04) for icon in icons], lag_ratio=0.08), run_time=1.15)
        self.play(FadeIn(fields, shift=UP * 0.10), run_time=0.55)
        self.wait(1.15)

        self.learning_statement = statement
        self.learning_center = VGroup(center_glow, center)
        self.learning_icons = icons
        self.learning_fields = fields

    def scene_5_experiment_process(self) -> None:
        first = self.bilingual_text(
            "The hard part is not writing code.",
            "الصعب ليس كتابة الكود فقط.",
            en_size=28,
            ar_size=23,
            max_width=6.8,
        )
        first.move_to(UP * 4.15)
        second = self.bilingual_text(
            "The hard part is translating thought into motion.",
            "الصعب هو تحويل الفكرة إلى حركة.",
            en_size=26,
            ar_size=22,
            max_width=6.95,
        )
        second.move_to(first)

        timeline_specs = [
            ("Idea", "فكرة", GOLD),
            ("Scene", "مشهد", CYAN),
            ("Code", "كود", BLUE),
            ("Motion", "حركة", GREEN),
            ("Understanding", "فهم", GOLD),
        ]
        cards = VGroup()
        for english, arabic_label, color in timeline_specs:
            card = self.make_logic_node(
                english,
                arabic_label,
                color=color,
                width=2.55,
                height=0.72,
                en_size=19,
                ar_size=16,
                fill_opacity=0.10,
            )
            cards.add(card)
        cards.arrange(DOWN, buff=0.36)
        cards.move_to(DOWN * 0.40)

        arrows = VGroup()
        for index, (top, bottom) in enumerate(zip(cards, cards[1:])):
            color = GOLD if index == 2 else CYAN
            arrow = Arrow(
                top.get_bottom() + DOWN * 0.02,
                bottom.get_top() + UP * 0.02,
                buff=0,
                stroke_width=2.2 if index == 2 else 1.7,
                color=color,
                max_tip_length_to_length_ratio=0.18,
            )
            arrow.set_opacity(0.88 if index == 2 else 0.55)
            arrows.add(arrow)

        drifting_particles = VGroup()
        for _ in range(24):
            dot = Dot(
                [
                    self.rng.uniform(-3.5, 3.5),
                    self.rng.uniform(-4.2, 3.5),
                    0,
                ],
                radius=self.rng.uniform(0.006, 0.014),
                color=CYAN if self.rng.random() > 0.35 else GOLD,
            )
            dot.set_opacity(self.rng.uniform(0.10, 0.24))
            drifting_particles.add(dot)
        drifting_particles.set_z_index(-20)

        timeline_seeds = VGroup()
        for card in cards:
            timeline_seeds.add(self.create_glow_dot(card.get_center(), color=CYAN, radius=0.026, glow_scale=3.7))

        self.play(
            FadeOut(self.learning_statement, shift=UP * 0.08),
            FadeOut(self.learning_center, scale=0.98),
            FadeOut(self.learning_fields, shift=DOWN * 0.08),
            ReplacementTransform(self.learning_icons, timeline_seeds),
            FadeIn(first, shift=UP * 0.10),
            FadeIn(drifting_particles),
            run_time=1.00,
            rate_func=smooth,
        )

        visible_cards = VGroup()
        for index, (seed, card) in enumerate(zip(timeline_seeds, cards)):
            self.play(ReplacementTransform(seed, card), run_time=0.34, rate_func=smooth)
            visible_cards.add(card)
            if index < len(arrows):
                if index == 2:
                    glow = arrows[index].copy().set_stroke(GOLD, width=5.0, opacity=0.18)
                    self.play(GrowArrow(arrows[index]), FadeIn(glow), run_time=0.35, rate_func=smooth)
                    arrows.add(glow)
                else:
                    self.play(GrowArrow(arrows[index]), run_time=0.26, rate_func=smooth)

        self.play(ReplacementTransform(first, second), run_time=0.62, rate_func=smooth)
        self.play(
            drifting_particles.animate.shift(UP * 0.35 + RIGHT * 0.12).set_opacity(0.18),
            cards[-1].animate.scale(1.09).set_z_index(8),
            Circumscribe(cards[-1], color=GOLD, buff=0.10),
            run_time=1.20,
            rate_func=smooth,
        )
        self.wait(0.90)

        self.workflow_text = second
        self.workflow_cards = cards
        self.workflow_arrows = arrows
        self.workflow_particles = drifting_particles

    def scene_6_closing_question(self) -> None:
        final_card = self.workflow_cards[-1]
        other_cards = VGroup(*self.workflow_cards[:-1])

        closing_1 = self.bilingual_text(
            "Still experimenting.",
            "ما زلت أجرّب.",
            en_size=35,
            ar_size=28,
            max_width=6.3,
        )
        closing_1.move_to(UP * 1.20)

        closing_2 = self.bilingual_text(
            "But I think visual coding has a future in education.",
            "لكنني أؤمن أن للكود البصري مستقبلًا في التعليم.",
            en_size=24,
            ar_size=20,
            color=SOFT_WHITE,
            en_weight="BOLD",
            max_width=6.9,
        )
        closing_2.move_to(DOWN * 0.20)

        question = self.bilingual_text(
            "Where do you think this can help most?",
            "أين تعتقد أن هذا الأسلوب يمكن أن يساعد أكثر؟",
            en_size=27,
            ar_size=22,
            color=WHITE,
            max_width=6.9,
        )
        question.move_to(DOWN * 2.00)

        glow = VGroup()
        for radius, opacity in ((1.25, 0.16), (1.78, 0.09), (2.36, 0.045)):
            ring = Circle(radius=radius, stroke_color=CYAN, stroke_width=1.5, stroke_opacity=opacity)
            ring.move_to(UP * 0.36)
            glow.add(ring)

        outward_particles = VGroup()
        for index in range(34):
            angle = TAU * index / 34
            dot = Dot(np.array([math.cos(angle) * 0.75, math.sin(angle) * 0.48 + 0.30, 0]), radius=0.010, color=GOLD if index % 5 == 0 else CYAN)
            dot.set_opacity(0.34 if index % 5 == 0 else 0.20)
            outward_particles.add(dot)

        fade_items = VGroup(self.workflow_text, other_cards, self.workflow_arrows, self.workflow_particles)
        self.play(
            FadeOut(fade_items, shift=DOWN * 0.10),
            final_card.animate.move_to(UP * 0.30).scale(1.12),
            run_time=0.78,
            rate_func=smooth,
        )
        self.play(FadeIn(glow, scale=0.72), ReplacementTransform(final_card, closing_1), run_time=0.82, rate_func=smooth)
        self.play(FadeIn(outward_particles, scale=0.68), run_time=0.34)
        self.play(Rotate(glow, angle=8 * DEGREES), outward_particles.animate.scale(1.55).set_opacity(0.14), run_time=1.05, rate_func=smooth)
        self.play(FadeIn(closing_2, shift=UP * 0.12), run_time=0.66, rate_func=smooth)
        self.wait(0.65)
        self.play(FadeIn(question, shift=UP * 0.16), Circumscribe(question[0], color=GOLD, buff=0.16), run_time=0.82, rate_func=smooth)
        self.wait(2.15)

        fade_to_dark = Rectangle(
            width=config.frame_width + 0.4,
            height=config.frame_height + 0.4,
            stroke_opacity=0,
            fill_color=DEEP,
            fill_opacity=0,
        )
        fade_to_dark.set_z_index(100)
        self.add(fade_to_dark)
        self.play(fade_to_dark.animate.set_fill(opacity=1), run_time=0.95, rate_func=smooth)


# Render:
# manim -pqh projects/manim_journey_teaser.py ManimJourneyTeaser
#
# Add music after rendering, for example:
# ffmpeg -i media/videos/manim_journey_teaser/1080p60/ManimJourneyTeaser.mp4 -i music.mp3 -shortest -c:v copy -c:a aac final.mp4
