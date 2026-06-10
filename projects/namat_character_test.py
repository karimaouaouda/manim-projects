# -*- coding: utf-8 -*-
"""Standalone Namat thinker character test.

Render from the project root:
    manim -pqh projects/namat_character_test.py NamatTalkingTest
    manim -pqh projects/namat_character_test.py NamatPoseSheet

The rendered character is imported from the provided SVG trace. When present,
``character.svg.txt`` is used as the path descriptor source, with the traced
background rectangle removed before Manim imports it.
"""

from __future__ import annotations

import math
import re
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable

import numpy as np
from manim import *


BG = "#061A33"
WHITE = "#F7F7F2"
YELLOW = "#F6C445"
TEAL = "#38D6C6"
TEAL_DARK = "#1D9EAA"
SHADOW = "#020B16"

STROKE_WIDTH_MAIN = 5
STROKE_WIDTH_DETAIL = 3
STROKE_WIDTH_SYMBOL = 2.5

HEAD_RADIUS = 1.05
HEAD_CENTER = UP * 1.0

ROOT = Path(__file__).resolve().parents[1]
SVG_CHARACTER_PATH = ROOT / "image.svg"
SVG_CHARACTER_DESCRIPTOR_PATH = ROOT / "character.svg.txt"
CLEAN_SVG_CACHE_PATH = Path(tempfile.gettempdir()) / "namat_manim_character_lines.svg"

STENCIL_BACKGROUND_PATTERN = re.compile(
    r"^M0\s+1860\s+l0\s+-1860\s+2065\s+0\s+2065\s+0\s+0\s+1860\s+0\s+1860\s+"
    r"-2065\s+0\s+-2065\s+0\s+0\s+-1860z\s+",
    re.IGNORECASE,
)


config.pixel_width = 1920
config.pixel_height = 1080
config.frame_width = 16
config.frame_height = 9
config.frame_rate = 30


def curve_from_points(points: Iterable[np.ndarray], color: str = WHITE, width: float = STROKE_WIDTH_MAIN) -> VMobject:
    curve = VMobject()
    curve.set_points_smoothly(list(points))
    curve.set_stroke(color, width=width)
    curve.set_fill(opacity=0)
    return curve


def corner_path(points: Iterable[np.ndarray], color: str = WHITE, width: float = STROKE_WIDTH_DETAIL) -> VMobject:
    path = VMobject()
    path.set_points_as_corners(list(points))
    path.set_stroke(color, width=width)
    path.set_fill(opacity=0)
    return path


def make_tiny_spark(color: str = WHITE, scale: float = 1.0) -> VGroup:
    lines = VGroup(
        Line(LEFT * 0.075, RIGHT * 0.075),
        Line(DOWN * 0.075, UP * 0.075),
        Line(LEFT * 0.052 + DOWN * 0.052, RIGHT * 0.052 + UP * 0.052),
        Line(LEFT * 0.052 + UP * 0.052, RIGHT * 0.052 + DOWN * 0.052),
    )
    lines.set_stroke(color, width=STROKE_WIDTH_SYMBOL, opacity=0.95)
    lines.scale(scale)
    return lines


def make_orbit_symbol(scale: float = 1.0) -> VGroup:
    """Small atom/orbit symbol from the SVG composition pose."""

    ring = Circle(radius=0.26)
    ring.set_style(
        stroke_color=TEAL,
        stroke_width=STROKE_WIDTH_SYMBOL,
        stroke_opacity=0.82,
        fill_color=BG,
        fill_opacity=0,
    )
    node_specs = [
        (0 * DEGREES, WHITE, 0.038),
        (120 * DEGREES, TEAL, 0.032),
        (240 * DEGREES, WHITE, 0.038),
    ]
    nodes = VGroup()
    for angle, color, radius in node_specs:
        point = np.array([math.cos(angle), math.sin(angle), 0.0]) * 0.26
        node = Dot(point, radius=radius)
        node.set_fill(color, opacity=1)
        nodes.add(node)
    center = Dot(radius=0.020)
    center.set_fill(TEAL, opacity=0.85)
    return VGroup(ring, nodes, center).scale(scale)


