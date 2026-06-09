# -*- coding: utf-8 -*-
"""Reusable Namat brand opening animation for Manim videos."""

from __future__ import annotations

from dataclasses import dataclass
import random

import numpy as np
from manim import *

from .manim_helpers import ARABIC_FONT, fit_to_frame, make_ar_text, make_latin_text
from .namat_closing import BRAND_NAME


BACKGROUND = "#0B0F19"
DEEP_BACKGROUND = "#020617"
SURFACE = "#111827"
PRIMARY = "#F8FAFC"
ACCENT = "#38BDF8"
MUTED = "#94A3B8"
DEEP_BLUE = "#1E293B"
GOLD = "#F2C94C"

OPENING_SCENE_DURATION_TARGET = 7.0
OPENING_TAGLINE = "كل ظاهرة لها نمط"
OPENING_SECONDARY_TAGLINE = "نفهم المجتمع… لا نحكم عليه"
SOCIAL_KEYWORDS = (
    "ترند",
    "رأي",
    "عادة",
    "ضغط",
    "خوف",
    "مقارنة",
    "مظهر",
    "قطيع",
)


@dataclass(frozen=True)
class OpeningLayout:
    width: float
    height: float
    scale: float
    pattern_center: np.ndarray
    title_y: float
    tagline_y: float
    is_vertical: bool


