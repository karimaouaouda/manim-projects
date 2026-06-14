# -*- coding: utf-8 -*-
"""Cinematic helper objects for vertical Namat social-analysis videos."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
from manim import *

from .arabic_text_helper import get_arabic_text
from .manim_helpers import fit_to_frame, make_latin_text
from .namat_closing import play_namat_closing


NAVY = "#061522"
DEEP_NAVY = "#030A12"
SURFACE = "#0E1F33"
SURFACE_2 = "#102942"
WHITE = "#F4F7FB"
SOFT_WHITE = "#DCE8F8"
MUTED = "#9FB3C8"
GOLD = "#F2C94C"
RED = "#FF4D4D"
CYAN = "#4DD8FF"
GREEN = "#6EE7B7"
BLACK = "#02050C"

SAFE_WIDTH = 7.35


def safe_ar_text(
    text: str,
    font_size: float = 40,
    color: str = WHITE,
    weight: str = "NORMAL",
    max_width: float = SAFE_WIDTH,
    max_height: float | None = None,
) -> Tex:
    """Create LuaLaTeX Arabic text constrained to the mobile safe area."""

    label = get_arabic_text(
        text,
        size=font_size,
        color=color,
    )
    if weight.upper() == "BOLD":
        label.set_stroke(color, width=0.25, opacity=0.35)
    return fit_to_frame(label, max_width=max_width, max_height=max_height)


def cinematic_background(seed: int = 1) -> VGroup:
    """Dark Namat background with light texture, grid, and documentary depth."""

    rng = np.random.default_rng(seed)
    base = Rectangle(
        width=config.frame_width + 0.45,
        height=config.frame_height + 0.45,
        fill_color=NAVY,
        fill_opacity=1,
        stroke_opacity=0,
    )

    depth = VGroup()
    for center, radius, color, opacity in (
        (UP * 4.9 + LEFT * 2.4, 3.5, CYAN, 0.030),
        (DOWN * 4.4 + RIGHT * 2.7, 3.1, GOLD, 0.021),
        (ORIGIN, 5.8, "#1E3A8A", 0.026),
    ):
        glow = Circle(radius=radius, stroke_opacity=0, fill_color=color, fill_opacity=opacity)
        glow.move_to(center)
        depth.add(glow)

    grid = VGroup()
    for x in np.linspace(-4.0, 4.0, 9):
        line = Line([x, -7.9, 0], [x, 7.9, 0])
        line.set_stroke(SOFT_WHITE, width=0.45, opacity=0.028)
        grid.add(line)
    for y in np.linspace(-7.0, 7.0, 10):
        line = Line([-4.35, y, 0], [4.35, y, 0])
        line.set_stroke(SOFT_WHITE, width=0.45, opacity=0.024)
        grid.add(line)

    grain = VGroup()
    for _ in range(52):
        dot = Dot(
            [
                rng.uniform(-4.1, 4.1),
                rng.uniform(-7.25, 7.25),
                0,
            ],
            radius=rng.uniform(0.004, 0.011),
            color=SOFT_WHITE,
        )
        dot.set_opacity(rng.uniform(0.06, 0.18))
        grain.add(dot)

    return VGroup(base, depth, grid, grain).set_z_index(-100)


def create_comment_bubble(
    text: str,
    tone: str = "harsh",
    width: float = 3.25,
    font_size: float = 24,
    fill_opacity: float = 0.92,
) -> VGroup:
    """Create a social-media comment bubble.

    tone can be "harsh", "neutral", or "mercy".
    """

    tone_colors = {
        "harsh": RED,
        "neutral": CYAN,
        "mercy": GOLD,
    }
    accent = tone_colors.get(tone, CYAN)
    label = safe_ar_text(
        text,
        font_size=font_size,
        color=WHITE,
        weight="BOLD" if tone == "harsh" else "NORMAL",
        max_width=width - 0.72,
        max_height=0.78,
    )
    height = max(0.62, label.height + 0.26)
    card = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.13,
        stroke_color=accent,
        stroke_width=1.9,
        fill_color=SURFACE,
        fill_opacity=fill_opacity,
    )
    avatar = Circle(
        radius=0.105,
        stroke_color=MUTED,
        stroke_width=1.1,
        fill_color=accent,
        fill_opacity=0.16,
    )
    avatar.move_to(card.get_right() + LEFT * 0.26)
    label.next_to(avatar, LEFT, buff=0.14)
    fit_to_frame(label, max_width=width - 0.62, max_height=height - 0.12)
    return VGroup(card, avatar, label)


def typewriter_text(
    text: str,
    font_size: float = 42,
    color: str = WHITE,
    weight: str = "BOLD",
    max_width: float = SAFE_WIDTH,
) -> Text:
    """Return text intended to be animated with Write for a typewriter feel."""

    return safe_ar_text(text, font_size=font_size, color=color, weight=weight, max_width=max_width)


def cinematic_fade_in(
    scene: Scene,
    *mobjects: Mobject,
    run_time: float = 0.75,
    shift: np.ndarray = UP * 0.12,
    lag_ratio: float = 0.08,
) -> None:
    """Fade objects in with a small upward drift and restrained pacing."""

    if not mobjects:
        return
    scene.play(
        LaggedStart(
            *[FadeIn(mobject, shift=shift, scale=0.98) for mobject in mobjects],
            lag_ratio=lag_ratio,
        ),
        run_time=run_time,
        rate_func=smooth,
    )


def slow_camera_push(scene: Scene, scale: float = 0.94, duration: float = 2.0) -> None:
    """Slow camera push-in for MovingCameraScene, with a group fallback."""

    frame = getattr(scene.camera, "frame", None)
    if frame is not None:
        scene.play(frame.animate.scale(scale), run_time=duration, rate_func=smooth)
        return

    if scene.mobjects:
        scene.play(Group(*scene.mobjects).animate.scale(1 / max(scale, 0.01)), run_time=duration, rate_func=smooth)


def blurred_video_placeholder(
    video_path: str | Path,
    label: str = "SYMBOLIC_BLURRED_FALL_PLACEHOLDER",
) -> VGroup:
    """Create a respectful blurred/symbolic hook frame.

    Replace this vector fallback with pre-blurred footage at the provided path.
    The Manim version keeps the scene renderable when the asset is missing.
    """

    video_path = Path(video_path)
    frame = Rectangle(
        width=config.frame_width + 0.35,
        height=config.frame_height + 0.35,
        stroke_opacity=0,
        fill_color=BLACK,
        fill_opacity=1,
    )
    vertical_slot = RoundedRectangle(
        width=config.frame_width * 0.96,
        height=config.frame_height * 0.96,
        corner_radius=0.24,
        stroke_color=CYAN,
        stroke_width=1.2,
        stroke_opacity=0.18,
        fill_color=DEEP_NAVY,
        fill_opacity=0.96,
    )

    blur_shapes = VGroup()
    blur_specs = (
        (UP * 2.7 + LEFT * 0.25, 5.4, 1.35, CYAN, 0.085, 9),
        (UP * 0.4 + RIGHT * 0.3, 4.4, 1.20, SOFT_WHITE, 0.055, -12),
        (DOWN * 2.2 + LEFT * 0.35, 5.2, 1.45, GOLD, 0.045, 7),
        (DOWN * 0.6 + RIGHT * 0.65, 2.4, 0.95, RED, 0.030, -24),
    )
    for center, width, height, color, opacity, angle in blur_specs:
        smear = Ellipse(width=width, height=height, stroke_opacity=0, fill_color=color, fill_opacity=opacity)
        smear.move_to(center)
        smear.rotate(angle * DEGREES)
        blur_shapes.add(smear)

    cliff = Polygon(
        LEFT * 4.6 + DOWN * 5.8,
        RIGHT * 4.6 + DOWN * 5.8,
        RIGHT * 2.5 + DOWN * 2.1,
        LEFT * 0.25 + DOWN * 2.9,
        LEFT * 3.6 + DOWN * 1.15,
        stroke_color=MUTED,
        stroke_width=1.4,
        fill_color=SURFACE_2,
        fill_opacity=0.52,
    )

    silhouettes = VGroup()
    for index, opacity in enumerate((0.18, 0.12, 0.07)):
        body = Line(UP * 0.28, DOWN * 0.48, stroke_color=SOFT_WHITE, stroke_width=5.0, stroke_opacity=opacity)
        head = Circle(radius=0.16, stroke_color=SOFT_WHITE, stroke_width=3.0, stroke_opacity=opacity)
        head.next_to(body, UP, buff=0.03)
        arms = Line(LEFT * 0.36 + UP * 0.04, RIGHT * 0.36 + DOWN * 0.08, stroke_color=SOFT_WHITE, stroke_width=4.0, stroke_opacity=opacity)
        person = VGroup(head, body, arms)
        person.rotate((-16 - index * 5) * DEGREES)
        person.move_to(LEFT * (0.15 + index * 0.16) + UP * (1.55 - index * 0.08))
        silhouettes.add(person)

    overlay = Rectangle(
        width=config.frame_width + 0.4,
        height=config.frame_height + 0.4,
        stroke_opacity=0,
        fill_color=NAVY,
        fill_opacity=0.48,
    )
    vignette = VGroup()
    for radius, opacity in ((5.1, 0.14), (6.4, 0.11), (7.7, 0.08)):
        ring = Circle(radius=radius)
        ring.set_stroke(BLACK, width=36, opacity=opacity)
        vignette.add(ring)

    asset_note = make_latin_text(label, font_size=11, color=MUTED, weight="BOLD", max_width=4.2)
    asset_note.move_to(DOWN * 7.1)
    asset_note.set_opacity(0.58 if not video_path.exists() else 0.22)

    return VGroup(frame, vertical_slot, blur_shapes, cliff, silhouettes, overlay, vignette, asset_note)


def phone_screen_container(
    width: float = 4.45,
    height: float = 8.25,
    accent: str = CYAN,
    fill: str = BLACK,
) -> VGroup:
    """Create a vertical phone container for social-media metaphors."""

    phone = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.38,
        stroke_color=accent,
        stroke_width=2.2,
        fill_color=fill,
        fill_opacity=0.92,
    )
    screen = RoundedRectangle(
        width=width - 0.36,
        height=height - 0.55,
        corner_radius=0.25,
        stroke_color=SOFT_WHITE,
        stroke_width=0.8,
        stroke_opacity=0.18,
        fill_color=SURFACE,
        fill_opacity=0.94,
    ).move_to(phone)
    notch = Line(LEFT * 0.34, RIGHT * 0.34, stroke_color=MUTED, stroke_width=2.0)
    notch.move_to(phone.get_top() + DOWN * 0.30)
    dot = Dot(phone.get_bottom() + UP * 0.25, radius=0.035, color=MUTED)
    return VGroup(phone, screen, notch, dot)


def comment_storm(comments: Sequence[str]) -> VGroup:
    """Create positioned harsh comment bubbles for the hook invasion."""

    positions = [
        LEFT * 2.05 + UP * 4.05,
        RIGHT * 1.55 + UP * 3.18,
        LEFT * 1.15 + UP * 1.95,
        RIGHT * 1.20 + UP * 0.82,
        LEFT * 1.75 + DOWN * 0.48,
        RIGHT * 1.45 + DOWN * 1.70,
        LEFT * 0.72 + DOWN * 2.85,
    ]
    widths = [3.4, 3.65, 3.25, 2.55, 3.35, 2.25, 2.75]
    bubbles = VGroup()
    for index, text in enumerate(comments):
        bubble = create_comment_bubble(text, tone="harsh", width=widths[index % len(widths)], font_size=22)
        bubble.move_to(positions[index % len(positions)])
        bubble.rotate(((-1) ** index) * (2 + index % 3) * DEGREES)
        bubble.set_opacity(0.96)
        bubble.set_z_index(10 + index)
        bubbles.add(bubble)
    return bubbles


def word_cloud_reveal(words: Sequence[str], colors: Sequence[str] | None = None) -> VGroup:
    """Create a spacious word cloud around the center of the vertical frame."""

    positions = [
        LEFT * 2.35 + UP * 2.55,
        RIGHT * 2.10 + UP * 2.05,
        LEFT * 2.25 + UP * 0.45,
        RIGHT * 2.35 + DOWN * 0.25,
        LEFT * 1.95 + DOWN * 2.05,
        RIGHT * 1.60 + DOWN * 2.35,
        ORIGIN + UP * 3.60,
        ORIGIN + DOWN * 3.45,
    ]
    cloud = VGroup()
    for index, word in enumerate(words):
        color = colors[index % len(colors)] if colors else (GOLD if index % 3 == 0 else CYAN if index % 2 else SOFT_WHITE)
        label = safe_ar_text(word, font_size=26, color=WHITE, weight="BOLD", max_width=2.3)
        pill = RoundedRectangle(
            width=max(1.15, label.width + 0.48),
            height=max(0.56, label.height + 0.20),
            corner_radius=0.14,
            stroke_color=color,
            stroke_width=1.7,
            fill_color=color,
            fill_opacity=0.09,
        )
        label.move_to(pill)
        item = VGroup(pill, label)
        item.move_to(positions[index % len(positions)])
        cloud.add(item)
    return cloud


def create_human_silhouette(
    scale: float = 1.0,
    color: str = SOFT_WHITE,
    accent: str = CYAN,
) -> VGroup:
    """Respectful symbolic human figure with no facial detail."""

    head = Circle(
        radius=0.24 * scale,
        stroke_color=color,
        stroke_width=3.2 * scale,
        fill_color=NAVY,
        fill_opacity=1,
    )
    head.shift(UP * 0.64 * scale)
    body = Line(UP * 0.35 * scale, DOWN * 0.72 * scale, stroke_color=color, stroke_width=4.0 * scale)
    arms = Line(LEFT * 0.42 * scale + UP * 0.05 * scale, RIGHT * 0.42 * scale + UP * 0.05 * scale, stroke_color=color, stroke_width=3.6 * scale)
    legs = VGroup(
        Line(DOWN * 0.72 * scale, LEFT * 0.30 * scale + DOWN * 1.22 * scale, stroke_color=color, stroke_width=3.6 * scale),
        Line(DOWN * 0.72 * scale, RIGHT * 0.30 * scale + DOWN * 1.22 * scale, stroke_color=color, stroke_width=3.6 * scale),
    )
    chest = Dot(DOWN * 0.10 * scale, radius=0.045 * scale, color=accent)
    return VGroup(head, body, arms, legs, chest)


def create_crater_shape(width: float = 7.3, height: float = 3.2) -> VGroup:
    """Symbolic volcanic crater made of curved contour lines."""

    base = Ellipse(
        width=width,
        height=height,
        stroke_color=MUTED,
        stroke_width=2.0,
        stroke_opacity=0.45,
        fill_color=BLACK,
        fill_opacity=0.30,
    )
    contours = VGroup()
    for index, opacity in enumerate((0.34, 0.24, 0.16)):
        arc = Arc(
            radius=1.0 + index * 0.45,
            start_angle=200 * DEGREES,
            angle=140 * DEGREES,
        )
        arc.stretch_to_fit_width(width * (0.70 - index * 0.10))
        arc.stretch_to_fit_height(height * (0.54 - index * 0.08))
        arc.set_stroke(CYAN if index == 0 else MUTED, width=1.3, opacity=opacity)
        arc.move_to(base.get_center() + DOWN * (0.08 + index * 0.16))
        contours.add(arc)
    wind = VGroup()
    for offset in (-2.2, -0.6, 1.2):
        line = Arc(radius=0.42, start_angle=15 * DEGREES, angle=120 * DEGREES)
        line.set_stroke(SOFT_WHITE, width=1.1, opacity=0.20)
        line.move_to(LEFT * offset + UP * 0.92)
        wind.add(line)
    return VGroup(base, contours, wind)


def create_scale_icon(scale: float = 1.0) -> VGroup:
    """Create a simple balance scale for the ten seconds vs full life idea."""

    stand = Line(DOWN * 0.85 * scale, UP * 0.78 * scale, stroke_color=SOFT_WHITE, stroke_width=3.0 * scale)
    beam = Line(LEFT * 1.45 * scale, RIGHT * 1.45 * scale, stroke_color=GOLD, stroke_width=3.0 * scale)
    beam.move_to(UP * 0.62 * scale)
    pivot = Dot(beam.get_center(), radius=0.055 * scale, color=GOLD)
    dishes = VGroup()
    for side in (-1, 1):
        rope = Line(beam.get_center() + RIGHT * side * 1.12 * scale, RIGHT * side * 1.12 * scale + DOWN * 0.56 * scale, stroke_color=MUTED, stroke_width=1.6 * scale)
        dish = Arc(radius=0.38 * scale, start_angle=200 * DEGREES, angle=140 * DEGREES)
        dish.set_stroke(MUTED, width=2.0 * scale, opacity=0.78)
        dish.move_to(rope.get_end() + DOWN * 0.04 * scale)
        dishes.add(VGroup(rope, dish))
    return VGroup(stand, beam, pivot, dishes)


def create_analysis_node(text: str, color: str = CYAN, width: float = 2.1) -> VGroup:
    """Small labeled node for Namat analysis networks."""

    label = safe_ar_text(text, font_size=23, color=WHITE, weight="BOLD", max_width=width - 0.34)
    box = RoundedRectangle(
        width=max(width, label.width + 0.52),
        height=max(0.62, label.height + 0.24),
        corner_radius=0.14,
        stroke_color=color,
        stroke_width=1.8,
        fill_color=color,
        fill_opacity=0.08,
    )
    label.move_to(box)
    return VGroup(box, label)


def mercy_rewrite_transition(
    scene: Scene,
    bad_mobject: Mobject,
    good_text: str = "رحمه الله",
    position: np.ndarray | None = None,
    font_size: float = 52,
) -> VGroup:
    """Dissolve a cruel phrase and rewrite it as mercy."""

    target_position = position if position is not None else bad_mobject.get_center()
    mercy = typewriter_text(good_text, font_size=font_size, color=GOLD, weight="BOLD", max_width=5.8)
    mercy.move_to(target_position)
    glow = Circle(radius=max(1.0, mercy.width * 0.32), stroke_opacity=0, fill_color=GOLD, fill_opacity=0.08)
    glow.move_to(mercy)
    scene.play(bad_mobject.animate.set_opacity(0.15).shift(DOWN * 0.08), run_time=0.35, rate_func=smooth)
    scene.play(FadeOut(bad_mobject, shift=DOWN * 0.12), FadeIn(glow, scale=0.75), run_time=0.48)
    scene.play(Write(mercy), run_time=0.85)
    return VGroup(glow, mercy)


def line_network_transition(nodes: Sequence[Mobject], color: str = CYAN) -> VGroup:
    """Connect nodes with subtle analysis lines."""

    network = VGroup()
    for first, second in zip(nodes, nodes[1:]):
        line = Line(first.get_center(), second.get_center())
        line.set_stroke(color, width=1.6, opacity=0.45)
        network.add(line)
    if len(nodes) > 2:
        line = Line(nodes[-1].get_center(), nodes[0].get_center())
        line.set_stroke(GOLD, width=1.2, opacity=0.30)
        network.add(line)
    return network


def ink_wipe_to_black(scene: Scene, source_mobject: Mobject | None = None, run_time: float = 0.55) -> Circle:
    """Soft organic black wipe for painful pauses."""

    center = source_mobject.get_center() if source_mobject is not None else ORIGIN
    wipe = Circle(radius=0.08, stroke_opacity=0, fill_color=BLACK, fill_opacity=1)
    wipe.move_to(center)
    wipe.set_z_index(80)
    scene.add(wipe)
    cover_scale = max(config.frame_width, config.frame_height) / 0.08 * 1.15
    scene.play(wipe.animate.scale(cover_scale), run_time=run_time, rate_func=smooth)
    return wipe


def namat_signature_outro(scene: Scene, clear_existing: bool = True, seed: int = 24) -> None:
    """Append the existing vertical Namat closing animation."""

    play_namat_closing(scene, clear_existing=clear_existing, seed=seed)