def make_thought_symbols() -> VGroup:
    """Small geometric idea symbols that stay light and uncrowded."""

    orbit = make_orbit_symbol(scale=0.92)
    orbit.move_to(LEFT * 1.62 + UP * 2.10)

    triangle = Triangle()
    triangle.set(width=0.22)
    triangle.set_stroke(TEAL, width=STROKE_WIDTH_SYMBOL)
    triangle.set_fill(opacity=0)
    triangle.move_to(RIGHT * 1.58 + UP * 2.64)

    square = Square(side_length=0.18)
    square.set_stroke(WHITE, width=STROKE_WIDTH_SYMBOL)
    square.set_fill(opacity=0)
    square.rotate(10 * DEGREES)
    square.move_to(RIGHT * 1.96 + UP * 1.88)

    yellow_dot = Dot(radius=0.055)
    yellow_dot.set_fill(YELLOW, opacity=1)
    yellow_dot.move_to(RIGHT * 1.16 + UP * 2.88)

    teal_circle = Circle(radius=0.085)
    teal_circle.set_stroke(TEAL, width=STROKE_WIDTH_SYMBOL)
    teal_circle.set_fill(opacity=0)
    teal_circle.move_to(RIGHT * 1.42 + UP * 2.74)

    white_spark = make_tiny_spark(WHITE, scale=0.95)
    white_spark.move_to(RIGHT * 1.72 + UP * 2.38)

    teal_dot = Dot(radius=0.025)
    teal_dot.set_fill(TEAL, opacity=0.9)
    teal_dot.move_to(RIGHT * 1.82 + UP * 2.0)

    question = Text("?", font_size=28, color=TEAL)
    question.set_stroke(TEAL_DARK, width=0.6, opacity=0.5)
    question.move_to(RIGHT * 2.18 + UP * 1.52)

    symbols = VGroup(orbit, triangle, square, yellow_dot, teal_circle, white_spark, teal_dot, question)
    symbols.set_z_index(8)
    return symbols


