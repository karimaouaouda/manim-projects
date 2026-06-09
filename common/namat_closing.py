# -*- coding: utf-8 -*-
"""Reusable Namat brand closing animation for Manim videos."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from manim import *

from .manim_helpers import fit_to_frame, make_ar_text, make_latin_text


BACKGROUND = "#0B1020"
PRIMARY = "#EAF2FF"
ACCENT = "#38BDF8"
SECONDARY = "#A7F3D0"
MUTED = "#64748B"
WARM = "#FBBF24"

DOT_COUNT = 28
SCENE_DURATION_TARGET = 7.0
BRAND_NAME = "نمط - Namat"
SLOGAN = "كل ظاهرة لها نمط… وكل نمط له سبب"
CTA = "تابعنا لنفهم المجتمع ببساطة"


@dataclass(frozen=True)
class ClosingLayout:
    width: float
    height: float
    scale: float
    emblem_center: np.ndarray
    brand_y: float
    cta_y: float


class NamatClosingBuilder:
    """Builds and plays the Namat closing animation on any Manim scene."""

    def __init__(self, scene: Scene, seed: int = 24) -> None:
        self.scene = scene
        self.rng = np.random.default_rng(seed)
        self.layout = self._layout()

    def _layout(self) -> ClosingLayout:
        frame_width = float(config.frame_width)
        frame_height = float(config.frame_height)
        base_scale = min(frame_width / 14.222, frame_height / 8.0)
        scale = float(np.clip(base_scale, 0.58, 1.18))
        is_vertical = frame_height > frame_width * 1.22
        center_y = frame_height * (0.16 if is_vertical else 0.12)
        brand_y = center_y - (1.72 if is_vertical else 1.55) * scale
        cta_y = -frame_height * (0.35 if is_vertical else 0.38)
        return ClosingLayout(
            width=frame_width,
            height=frame_height,
            scale=scale,
            emblem_center=np.array([0.0, center_y, 0.0]),
            brand_y=brand_y,
            cta_y=cta_y,
        )

    def create_background(self) -> VGroup:
        bg = Rectangle(
            width=self.layout.width + 0.4,
            height=self.layout.height + 0.4,
            fill_color=BACKGROUND,
            fill_opacity=1,
            stroke_opacity=0,
        )
        vignette = VGroup()
        for radius, opacity in (
            (self.layout.width * 0.24, 0.045),
            (self.layout.width * 0.34, 0.025),
        ):
            glow = Circle(radius=radius, stroke_opacity=0, fill_color=ACCENT, fill_opacity=opacity)
            glow.move_to(self.layout.emblem_center)
            vignette.add(glow)

        grid = VGroup()
        x_step = self.layout.width / 9
        y_step = self.layout.height / 6
        for index in range(-4, 5):
            x = index * x_step
            line = Line(
                [x, -self.layout.height / 2, 0],
                [x, self.layout.height / 2, 0],
            )
            line.set_stroke(MUTED, width=0.6, opacity=0.08)
            grid.add(line)
        for index in range(-3, 4):
            y = index * y_step
            line = Line(
                [-self.layout.width / 2, y, 0],
                [self.layout.width / 2, y, 0],
            )
            line.set_stroke(MUTED, width=0.6, opacity=0.07)
            grid.add(line)

        particles = VGroup()
        for _ in range(22):
            x = self.rng.uniform(-self.layout.width * 0.42, self.layout.width * 0.42)
            y = self.rng.uniform(-self.layout.height * 0.38, self.layout.height * 0.38)
            particle = Dot([x, y, 0], radius=0.008 * self.layout.scale)
            particle.set_color(PRIMARY).set_opacity(self.rng.uniform(0.12, 0.24))
            particles.add(particle)

        return VGroup(bg, vignette, grid, particles).set_z_index(-10)

    def create_social_network(self) -> tuple[VGroup, VGroup, VGroup]:
        centers = np.array(
            [
                [-2.6, 0.85, 0.0],
                [-0.35, -0.28, 0.0],
                [1.75, 0.68, 0.0],
                [2.25, -0.72, 0.0],
            ],
        ) * self.layout.scale
        centers += self.layout.emblem_center

        points: list[np.ndarray] = []
        for index in range(DOT_COUNT):
            cluster = centers[index % len(centers)]
            spread = np.array(
                [
                    self.rng.normal(0, 0.54 * self.layout.scale),
                    self.rng.normal(0, 0.38 * self.layout.scale),
                    0.0,
                ],
            )
            points.append(cluster + spread)

        highlight_indices = {1, 5, 9, 14, 19, 24}
        dots = VGroup()
        for index, point in enumerate(points):
            radius = (0.048 if index in highlight_indices else 0.033) * self.layout.scale
            color = ACCENT if index in highlight_indices else PRIMARY
            dot = Dot(point, radius=radius)
            dot.set_fill(color, opacity=0.92 if index in highlight_indices else 0.42)
            dot.set_stroke(color, opacity=0)
            dots.add(dot)

        candidate_edges: list[tuple[float, int, int]] = []
        threshold = 1.25 * self.layout.scale
        for i, point_a in enumerate(points):
            for j, point_b in enumerate(points[i + 1 :], start=i + 1):
                distance = float(np.linalg.norm(point_a - point_b))
                if distance < threshold:
                    candidate_edges.append((distance, i, j))
        candidate_edges.sort(key=lambda item: item[0])

        lines = VGroup()
        used_edges: set[tuple[int, int]] = set()
        for _, i, j in candidate_edges[:42]:
            line = Line(points[i], points[j])
            line.set_stroke(MUTED, width=1.05 * self.layout.scale, opacity=0.22)
            lines.add(line)
            used_edges.add((i, j))

        path_indices = sorted(highlight_indices, key=lambda idx: points[idx][0])
        path_lines = VGroup()
        for first, second in zip(path_indices, path_indices[1:]):
            line = Line(points[first], points[second])
            line.set_stroke(ACCENT, width=2.2 * self.layout.scale, opacity=0.82)
            path_lines.add(line)

        return dots, lines, path_lines

    def create_lens(self) -> VGroup:
        lens = Circle(radius=1.22 * self.layout.scale)
        lens.set_stroke(ACCENT, width=2.2, opacity=0.62)
        lens.set_fill(ACCENT, opacity=0.06)
        inner = Circle(radius=0.86 * self.layout.scale)
        inner.set_stroke(SECONDARY, width=1.1, opacity=0.18)
        sweep_line = Line(UP * 1.12, DOWN * 1.12)
        sweep_line.set_stroke(PRIMARY, width=1.2, opacity=0.18)
        sweep_line.scale(self.layout.scale)
        return VGroup(lens, inner, sweep_line)

    def create_final_emblem(self) -> VGroup:
        center = self.layout.emblem_center
        radius = 0.92 * max(self.layout.scale, 0.72)
        ring = Circle(radius=radius)
        ring.set_stroke(ACCENT, width=2.2, opacity=0.82)

        angles = [110, 58, 8, -38, -92, -150]
        nodes = VGroup()
        node_points = []
        for index, angle in enumerate(angles):
            radians = angle * DEGREES
            point = center + np.array([np.cos(radians) * radius, np.sin(radians) * radius, 0])
            node_points.append(point)
            color = SECONDARY if index in (1, 4) else ACCENT
            node = Dot(point, radius=0.055 * self.layout.scale)
            node.set_fill(color, opacity=1)
            nodes.add(node)

        connectors = VGroup()
        for start, end in ((0, 1), (1, 2), (1, 4), (4, 5), (4, 3)):
            connector = Line(node_points[start], node_points[end])
            connector.set_stroke(PRIMARY, width=1.25 * self.layout.scale, opacity=0.55)
            connectors.add(connector)

        nucleus = Dot(center + DOWN * 0.08 * self.layout.scale, radius=0.07 * self.layout.scale)
        nucleus.set_fill(WARM, opacity=1)
        halo = Circle(radius=radius * 1.22)
        halo.set_stroke(SECONDARY, width=1.0, opacity=0.18)
        emblem = VGroup(halo, ring, connectors, nodes, nucleus)
        emblem.move_to(center)
        return emblem

    def create_brand_texts(self) -> tuple[VGroup, Text, Text, Line]:
        text_scale = max(self.layout.scale, 0.78)
        brand = make_ar_text(
            f"\u200e{BRAND_NAME}\u200e",
            font_size=50 * text_scale,
            color=PRIMARY,
            weight="BOLD",
            max_width=self.layout.width * 0.72,
        )
        brand.move_to([0, self.layout.brand_y, 0])

        slogan = make_ar_text(
            SLOGAN,
            font_size=29 * text_scale,
            color=PRIMARY,
            max_width=self.layout.width * 0.76,
        )
        slogan.next_to(brand, DOWN, buff=0.24 * text_scale)

        cta = make_ar_text(
            CTA,
            font_size=20 * text_scale,
            color=SECONDARY,
            max_width=self.layout.width * 0.64,
        )
        cta.move_to([0, self.layout.cta_y, 0])
        cta.set_opacity(0.78)

        underline = Line(LEFT * 0.38, RIGHT * 0.38)
        underline.scale(text_scale)
        underline.set_stroke(ACCENT, width=2.0 * text_scale, opacity=0.86)
        underline.next_to(brand, DOWN, buff=0.08 * text_scale)
        return brand, slogan, cta, underline

    def reset_camera(self) -> None:
        if hasattr(self.scene.camera, "frame"):
            self.scene.camera.frame.move_to(ORIGIN)
            self.scene.camera.frame.set(width=config.frame_width)

    def play(self, clear_existing: bool = True) -> None:
        self.reset_camera()
        self.scene.camera.background_color = BACKGROUND
        if clear_existing and self.scene.mobjects:
            self.scene.play(FadeOut(Group(*self.scene.mobjects), shift=DOWN * 0.12), run_time=0.35)

        background = self.create_background()
        self.scene.add(background)

        dots, lines, path_lines = self.create_social_network()
        network = VGroup(lines, path_lines, dots)
        lens = self.create_lens()
        lens.move_to(self.layout.emblem_center + LEFT * self.layout.width * 0.26)

        # Optional SFX: soft digital pulse here.
        self.scene.play(
            LaggedStart(
                *[FadeIn(dot, shift=UP * 0.06, scale=0.55) for dot in dots],
                lag_ratio=0.035,
            ),
            run_time=1.0,
            rate_func=smooth,
        )

        self.scene.play(
            LaggedStart(*[Create(line) for line in lines], lag_ratio=0.02),
            LaggedStart(*[Create(line) for line in path_lines], lag_ratio=0.12),
            run_time=1.05,
            rate_func=smooth,
        )

        # Optional SFX: subtle lens sweep whoosh here.
        self.scene.play(FadeIn(lens, scale=0.85), run_time=0.2)
        self.scene.play(
            lens.animate.move_to(self.layout.emblem_center + RIGHT * self.layout.width * 0.26),
            lines.animate.set_opacity(0.08),
            path_lines.animate.set_stroke(SECONDARY, width=3.0 * self.layout.scale, opacity=0.9),
            run_time=1.1,
            rate_func=smooth,
        )
        self.scene.play(
            ShowPassingFlash(
                path_lines.copy().set_stroke(SECONDARY, width=4.4 * self.layout.scale, opacity=0.9),
                time_width=0.55,
            ),
            run_time=0.45,
        )

        emblem = self.create_final_emblem()
        # Optional SFX: warm final logo chime here.
        self.scene.play(
            FadeOut(lens, scale=1.08),
            ReplacementTransform(network, emblem),
            run_time=1.0,
            rate_func=smooth,
        )
        self.scene.play(emblem.animate.scale(1.035), run_time=0.2, rate_func=there_and_back)

        brand, slogan, cta, underline = self.create_brand_texts()
        self.scene.play(FadeIn(brand, shift=UP * 0.12, scale=0.97), run_time=0.45)
        self.scene.play(
            Create(underline),
            FadeIn(slogan, shift=UP * 0.1),
            run_time=0.45,
            rate_func=smooth,
        )
        self.scene.play(FadeIn(cta, shift=UP * 0.08), run_time=0.3)
        self.scene.wait(0.85)


def play_namat_closing(scene: Scene, clear_existing: bool = True, seed: int = 24) -> None:
    """Append the Namat closing animation to an existing Manim scene."""

    NamatClosingBuilder(scene, seed=seed).play(clear_existing=clear_existing)