class NamatOpeningBuilder:
    """Builds and plays the Namat opening animation on any Manim scene."""

    def __init__(self, scene: Scene, seed: int = 42) -> None:
        self.scene = scene
        self.rng = np.random.default_rng(seed)
        self.py_rng = random.Random(seed)
        self.layout = self._layout()
        self.anchor_points = self._create_anchor_points(18)

    def _layout(self) -> OpeningLayout:
        frame_width = float(config.frame_width)
        frame_height = float(config.frame_height)
        is_vertical = frame_height > frame_width * 1.22
        base_scale = frame_width / 9.0 if is_vertical else frame_height / 9.0
        scale = float(np.clip(base_scale, 0.72, 1.12))
        title_y = -frame_height * (0.07 if is_vertical else 0.08)
        pattern_y = frame_height * (0.13 if is_vertical else 0.15)
        tagline_y = title_y - 0.78 * scale
        return OpeningLayout(
            width=frame_width,
            height=frame_height,
            scale=scale,
            pattern_center=np.array([0.0, pattern_y, 0.0]),
            title_y=title_y,
            tagline_y=tagline_y,
            is_vertical=is_vertical,
        )

    def _create_anchor_points(self, count: int) -> list[np.ndarray]:
        points: list[np.ndarray] = []
        for index in range(count):
            progress = index / max(count - 1, 1)
            angle = 1.35 + index * 0.62
            radius = (0.42 + progress * 2.0) * self.layout.scale
            x = np.cos(angle) * radius * (0.86 if self.layout.is_vertical else 1.05)
            y = np.sin(angle) * radius * 0.68
            points.append(self.layout.pattern_center + np.array([x, y, 0.0]))
        return points

    def reset_camera(self) -> None:
        if hasattr(self.scene.camera, "frame"):
            self.scene.camera.frame.move_to(ORIGIN)
            self.scene.camera.frame.set(width=config.frame_width)

    def create_background(self) -> VGroup:
        bg = Rectangle(
            width=self.layout.width + 0.4,
            height=self.layout.height + 0.4,
            fill_color=BACKGROUND,
            fill_opacity=1,
            stroke_opacity=0,
        )

        depth = VGroup()
        for center, radius, color, opacity in (
            (self.layout.pattern_center + UP * 0.25 * self.layout.scale, self.layout.width * 0.45, ACCENT, 0.035),
            (self.layout.pattern_center + DOWN * 0.7 * self.layout.scale, self.layout.width * 0.34, GOLD, 0.018),
            (ORIGIN, self.layout.width * 0.62, DEEP_BLUE, 0.08),
        ):
            glow = Circle(radius=radius, stroke_opacity=0, fill_color=color, fill_opacity=opacity)
            glow.move_to(center)
            depth.add(glow)

        grid = VGroup()
        x_positions = np.linspace(-self.layout.width * 0.42, self.layout.width * 0.42, 7)
        y_positions = np.linspace(-self.layout.height * 0.35, self.layout.height * 0.39, 10)
        for x in x_positions:
            for y in y_positions:
                dot = Dot([x, y, 0], radius=0.006 * self.layout.scale)
                dot.set_fill(MUTED, opacity=0.16)
                grid.add(dot)

        particles = VGroup()
        for _ in range(28):
            x = self.rng.uniform(-self.layout.width * 0.42, self.layout.width * 0.42)
            y = self.rng.uniform(-self.layout.height * 0.36, self.layout.height * 0.38)
            particle = Dot([x, y, 0], radius=self.rng.uniform(0.004, 0.009) * self.layout.scale)
            particle.set_fill(PRIMARY, opacity=self.rng.uniform(0.10, 0.22))
            particles.add(particle)

        return VGroup(bg, depth, grid, particles).set_z_index(-20)

    def _scatter_points(self, count: int) -> list[np.ndarray]:
        points: list[np.ndarray] = []
        keyword_slots = (
            (-0.24, 0.27),
            (0.20, 0.30),
            (-0.24, 0.12),
            (0.25, 0.14),
            (-0.14, 0.04),
            (0.12, 0.02),
            (-0.24, -0.07),
            (0.23, -0.08),
        )
        safe_x = self.layout.width * 0.38
        upper = self.layout.height * (0.34 if self.layout.is_vertical else 0.30)
        lower = -self.layout.height * (0.18 if self.layout.is_vertical else 0.22)
        for index in range(count):
            if index < len(keyword_slots):
                x_factor, y_factor = keyword_slots[index]
                points.append(np.array([self.layout.width * x_factor, self.layout.height * y_factor, 0.0]))
                continue

            band = index % 3
            x = self.rng.uniform(-safe_x, safe_x)
            y = self.rng.uniform(lower, upper)
            if band == 0:
                y += self.layout.height * 0.06
            if abs(x) < self.layout.width * 0.10 and abs(y - self.layout.pattern_center[1]) < self.layout.height * 0.08:
                x += np.sign(x or 1) * self.layout.width * 0.16
            points.append(np.array([x, y, 0.0]))
        return points

    def _create_keyword(self, word: str) -> Mobject:
        label = MarkupText(
            word,
            font=ARABIC_FONT,
            font_size=30 * self.layout.scale,
            color=PRIMARY,
            weight="BOLD",
        )
        fit_to_frame(label, max_width=1.58 * self.layout.scale)
        label.set_opacity(0.84)
        return label

    def _create_post_card(self, width: float, height: float) -> VGroup:
        card = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.08 * self.layout.scale,
            stroke_color=ACCENT,
            stroke_width=1.2,
            stroke_opacity=0.28,
            fill_color=SURFACE,
            fill_opacity=0.34,
        )
        avatar = Dot(card.get_left() + RIGHT * width * 0.18, radius=0.035 * self.layout.scale)
        avatar.set_fill(GOLD, opacity=0.8)
        lines = VGroup()
        for offset, line_width in ((0.10, 0.36), (-0.08, 0.48)):
            line = Line(LEFT * line_width * width, RIGHT * line_width * width)
            line.set_stroke(MUTED, width=1.1, opacity=0.42)
            line.move_to(card.get_center() + RIGHT * width * 0.16 + UP * offset * self.layout.scale)
            lines.add(line)
        return VGroup(card, avatar, lines)

    def _create_speech_bubble(self) -> VGroup:
        bubble = RoundedRectangle(
            width=0.82 * self.layout.scale,
            height=0.42 * self.layout.scale,
            corner_radius=0.10 * self.layout.scale,
            stroke_color=PRIMARY,
            stroke_width=1.1,
            stroke_opacity=0.34,
            fill_color=DEEP_BLUE,
            fill_opacity=0.22,
        )
        tail = Line(
            bubble.get_bottom() + RIGHT * 0.10 * self.layout.scale,
            bubble.get_bottom() + RIGHT * 0.25 * self.layout.scale + DOWN * 0.14 * self.layout.scale,
        )
        tail.set_stroke(PRIMARY, width=1.0, opacity=0.34)
        dots = VGroup()
        for x in (-0.16, 0.0, 0.16):
            dot = Dot(bubble.get_center() + RIGHT * x * self.layout.scale, radius=0.018 * self.layout.scale)
            dot.set_fill(ACCENT, opacity=0.56)
            dots.add(dot)
        return VGroup(bubble, tail, dots)

    def _create_phone_signal(self) -> VGroup:
        phone = RoundedRectangle(
            width=0.42 * self.layout.scale,
            height=0.72 * self.layout.scale,
            corner_radius=0.08 * self.layout.scale,
            stroke_color=ACCENT,
            stroke_width=1.2,
            stroke_opacity=0.42,
            fill_color=DEEP_BLUE,
            fill_opacity=0.18,
        )
        notch = Line(LEFT * 0.08 * self.layout.scale, RIGHT * 0.08 * self.layout.scale)
        notch.set_stroke(MUTED, width=1.0, opacity=0.46)
        notch.move_to(phone.get_top() + DOWN * 0.08 * self.layout.scale)
        heart = VGroup(
            Circle(radius=0.035 * self.layout.scale, fill_color=GOLD, fill_opacity=0.75, stroke_opacity=0),
            Circle(radius=0.035 * self.layout.scale, fill_color=GOLD, fill_opacity=0.75, stroke_opacity=0),
            Square(side_length=0.066 * self.layout.scale, fill_color=GOLD, fill_opacity=0.75, stroke_opacity=0).rotate(45 * DEGREES),
        )
        heart[0].shift(LEFT * 0.03 * self.layout.scale + UP * 0.01 * self.layout.scale)
        heart[1].shift(RIGHT * 0.03 * self.layout.scale + UP * 0.01 * self.layout.scale)
        heart.move_to(phone.get_center() + DOWN * 0.03 * self.layout.scale)
        return VGroup(phone, notch, heart)

    def create_social_signals(self) -> VGroup:
        signal_count = 18
        points = self._scatter_points(signal_count)
        signals = VGroup()

        for index, point in enumerate(points):
            if index < len(SOCIAL_KEYWORDS):
                signal = self._create_keyword(SOCIAL_KEYWORDS[index])
            elif index in (8, 12, 15):
                width = self.py_rng.uniform(0.95, 1.32) * self.layout.scale
                height = self.py_rng.uniform(0.36, 0.48) * self.layout.scale
                signal = self._create_post_card(width, height)
            elif index in (9, 14):
                signal = self._create_speech_bubble()
            elif index in (10, 16):
                signal = self._create_phone_signal()
            else:
                radius = self.py_rng.uniform(0.028, 0.050) * self.layout.scale
                signal = Dot(radius=radius, color=ACCENT)
                signal.set_fill(ACCENT if index % 2 else GOLD, opacity=0.78)

            signal.move_to(point)
            signal.rotate(self.py_rng.uniform(-7, 7) * DEGREES)
            signal.set_z_index(5 if index < len(SOCIAL_KEYWORDS) else 2)
            signals.add(signal)

        return signals

    def play_intro_noise(self, signals: VGroup) -> None:
        # Optional SFX: soft scattered digital pulses.
        self.scene.play(
            LaggedStart(
                *[FadeIn(signal, shift=UP * 0.08, scale=0.72) for signal in signals],
                lag_ratio=0.045,
            ),
            run_time=1.15,
            rate_func=smooth,
        )
        self.scene.play(
            *[
                signal.animate.shift(
                    np.array(
                        [
                            self.py_rng.uniform(-0.10, 0.10),
                            self.py_rng.uniform(-0.06, 0.08),
                            0.0,
                        ],
                    )
                    * self.layout.scale,
                )
                for signal in signals
            ],
            run_time=0.35,
            rate_func=smooth,
        )

    def create_network_from_signals(self, signals: VGroup) -> VGroup:
        lines = VGroup()
        edge_pairs = [
            (0, 1),
            (1, 4),
            (1, 5),
            (2, 5),
            (3, 6),
            (4, 7),
            (5, 8),
            (6, 9),
            (8, 10),
            (9, 11),
            (10, 12),
            (11, 13),
            (12, 15),
            (13, 16),
            (14, 17),
            (6, 14),
            (2, 12),
        ]
        for first, second in edge_pairs:
            line = Line(self.anchor_points[first], self.anchor_points[second])
            line.set_stroke(ACCENT, width=1.15 * self.layout.scale, opacity=0.34)
            lines.add(line)

        nodes = VGroup()
        for index, point in enumerate(self.anchor_points):
            color = GOLD if index in (1, 8, 14) else ACCENT
            opacity = 0.95 if index in (1, 8, 14) else 0.66
            node = Dot(point, radius=(0.038 if index in (1, 8, 14) else 0.028) * self.layout.scale)
            node.set_fill(color, opacity=opacity)
            nodes.add(node)

        return VGroup(lines, nodes)

    def play_network_reveal(self, signals: VGroup, network: VGroup) -> None:
        for signal, anchor in zip(signals, self.anchor_points):
            signal.generate_target()
            signal.target.move_to(anchor)
            signal.target.scale(0.62)
            signal.target.set_opacity(0.35)
            signal.target.set_z_index(1)

        lines, nodes = network
        # Optional SFX: a quiet whoosh as hidden links become visible.
        self.scene.play(
            AnimationGroup(*[MoveToTarget(signal) for signal in signals], lag_ratio=0.025),
            LaggedStart(*[Create(line) for line in lines], lag_ratio=0.045),
            LaggedStart(*[FadeIn(node, scale=0.7) for node in nodes], lag_ratio=0.035),
            run_time=1.75,
            rate_func=smooth,
        )
        self.scene.play(
            signals.animate.set_opacity(0.14),
            nodes.animate.set_opacity(0.95),
            run_time=0.28,
            rate_func=smooth,
        )

    def create_pattern_mark(self) -> VGroup:
        center = self.layout.pattern_center + UP * 0.05 * self.layout.scale
        arcs = VGroup()
        arc_specs = (
            (0.33, 220, 255),
            (0.55, 204, 282),
            (0.78, 196, 306),
            (1.02, 214, 270),
            (1.25, 230, 236),
            (1.48, 204, 202),
            (1.70, 232, 150),
        )
        for index, (radius, start, angle) in enumerate(arc_specs):
            arc = Arc(
                radius=radius * self.layout.scale,
                start_angle=start * DEGREES,
                angle=angle * DEGREES,
                arc_center=center,
            )
            color = ACCENT if index % 2 else PRIMARY
            opacity = 0.58 if index in (2, 3, 4) else 0.34
            arc.set_fill(opacity=0)
            arc.set_stroke(color, width=(1.25 + index * 0.05) * self.layout.scale, opacity=opacity)
            arcs.add(arc)

        breaks = VGroup()
        for radius, start, angle in ((0.93, 35, 48), (1.38, 72, 42), (1.61, -36, 34)):
            arc = Arc(
                radius=radius * self.layout.scale,
                start_angle=start * DEGREES,
                angle=angle * DEGREES,
                arc_center=center,
            )
            arc.set_fill(opacity=0)
            arc.set_stroke(GOLD, width=1.8 * self.layout.scale, opacity=0.72)
            breaks.add(arc)

        nodes = VGroup()
        for radius, angle, color in (
            (0.55, 36, GOLD),
            (0.98, 118, ACCENT),
            (1.30, -22, ACCENT),
            (1.58, 164, GOLD),
        ):
            point = center + np.array(
                [
                    np.cos(angle * DEGREES) * radius * self.layout.scale,
                    np.sin(angle * DEGREES) * radius * self.layout.scale,
                    0.0,
                ],
            )
            halo = Circle(radius=0.11 * self.layout.scale, stroke_opacity=0, fill_color=color, fill_opacity=0.10)
            halo.move_to(point)
            node = Dot(point, radius=0.044 * self.layout.scale)
            node.set_fill(color, opacity=0.95)
            nodes.add(VGroup(halo, node))

        core = Dot(center, radius=0.060 * self.layout.scale)
        core.set_fill(GOLD, opacity=0.95)
        return VGroup(arcs, breaks, nodes, core).set_z_index(3)

    def play_pattern_transform(self, signals: VGroup, network: VGroup, pattern: VGroup) -> None:
        # Optional SFX: low, clean pattern-resolution hit.
        self.scene.play(
            FadeOut(signals, scale=0.96),
            ReplacementTransform(network, pattern),
            run_time=1.20,
            rate_func=smooth,
        )
        self.scene.play(
            pattern.animate.scale(1.035),
            run_time=0.20,
            rate_func=there_and_back,
        )

    def create_brand_group(self) -> VGroup:
        title_scale = max(self.layout.scale, 0.82)
        title_ar = make_ar_text(
            "نمط",
            font_size=56 * title_scale,
            color=GOLD,
            weight="BOLD",
            max_width=self.layout.width * 0.32,
        )
        separator = make_latin_text(
            "-",
            font_size=43 * title_scale,
            color=MUTED,
            weight="BOLD",
        )
        title_en = make_latin_text(
            "Namat",
            font_size=46 * title_scale,
            color=PRIMARY,
            weight="BOLD",
            max_width=self.layout.width * 0.38,
        )
        title = VGroup(title_ar, separator, title_en).arrange(RIGHT, buff=0.15 * title_scale)
        title.move_to([0, self.layout.title_y, 0])

        tagline = make_ar_text(
            OPENING_TAGLINE,
            font_size=27 * title_scale,
            color=PRIMARY,
            max_width=self.layout.width * 0.68,
        )
        tagline.move_to([0, self.layout.tagline_y, 0])
        tagline.set_opacity(0.88)

        underline = Line(LEFT * 0.46, RIGHT * 0.46)
        underline.scale(title_scale)
        underline.set_stroke(ACCENT, width=2.0 * title_scale, opacity=0.76)
        underline.next_to(title, DOWN, buff=0.10 * title_scale)

        glow = Circle(radius=1.15 * title_scale, stroke_opacity=0, fill_color=ACCENT, fill_opacity=0.035)
        glow.move_to(title.get_center() + UP * 0.20 * title_scale)
        glow.set_z_index(-1)

        return VGroup(glow, title, underline, tagline)

    def play_brand_reveal(self, pattern: VGroup, brand_group: VGroup) -> None:
        glow, title, underline, tagline = brand_group
        pattern.generate_target()
        pattern.target.scale(0.62)
        pattern.target.move_to([0, self.layout.title_y + 1.20 * self.layout.scale, 0])
        pattern.target.set_opacity(0.56)
        pattern.target[0].set_stroke(width=0.64 * self.layout.scale, opacity=0.24)
        pattern.target[1].set_stroke(width=0.74 * self.layout.scale, opacity=0.36)
        for node_group in pattern.target[2]:
            node_group[0].set_fill(opacity=0.045)

        self.scene.play(
            MoveToTarget(pattern),
            FadeIn(glow, scale=0.75),
            FadeIn(title, shift=UP * 0.16, scale=0.96),
            run_time=0.82,
            rate_func=smooth,
        )
        # Optional SFX: small shimmer with the tagline.
        self.scene.play(
            Create(underline),
            FadeIn(tagline, shift=UP * 0.10),
            run_time=0.48,
            rate_func=smooth,
        )
        self.scene.wait(0.72)

    def play_exit_transition(self, brand_group: VGroup, pattern: VGroup) -> None:
        center = np.array([0.0, self.layout.title_y + 0.55 * self.layout.scale, 0.0])
        wipe = Circle(
            radius=0.050 * self.layout.scale,
            fill_color=DEEP_BACKGROUND,
            fill_opacity=1,
            stroke_color=ACCENT,
            stroke_width=1.4,
        )
        wipe.move_to(center)
        wipe.set_z_index(20)
        cover_scale = max(self.layout.width, self.layout.height) / max(wipe.radius, 0.01) * 1.15
        self.scene.add(wipe)
        self.scene.play(
            brand_group.animate.shift(UP * 0.12).set_opacity(0.18),
            pattern.animate.shift(UP * 0.10).set_opacity(0.10),
            wipe.animate.scale(cover_scale).set_stroke(opacity=0),
            run_time=0.48,
            rate_func=smooth,
        )
        self.scene.wait(0.10)

    def play(self, clear_existing: bool = True) -> None:
        self.reset_camera()
        self.scene.camera.background_color = BACKGROUND
        if clear_existing and self.scene.mobjects:
            self.scene.play(FadeOut(Group(*self.scene.mobjects), shift=DOWN * 0.12), run_time=0.30)

        background = self.create_background()
        self.scene.add(background)

        signals = self.create_social_signals()
        self.play_intro_noise(signals)

        network = self.create_network_from_signals(signals)
        self.play_network_reveal(signals, network)

        pattern = self.create_pattern_mark()
        self.play_pattern_transform(signals, network, pattern)

        brand_group = self.create_brand_group()
        self.play_brand_reveal(pattern, brand_group)
        self.play_exit_transition(brand_group, pattern)


def play_namat_opening(scene: Scene, clear_existing: bool = True, seed: int = 42) -> None:
    """Play the Namat opening animation on an existing Manim scene."""

    NamatOpeningBuilder(scene, seed=seed).play(clear_existing=clear_existing)