def make_data_icon(scale: float = 1.0) -> VGroup:
    """A compact chart icon used during the analytical gesture."""

    bars = VGroup()
    heights = [0.26, 0.46, 0.34, 0.62]
    for index, height in enumerate(heights):
        bar = Rectangle(
            width=0.12,
            height=height,
            stroke_color=TEAL,
            stroke_width=2.2,
            fill_color=TEAL_DARK,
            fill_opacity=0.16,
        )
        bar.move_to(RIGHT * (index * 0.22) + UP * (height / 2))
        bars.add(bar)

    graph_line = corner_path(
        [
            LEFT * 0.05 + UP * 0.78,
            RIGHT * 0.18 + UP * 0.98,
            RIGHT * 0.46 + UP * 0.86,
            RIGHT * 0.72 + UP * 1.16,
            RIGHT * 0.92 + UP * 1.06,
        ],
        color=WHITE,
        width=2.2,
    )
    nodes = VGroup()
    for point in graph_line.get_points()[:: max(1, len(graph_line.get_points()) // 4)]:
        node = Dot(point, radius=0.025)
        node.set_fill(WHITE, opacity=1)
        nodes.add(node)

    icon = VGroup(bars, graph_line, nodes)
    icon.move_to(ORIGIN)
    icon.scale(scale)
    return icon


def make_bulb_icon(scale: float = 1.0) -> VGroup:
    bulb = Circle(radius=0.22)
    bulb.set_stroke(YELLOW, width=2.4)
    bulb.set_fill(opacity=0)
    base = VGroup(
        Line(LEFT * 0.10 + DOWN * 0.24, RIGHT * 0.10 + DOWN * 0.24),
        Line(LEFT * 0.07 + DOWN * 0.32, RIGHT * 0.07 + DOWN * 0.32),
    )
    base.set_stroke(TEAL, width=2.2)
    rays = VGroup()
    for angle in (30, 90, 150, 210, 330):
        start = np.array([math.cos(angle * DEGREES), math.sin(angle * DEGREES), 0]) * 0.32
        end = np.array([math.cos(angle * DEGREES), math.sin(angle * DEGREES), 0]) * 0.43
        ray = Line(start, end)
        ray.set_stroke(YELLOW, width=1.8)
        rays.add(ray)
    return VGroup(bulb, base, rays).scale(scale)


def make_scene_backdrop() -> VGroup:
    background = Rectangle(
        width=config.frame_width + 0.8,
        height=config.frame_height + 0.8,
        fill_color=BG,
        fill_opacity=1,
        stroke_opacity=0,
    )

    vignette = VGroup()
    for radius, color, opacity, shift in (
        (4.8, TEAL, 0.030, LEFT * 2.8 + UP * 1.2),
        (3.8, YELLOW, 0.018, RIGHT * 3.0 + DOWN * 1.6),
        (6.0, WHITE, 0.018, ORIGIN),
    ):
        glow = Circle(radius=radius)
        glow.set_stroke(opacity=0)
        glow.set_fill(color, opacity=opacity)
        glow.move_to(shift)
        vignette.add(glow)

    dots = VGroup()
    for x in np.linspace(-7.2, 7.2, 13):
        for y in np.linspace(-3.6, 3.6, 7):
            if int((x + 8) * 10 + (y + 4) * 7) % 3 == 0:
                dot = Dot([x, y, 0], radius=0.009)
                dot.set_fill(WHITE, opacity=0.12)
                dots.add(dot)

    return VGroup(background, vignette, dots).set_z_index(-20)


def make_svg_scene_backdrop() -> VGroup:
    """Backdrop used behind the background-free imported SVG."""

    return make_scene_backdrop()


def _svg_source_path() -> Path:
    if SVG_CHARACTER_DESCRIPTOR_PATH.exists():
        return SVG_CHARACTER_DESCRIPTOR_PATH
    return SVG_CHARACTER_PATH


def _local_tag_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _strip_stencil_background(path_data: str) -> str:
    cleaned, replacements = STENCIL_BACKGROUND_PATTERN.subn("M0 1860 ", path_data, count=1)
    if replacements:
        return cleaned

    # Fallback for the same potrace-style asset if line wrapping changes.
    cleaned, replacements = re.subn(
        r"^M0\s+1860\b.*?z\s+(?=m)",
        "M0 1860 ",
        path_data,
        count=1,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return cleaned if replacements else path_data


def prepare_background_free_svg(svg_path: Path) -> Path:
    svg_path = Path(svg_path)
    if not svg_path.exists():
        raise FileNotFoundError(f"Missing SVG character asset: {svg_path}")

    svg_text = svg_path.read_text(encoding="utf-8")
    root = ET.fromstring(svg_text)
    paths = [element for element in root.iter() if _local_tag_name(element.tag) == "path"]
    if not paths:
        raise ValueError(f"SVG character asset has no path data: {svg_path}")

    paths[0].set("d", _strip_stencil_background(paths[0].attrib.get("d", "")))
    for path in paths:
        path.set("fill", "#000000")
        path.set("stroke", "none")

    CLEAN_SVG_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(CLEAN_SVG_CACHE_PATH, encoding="unicode")
    return CLEAN_SVG_CACHE_PATH


class NamatSvgCharacter(VGroup):
    """Character asset rendered from the provided SVG without its background."""

    def __init__(
        self,
        svg_path: Path | None = None,
        line_color: str = WHITE,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.source_svg_path = Path(svg_path) if svg_path is not None else _svg_source_path()
        self.svg_path = prepare_background_free_svg(self.source_svg_path)

        self.art = SVGMobject(str(self.svg_path))
        for mob in self.art.family_members_with_points():
            mob.set_fill(line_color, opacity=1)
            mob.set_stroke(line_color, width=0, opacity=0)
        self.art.set_z_index(2)
        self.add(self.art)

    def show_as_solid_trace(self, color: str = WHITE) -> "NamatSvgCharacter":
        """Fallback view for SVGs that are not stencil-style masks."""

        for mob in self.art.family_members_with_points():
            mob.set_fill(color, opacity=1)
            mob.set_stroke(color, width=0, opacity=0)
        return self


class NamatThinker(VGroup):
    """Reusable abstract philosopher character for Namat videos."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.shadow = self._build_shadow()
        self.body = self._build_body()
        self.chest_symbol = self._build_chest_symbol()
        self.support_arm_group = self._to_current_pose(self._support_arm_local())
        self.chin_arm_group = self._to_current_pose(self._chin_arm_local())
        self.arm_chin = self.chin_arm_group[0]
        self.hand_chin = self.chin_arm_group[-1]

        self.head = self._build_head()
        self.spiral_group = self._build_spiral()
        self.eyes = self.get_eyes(closed=False)
        self.eyelids = self._build_eyelids()
        self.nose = self._build_nose()
        self.mouth = self.get_mouth("neutral")
        self._mouth_mode = "neutral"

        self.thought_symbols = make_thought_symbols()

        self.body_group = VGroup(
            self.body,
            self.chest_symbol,
            self.support_arm_group,
            self.chin_arm_group,
        )
        self.face_group = VGroup(
            self.head,
            self.spiral_group,
            self.eyes,
            self.eyelids,
            self.nose,
            self.mouth,
        )
        self.core = VGroup(self.shadow, self.body_group, self.face_group)

        self.draw_order = [
            self.shadow,
            self.body,
            self.support_arm_group,
            self.chin_arm_group,
            self.head,
            self.spiral_group,
            self.eyes,
            self.eyelids,
            self.nose,
            self.mouth,
            self.chest_symbol,
            self.thought_symbols,
        ]

        self.add(self.shadow, self.body_group, self.face_group, self.thought_symbols)

    def _current_scale(self) -> float:
        return self.head.width / (HEAD_RADIUS * 2)

    def _to_current_pose(self, mobject: Mobject) -> Mobject:
        scale = self._current_scale() if hasattr(self, "head") else 1.0
        mobject.scale(scale, about_point=ORIGIN)
        if hasattr(self, "head"):
            mobject.shift(self.head.get_center() - HEAD_CENTER * scale)
        return mobject

    def _build_shadow(self) -> Ellipse:
        shadow = Ellipse(width=2.2, height=0.25)
        shadow.set_stroke(opacity=0)
        shadow.set_fill(SHADOW, opacity=0.72)
        shadow.move_to(DOWN * 1.78)
        shadow.set_z_index(-2)
        return shadow

    def _build_head(self) -> Circle:
        head = Circle(radius=HEAD_RADIUS)
        head.set_stroke(WHITE, width=STROKE_WIDTH_MAIN)
        head.set_fill(opacity=0)
        head.move_to(HEAD_CENTER)
        head.set_z_index(3)
        return head

    def _build_spiral(self) -> VGroup:
        stem = curve_from_points(
            [
                UP * 2.00 + LEFT * 0.04,
                UP * 2.20 + RIGHT * 0.22,
                UP * 2.42 + RIGHT * 0.04,
            ],
            color=WHITE,
            width=STROKE_WIDTH_MAIN,
        )

        def spiral_point(t: float) -> np.ndarray:
            radius = 0.026 + 0.017 * t
            return np.array(
                [
                    0.02 + radius * math.cos(t),
                    2.50 + radius * math.sin(t),
                    0.0,
                ],
            )

        spiral = ParametricFunction(
            spiral_point,
            t_range=[0.65, 2.72 * PI],
            color=WHITE,
            use_smoothing=True,
        )
        spiral.set_stroke(WHITE, width=STROKE_WIDTH_MAIN)

        dot = Dot(radius=0.065)
        dot.set_fill(YELLOW, opacity=1)
        dot.move_to(RIGHT * 0.02 + UP * 2.93)

        teal_orbit = Circle(radius=0.075)
        teal_orbit.set_stroke(TEAL, width=STROKE_WIDTH_SYMBOL)
        teal_orbit.set_fill(opacity=0)
        teal_orbit.move_to(RIGHT * 0.25 + UP * 2.64)

        return VGroup(stem, spiral, dot, teal_orbit).set_z_index(5)

    def get_eyes(self, closed: bool = False) -> VGroup:
        if closed:
            left_eye = Line(LEFT * 0.47 + UP * 1.13, LEFT * 0.21 + UP * 1.13)
            right_eye = Line(RIGHT * 0.21 + UP * 1.13, RIGHT * 0.47 + UP * 1.13)
            eyes = VGroup(left_eye, right_eye)
            eyes.set_stroke(WHITE, width=STROKE_WIDTH_DETAIL)
        else:
            left_eye = Ellipse(width=0.16, height=0.38)
            right_eye = Ellipse(width=0.16, height=0.38)
            for eye in (left_eye, right_eye):
                eye.set_stroke(WHITE, width=1.4)
                eye.set_fill(WHITE, opacity=1)
            left_eye.move_to(LEFT * 0.36 + UP * 1.13)
            right_eye.move_to(RIGHT * 0.36 + UP * 1.13)
            eyes = VGroup(left_eye, right_eye)
        eyes.set_z_index(6)
        return self._to_current_pose(eyes)

    def _build_eyelids(self) -> VGroup:
        left_lid = Arc(radius=0.20, start_angle=28 * DEGREES, angle=118 * DEGREES)
        right_lid = Arc(radius=0.20, start_angle=34 * DEGREES, angle=112 * DEGREES)
        left_lid.move_to(LEFT * 0.39 + UP * 1.42)
        right_lid.move_to(RIGHT * 0.37 + UP * 1.42)
        lids = VGroup(left_lid, right_lid)
        lids.set_stroke(WHITE, width=STROKE_WIDTH_DETAIL, opacity=0.86)
        lids.set_fill(opacity=0)
        lids.set_z_index(6)
        return lids

    def _build_nose(self) -> VMobject:
        nose = corner_path(
            [
                LEFT * 0.08 + UP * 1.30,
                RIGHT * 0.08 + UP * 0.88,
                LEFT * 0.10 + UP * 0.75,
            ],
            color=YELLOW,
            width=4,
        )
        nose.set_z_index(7)
        return nose

    def _mouth_local(self, mode: str) -> Mobject:
        center = RIGHT * 0.03 + UP * 0.52
        if mode == "neutral":
            mouth = Line(center + LEFT * 0.18, center + RIGHT * 0.18)
            mouth.set_stroke(WHITE, width=STROKE_WIDTH_DETAIL)
            return mouth
        if mode == "small_open":
            mouth = Ellipse(width=0.22, height=0.12)
            mouth.set_stroke(WHITE, width=STROKE_WIDTH_DETAIL)
            mouth.set_fill(BG, opacity=1)
            mouth.move_to(center + DOWN * 0.02)
            return mouth
        if mode == "wide_open":
            mouth = Ellipse(width=0.32, height=0.25)
            mouth.set_stroke(WHITE, width=STROKE_WIDTH_DETAIL)
            mouth.set_fill(BG, opacity=1)
            mouth.move_to(center + DOWN * 0.03)
            return mouth
        if mode == "smile":
            smile = curve_from_points(
                [
                    center + LEFT * 0.19 + DOWN * 0.01,
                    center + DOWN * 0.10,
                    center + RIGHT * 0.20 + DOWN * 0.01,
                ],
                color=WHITE,
                width=STROKE_WIDTH_DETAIL,
            )
            accent = Line(center + RIGHT * 0.03 + DOWN * 0.16, center + RIGHT * 0.15 + DOWN * 0.13)
            accent.set_stroke(YELLOW, width=2, opacity=0.8)
            return VGroup(smile, accent)

        raise ValueError(f"Unsupported mouth mode: {mode}")

    def get_mouth(self, mode: str) -> Mobject:
        mouth = self._mouth_local(mode)
        mouth.set_z_index(8)
        return self._to_current_pose(mouth)

    def set_mouth(self, mode: str) -> "NamatThinker":
        self.mouth.become(self.get_mouth(mode))
        self._mouth_mode = mode
        return self

    def _build_body(self) -> VGroup:
        outline = curve_from_points(
            [
                LEFT * 0.55 + DOWN * 0.05,
                LEFT * 0.92 + DOWN * 0.42,
                LEFT * 1.05 + DOWN * 1.05,
                LEFT * 0.84 + DOWN * 1.55,
                LEFT * 0.22 + DOWN * 1.70,
                RIGHT * 0.56 + DOWN * 1.68,
                RIGHT * 0.94 + DOWN * 1.20,
                RIGHT * 0.92 + DOWN * 0.58,
                RIGHT * 0.55 + DOWN * 0.05,
            ],
            color=WHITE,
            width=STROKE_WIDTH_MAIN,
        )
        lower_fold = curve_from_points(
            [
                LEFT * 0.72 + DOWN * 1.42,
                LEFT * 0.23 + DOWN * 1.42,
                RIGHT * 0.36 + DOWN * 1.05,
                RIGHT * 0.55 + DOWN * 0.76,
            ],
            color=WHITE,
            width=STROKE_WIDTH_DETAIL,
        )
        neck_shadow = curve_from_points(
            [
                LEFT * 0.36 + DOWN * 0.05,
                LEFT * 0.16 + DOWN * 0.22,
                RIGHT * 0.05 + DOWN * 0.16,
            ],
            color=WHITE,
            width=STROKE_WIDTH_DETAIL,
        )
        side_fold = Line(RIGHT * 0.77 + DOWN * 1.18, RIGHT * 0.86 + DOWN * 1.54)
        side_fold.set_stroke(WHITE, width=STROKE_WIDTH_DETAIL, opacity=0.88)

        body = VGroup(outline, lower_fold, neck_shadow, side_fold)
        body.set_z_index(1)
        return body

    def _build_chest_symbol(self) -> VGroup:
        center = LEFT * 0.56 + DOWN * 0.80

        def spiral_point(t: float) -> np.ndarray:
            radius = 0.010 + 0.012 * t
            return np.array(
                [
                    center[0] + radius * math.cos(t),
                    center[1] + radius * math.sin(t),
                    0.0,
                ],
            )

        spiral = ParametricFunction(spiral_point, t_range=[0.25, 2.2 * PI], color=YELLOW)
        spiral.set_stroke(YELLOW, width=2.4)
        top_petal = Ellipse(width=0.12, height=0.18)
        left_petal = Ellipse(width=0.18, height=0.10).rotate(34 * DEGREES)
        right_petal = Ellipse(width=0.18, height=0.10).rotate(-34 * DEGREES)
        for petal in (top_petal, left_petal, right_petal):
            petal.set_stroke(YELLOW, width=2.0, opacity=0.95)
            petal.set_fill(opacity=0)
        top_petal.move_to(center + UP * 0.13)
        left_petal.move_to(center + LEFT * 0.11 + UP * 0.03)
        right_petal.move_to(center + RIGHT * 0.11 + UP * 0.03)

        stem = curve_from_points(
            [center + DOWN * 0.03, center + DOWN * 0.20, center + LEFT * 0.05 + DOWN * 0.33],
            color=YELLOW,
            width=2.1,
        )
        leaf = curve_from_points(
            [center + DOWN * 0.20, center + RIGHT * 0.14 + DOWN * 0.24, center + RIGHT * 0.22 + DOWN * 0.14],
            color=TEAL,
            width=1.8,
        )
        accent = VGroup(stem, leaf, top_petal, left_petal, right_petal, spiral)
        accent.set_z_index(4)
        return accent

    def _support_arm_local(self) -> VGroup:
        arm = curve_from_points(
            [
                LEFT * 0.82 + DOWN * 1.22,
                LEFT * 0.42 + DOWN * 1.42,
                RIGHT * 0.18 + DOWN * 1.32,
                RIGHT * 0.48 + DOWN * 1.04,
            ],
            color=WHITE,
            width=STROKE_WIDTH_MAIN,
        )
        hand = VGroup(
            curve_from_points(
                [
                    RIGHT * 0.45 + DOWN * 1.07,
                    RIGHT * 0.55 + DOWN * 0.94,
                    RIGHT * 0.73 + DOWN * 0.96,
                    RIGHT * 0.82 + DOWN * 1.08,
                    RIGHT * 0.72 + DOWN * 1.20,
                    RIGHT * 0.53 + DOWN * 1.17,
                ],
                color=WHITE,
                width=STROKE_WIDTH_DETAIL,
            ),
            curve_from_points(
                [RIGHT * 0.54 + DOWN * 0.95, RIGHT * 0.62 + DOWN * 0.83, RIGHT * 0.70 + DOWN * 0.95],
                color=WHITE,
                width=2.4,
            ),
            curve_from_points(
                [RIGHT * 0.60 + DOWN * 0.98, RIGHT * 0.69 + DOWN * 0.90, RIGHT * 0.79 + DOWN * 1.00],
                color=WHITE,
                width=2.4,
            ),
            curve_from_points(
                [RIGHT * 0.58 + DOWN * 1.08, RIGHT * 0.71 + DOWN * 1.05, RIGHT * 0.80 + DOWN * 1.12],
                color=WHITE,
                width=2.4,
            ),
        )
        cuff = Line(RIGHT * 0.37 + DOWN * 1.12, RIGHT * 0.58 + DOWN * 0.92)
        cuff.set_stroke(WHITE, width=STROKE_WIDTH_DETAIL, opacity=0.9)
        return VGroup(arm, cuff, hand).set_z_index(4)

    def get_support_arm(self) -> VGroup:
        return self._to_current_pose(self._support_arm_local())

    def get_chin_arm(self) -> VGroup:
        return self._to_current_pose(self._chin_arm_local())

    def _open_hand_local(self, center: np.ndarray, side: int = 1, scale: float = 1.0) -> VGroup:
        """Return an open human-like line-art hand.

        ``side`` mirrors the hand so it can be reused for both arms. The
        outline follows the reference: rounded fingertips, visible thumb, and a
        broad palm instead of isolated finger strokes.
        """

        def p(x: float, y: float) -> np.ndarray:
            return center + np.array([side * x * scale, y * scale, 0.0])

        outline = curve_from_points(
            [
                p(-0.36, -0.42),
                p(-0.20, -0.19),
                p(-0.06, 0.02),
                p(-0.31, 0.10),
                p(-0.51, 0.25),
                p(-0.39, 0.34),
                p(-0.13, 0.23),
                p(0.02, 0.35),
                p(0.06, 0.58),
                p(0.16, 0.61),
                p(0.19, 0.36),
                p(0.29, 0.65),
                p(0.40, 0.68),
                p(0.42, 0.37),
                p(0.52, 0.61),
                p(0.63, 0.62),
                p(0.60, 0.31),
                p(0.72, 0.48),
                p(0.82, 0.44),
                p(0.67, 0.18),
                p(0.46, -0.02),
                p(0.18, -0.14),
                p(-0.08, -0.20),
                p(-0.36, -0.42),
            ],
            color=WHITE,
            width=STROKE_WIDTH_DETAIL,
        )

        separators = VGroup(
            curve_from_points([p(0.18, 0.30), p(0.17, 0.46), p(0.16, 0.58)], color=WHITE, width=2.0),
            curve_from_points([p(0.40, 0.31), p(0.40, 0.49), p(0.40, 0.62)], color=WHITE, width=2.0),
            curve_from_points([p(0.59, 0.25), p(0.63, 0.40), p(0.68, 0.50)], color=WHITE, width=2.0),
            curve_from_points([p(-0.08, 0.05), p(0.09, -0.01), p(0.33, 0.03)], color=WHITE, width=2.0),
            curve_from_points([p(-0.24, -0.05), p(-0.02, -0.12), p(0.20, -0.10)], color=WHITE, width=2.0),
        )
        wrist = VGroup(
            Line(p(-0.43, -0.41), p(-0.17, -0.28)),
            Line(p(-0.33, -0.50), p(-0.06, -0.36)),
        )
        wrist.set_stroke(WHITE, width=STROKE_WIDTH_DETAIL, opacity=0.9)
        return VGroup(outline, separators, wrist).set_z_index(8)

    def _explaining_arm_local(self) -> VGroup:
        arm = curve_from_points(
            [
                RIGHT * 0.58 + DOWN * 0.96,
                RIGHT * 1.08 + DOWN * 0.64,
                RIGHT * 1.42 + DOWN * 0.12,
                RIGHT * 1.54 + UP * 0.10,
            ],
            color=WHITE,
            width=STROKE_WIDTH_MAIN,
        )
        hand = self._open_hand_local(center=RIGHT * 1.58 + UP * 0.18, side=1, scale=0.62)
        return VGroup(arm, hand).set_z_index(4)

    def get_explaining_arm(self) -> VGroup:
        return self._to_current_pose(self._explaining_arm_local())

    def _left_explaining_arm_local(self) -> VGroup:
        arm = curve_from_points(
            [
                LEFT * 0.58 + DOWN * 0.96,
                LEFT * 1.08 + DOWN * 0.64,
                LEFT * 1.42 + DOWN * 0.12,
                LEFT * 1.54 + UP * 0.10,
            ],
            color=WHITE,
            width=STROKE_WIDTH_MAIN,
        )
        hand = self._open_hand_local(center=LEFT * 1.58 + UP * 0.18, side=-1, scale=0.62)
        return VGroup(arm, hand).set_z_index(4)

    def get_left_explaining_arm(self) -> VGroup:
        return self._to_current_pose(self._left_explaining_arm_local())

    def set_svg_composition_pose(self) -> "NamatThinker":
        """Switch to the open-arm pose traced in ``image.svg``."""

        self.support_arm_group.become(self.get_left_explaining_arm())
        self.chin_arm_group.become(self.get_explaining_arm())
        self.set_mouth("neutral")
        return self

    def _chin_arm_local(self) -> VGroup:
        arm = curve_from_points(
            [
                RIGHT * 0.72 + DOWN * 1.58,
                RIGHT * 0.75 + DOWN * 0.96,
                RIGHT * 0.54 + DOWN * 0.36,
                RIGHT * 0.32 + DOWN * 0.06,
            ],
            color=WHITE,
            width=STROKE_WIDTH_MAIN,
        )
        cuff = curve_from_points(
            [
                RIGHT * 0.14 + DOWN * 0.31,
                RIGHT * 0.31 + DOWN * 0.36,
                RIGHT * 0.48 + DOWN * 0.23,
            ],
            color=WHITE,
            width=STROKE_WIDTH_DETAIL,
        )
        hand = VGroup(
            curve_from_points(
                [
                    RIGHT * 0.04 + DOWN * 0.20,
                    RIGHT * 0.22 + DOWN * 0.27,
                    RIGHT * 0.42 + DOWN * 0.14,
                    RIGHT * 0.43 + UP * 0.04,
                ],
                color=WHITE,
                width=STROKE_WIDTH_DETAIL,
            ),
            curve_from_points(
                [RIGHT * 0.04 + UP * 0.09, RIGHT * 0.22 + UP * 0.18, RIGHT * 0.41 + UP * 0.11],
                color=WHITE,
                width=2.5,
            ),
            curve_from_points(
                [RIGHT * 0.02 + DOWN * 0.02, RIGHT * 0.20 + UP * 0.04, RIGHT * 0.36 + DOWN * 0.02],
                color=WHITE,
                width=2.5,
            ),
            curve_from_points(
                [LEFT * 0.02 + DOWN * 0.13, RIGHT * 0.15 + DOWN * 0.10, RIGHT * 0.29 + DOWN * 0.15],
                color=WHITE,
                width=2.5,
            ),
            curve_from_points(
                [RIGHT * 0.23 + DOWN * 0.25, RIGHT * 0.42 + DOWN * 0.10, RIGHT * 0.43 + UP * 0.04],
                color=WHITE,
                width=2.5,
            ),
        )
        hand.set_z_index(7)
        return VGroup(arm, cuff, hand).set_z_index(5)

    def blink(self, scene: Scene) -> None:
        closed = self.get_eyes(closed=True)
        opened = self.get_eyes(closed=False)
        scene.play(Transform(self.eyes, closed), run_time=0.08, rate_func=linear)
        scene.play(Transform(self.eyes, opened), run_time=0.10, rate_func=smooth)

    def talk(self, scene: Scene, duration: float = 3.0) -> None:
        sequence = [
            "small_open",
            "neutral",
            "wide_open",
            "small_open",
            "smile",
            "neutral",
            "small_open",
            "wide_open",
            "neutral",
        ]
        timings = [0.14, 0.12, 0.18, 0.14, 0.18, 0.13, 0.15, 0.19, 0.14]
        face_origin = self.face_group.get_center()
        hand_origin = self.hand_chin.get_center()

        elapsed = 0.0
        index = 0
        while elapsed < duration:
            if index % 5 == 1:
                scene.play(self.face_group.animate.shift(UP * 0.026), run_time=0.08, rate_func=smooth)
                elapsed += 0.08
            elif index % 5 == 3:
                scene.play(self.face_group.animate.move_to(face_origin), run_time=0.08, rate_func=smooth)
                elapsed += 0.08

            mode = sequence[index % len(sequence)]
            run_time = min(timings[index % len(timings)], max(0.08, duration - elapsed))
            hand_shift = UP * (0.018 if index % 2 == 0 else -0.014)
            scene.play(
                Transform(self.mouth, self.get_mouth(mode)),
                self.hand_chin.animate.shift(hand_shift),
                run_time=run_time,
                rate_func=smooth,
            )
            elapsed += run_time
            index += 1

        scene.play(
            self.face_group.animate.move_to(face_origin),
            self.hand_chin.animate.move_to(hand_origin),
            Transform(self.mouth, self.get_mouth("smile")),
            run_time=0.22,
            rate_func=smooth,
        )
        self._mouth_mode = "smile"


class NamatTalkingTest(Scene):
    """Demonstrates the SVG Namat character as a movable scene asset."""

    def construct(self) -> None:
        self.camera.background_color = BG

        backdrop = make_svg_scene_backdrop()
        namat = NamatSvgCharacter().scale(2.35).move_to(LEFT * 2.15 + DOWN * 0.06)
        namat.set_z_index(5)

        self.play(FadeIn(backdrop), run_time=0.55)
        self.play(FadeIn(namat, shift=UP * 0.18, scale=0.94), run_time=1.15, rate_func=smooth)

        self.play(
            namat.animate.shift(UP * 0.10).rotate(1.2 * DEGREES),
            run_time=1.15,
            rate_func=there_and_back,
        )
        self.play(
            namat.animate.shift(RIGHT * 0.22).scale(1.025),
            run_time=0.9,
            rate_func=there_and_back,
        )

        data_icon = make_data_icon(scale=0.78)
        data_icon.move_to(RIGHT * 2.75 + UP * 0.55)
        data_icon.set_z_index(6)

        self.play(
            namat.animate.move_to(LEFT * 2.45 + DOWN * 0.03),
            FadeIn(data_icon, shift=UP * 0.18, scale=0.82),
            run_time=0.85,
            rate_func=smooth,
        )
        self.play(
            ShowPassingFlash(
                data_icon[1].copy().set_stroke(YELLOW, width=4, opacity=0.95),
                time_width=0.55,
            ),
            namat.animate.shift(UP * 0.08),
            run_time=0.72,
            rate_func=there_and_back,
        )
        self.play(
            FadeOut(data_icon, shift=UP * 0.14),
            namat.animate.move_to(LEFT * 2.15 + DOWN * 0.06),
            run_time=0.75,
            rate_func=smooth,
        )

        self.play(
            namat.animate.shift(DOWN * 0.025).rotate(-0.7 * DEGREES),
            run_time=0.65,
            rate_func=there_and_back,
        )
        final_glow = Circle(radius=1.42)
        final_glow.set_stroke(TEAL, width=1.5, opacity=0.30)
        final_glow.set_fill(opacity=0)
        final_glow.move_to(namat.get_center() + UP * 0.48)
        final_glow.set_z_index(0)
        self.play(Create(final_glow), run_time=0.5)
        self.play(FadeOut(final_glow), run_time=0.55)
        self.wait(0.7)


class NamatPoseSheet(Scene):
    """Shows the same SVG asset moved into three reusable placements."""

    def construct(self) -> None:
        self.camera.background_color = BG
        self.add(make_svg_scene_backdrop())

        thinking = NamatSvgCharacter().scale(1.42).move_to(LEFT * 4.55 + DOWN * 0.2)

        explaining = NamatSvgCharacter().scale(1.52).move_to(DOWN * 0.15)
        bulb = make_bulb_icon(scale=0.72)
        bulb.move_to(explaining.get_center() + RIGHT * 1.82 + UP * 1.00)
        bulb.set_z_index(9)

        analyzing = NamatSvgCharacter().scale(1.42).move_to(RIGHT * 4.55 + DOWN * 0.2)
        chart = make_data_icon(scale=0.55)
        chart.move_to(analyzing.get_center() + RIGHT * 1.72 + UP * 0.55)
        chart.set_z_index(9)

        labels = VGroup(
            Text("Thinking", font_size=28, color=WHITE),
            Text("Explaining", font_size=28, color=WHITE),
            Text("Analyzing", font_size=28, color=WHITE),
        )
        for label, pose in zip(labels, (thinking, explaining, analyzing)):
            label.next_to(pose, DOWN, buff=0.22)
            label.set_opacity(0.82)

        self.play(
            LaggedStart(
                FadeIn(thinking, shift=UP * 0.15),
                FadeIn(explaining, shift=UP * 0.15),
                FadeIn(analyzing, shift=UP * 0.15),
                FadeIn(bulb, scale=0.7),
                FadeIn(chart, scale=0.7),
                FadeIn(labels, shift=UP * 0.08),
                lag_ratio=0.12,
            ),
            run_time=1.6,
            rate_func=smooth,
        )
        self.play(
            thinking.animate.shift(UP * 0.05).rotate(1.5 * DEGREES),
            explaining.animate.shift(UP * 0.08),
            analyzing.animate.shift(UP * 0.05).rotate(-1.5 * DEGREES),
            run_time=0.9,
            rate_func=there_and_back,
        )
        self.wait(1.2)
