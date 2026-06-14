# -*- coding: utf-8 -*-
"""Vertical hidden-pattern intro video for نمط - Namat.

Render from the project root:
    manim -pqh projects/namat_intro_hidden_pattern_vertical.py NamatIntroVideo

This script follows the social-analysis reveal brief while avoiding character
or mascot visuals. The final brand outro reuses the existing vertical closing.
"""

from __future__ import annotations

import math
import random
import sys
from pathlib import Path
from typing import Iterable

import numpy as np
from manim import *

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.manim_helpers import fit_to_frame, make_ar_text, make_latin_text
from common.namat_closing import play_namat_closing


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30


BG = "#071421"
DEEP_BG = "#030A12"
CARD = "#0D1D2D"
CARD_2 = "#10283D"
WHITE = "#F4F7FB"
MUTED = "#8EA4B8"
GOLD = "#F6C85F"
RED = "#F25F5C"
CYAN = "#3DDCFF"
GREEN = "#6EE7B7"
BLUE = "#2F6BFF"
VIOLET = "#B589FF"

SAFE_TEXT_WIDTH = 7.35
PROFILE_DIR = ROOT / "assets" / "profiles"


def make_arabic_text(
    text: str,
    size: float = 42,
    color: str = WHITE,
    weight: str = "NORMAL",
    max_width: float = SAFE_TEXT_WIDTH,
    max_height: float | None = None,
) -> Text:
    return make_ar_text(
        text,
        font_size=size,
        color=color,
        weight=weight,
        max_width=max_width,
        max_height=max_height,
    )


def make_english_text(
    text: str,
    size: float = 28,
    color: str = WHITE,
    weight: str = "NORMAL",
    max_width: float | None = None,
) -> Text:
    return make_latin_text(text, font_size=size, color=color, weight=weight, max_width=max_width)


def safe_title(text: str, y: float = 5.35, size: float = 44, color: str = WHITE) -> Text:
    title = make_arabic_text(text, size=size, color=color, weight="BOLD", max_width=SAFE_TEXT_WIDTH)
    title.move_to([0, y, 0])
    return title


def make_caption(text: str, y: float = -4.85, color: str = WHITE, accent: str = CYAN) -> VGroup:
    label = make_arabic_text(text, size=30, color=color, weight="BOLD", max_width=6.7)
    label.move_to([0, y, 0])
    box = RoundedRectangle(
        width=max(2.1, label.width + 0.62),
        height=max(0.72, label.height + 0.24),
        corner_radius=0.15,
        stroke_color=accent,
        stroke_width=1.8,
        fill_color=CARD,
        fill_opacity=0.82,
    )
    box.move_to(label)
    return VGroup(box, label)


def make_pill(
    text: str,
    color: str = CYAN,
    size: float = 27,
    width: float | None = None,
    fill_opacity: float = 0.12,
    is_arabic:bool = True
) -> VGroup:
    label_width = (width or 2.5) - 0.18
    if is_arabic:
        label = make_arabic_text(
        f"\u200f{text}\u200f",
        size=size,
        color=WHITE,
        weight="BOLD",
        max_width=label_width,
    )
    else:
        label = make_latin_text(
            f"\u200f{text}\u200f",
            size=size,
            color=WHITE,
            weight="BOLD",
            max_width=label_width,
        )
    box = RoundedRectangle(
        width=width or max(1.35, label.width + 0.55),
        height=max(0.56, label.height + 0.20),
        corner_radius=0.14,
        stroke_color=color,
        stroke_width=1.9,
        fill_color=color,
        fill_opacity=fill_opacity,
    )
    box.set_z_index(1)
    label.move_to(box)
    label.set_z_index(5)
    return VGroup(box, label)


def full_screen_background(seed: int = 10) -> VGroup:
    rng = np.random.default_rng(seed)
    base = Rectangle(
        width=config.frame_width + 0.45,
        height=config.frame_height + 0.45,
        fill_color=BG,
        fill_opacity=1,
        stroke_opacity=0,
    )

    glows = VGroup()
    for center, radius, color, opacity in (
        (UP * 4.8 + LEFT * 2.2, 3.8, CYAN, 0.030),
        (DOWN * 2.6 + RIGHT * 2.4, 3.4, GOLD, 0.024),
        (ORIGIN, 5.6, BLUE, 0.025),
    ):
        glow = Circle(radius=radius, stroke_opacity=0, fill_color=color, fill_opacity=opacity)
        glow.move_to(center)
        glows.add(glow)

    grid = VGroup()
    for x in np.linspace(-4.0, 4.0, 9):
        line = Line([x, -7.8, 0], [x, 7.8, 0])
        line.set_stroke(WHITE, width=0.45, opacity=0.035)
        grid.add(line)
    for y in np.linspace(-6.8, 6.8, 9):
        line = Line([-4.35, y, 0], [4.35, y, 0])
        line.set_stroke(WHITE, width=0.45, opacity=0.030)
        grid.add(line)

    particles = VGroup()
    for _ in range(42):
        particle = Dot(
            [
                rng.uniform(-4.1, 4.1),
                rng.uniform(-7.0, 6.9),
                0,
            ],
            radius=rng.uniform(0.006, 0.014),
        )
        particle.set_fill(WHITE, opacity=rng.uniform(0.10, 0.24))
        particles.add(particle)

    return VGroup(base, glows, grid, particles).set_z_index(-100)


def create_glow_dot(point: Iterable[float], color: str = CYAN, radius: float = 0.055) -> VGroup:
    center = np.array(point, dtype=float)
    halo = Circle(radius=radius * 3.2, stroke_opacity=0, fill_color=color, fill_opacity=0.12)
    halo.move_to(center)
    dot = Dot(center, radius=radius, color=color)
    return VGroup(halo, dot)


def create_clock(scale: float = 1.0) -> VGroup:
    face = Circle(radius=0.42 * scale, stroke_color=MUTED, stroke_width=2.2, fill_color=CARD, fill_opacity=0.8)
    hour = Line(ORIGIN, UP * 0.22 * scale, stroke_color=WHITE, stroke_width=2.4)
    minute = Line(ORIGIN, RIGHT * 0.30 * scale, stroke_color=CYAN, stroke_width=2.1)
    center = Dot(radius=0.025 * scale, color=GOLD)
    return VGroup(face, hour, minute, center)


def create_document(label: str, width: float = 1.45, height: float = 1.95, accent: str = CYAN) -> VGroup:
    page = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.08,
        stroke_color=accent,
        stroke_width=2.0,
        fill_color=CARD_2,
        fill_opacity=0.92,
    )
    title = make_arabic_text(label, size=22, color=WHITE, weight="BOLD", max_width=width - 0.25)
    title.move_to(page.get_top() + DOWN * 0.36)
    lines = VGroup()
    for offset, opacity in ((0.18, 0.42), (-0.13, 0.35), (-0.44, 0.24)):
        line = Line(LEFT * width * 0.30, RIGHT * width * 0.30, stroke_color=MUTED, stroke_width=1.4, stroke_opacity=opacity)
        line.move_to(page.get_center() + DOWN * offset)
        lines.add(line)
    return VGroup(page, title, lines)


def create_phone(scale: float = 1.0, accent: str = CYAN) -> VGroup:
    phone = RoundedRectangle(
        width=1.28 * scale,
        height=2.32 * scale,
        corner_radius=0.16 * scale,
        stroke_color=accent,
        stroke_width=2.2 * scale,
        fill_color=DEEP_BG,
        fill_opacity=0.95,
    )
    screen = RoundedRectangle(
        width=1.08 * scale,
        height=1.92 * scale,
        corner_radius=0.09 * scale,
        stroke_opacity=0,
        fill_color=CARD,
        fill_opacity=0.96,
    ).move_to(phone)
    notch = Line(LEFT * 0.18 * scale, RIGHT * 0.18 * scale, stroke_color=MUTED, stroke_width=1.4 * scale)
    notch.move_to(phone.get_top() + DOWN * 0.16 * scale)
    posts = VGroup()
    for index, (y, color) in enumerate(((0.45, GOLD), (-0.05, CYAN), (-0.55, GREEN))):
        post = RoundedRectangle(
            width=0.78 * scale,
            height=0.28 * scale,
            corner_radius=0.04 * scale,
            stroke_opacity=0,
            fill_color=color,
            fill_opacity=0.18,
        )
        post.move_to(phone.get_center() + UP * y * scale)
        posts.add(post)
    return VGroup(phone, screen, notch, posts)


def create_idea_icon(scale: float = 1.0) -> VGroup:
    bulb = Circle(radius=0.36 * scale, stroke_color=GOLD, stroke_width=2.4 * scale, fill_color=GOLD, fill_opacity=0.12)
    stem = RoundedRectangle(
        width=0.35 * scale,
        height=0.22 * scale,
        corner_radius=0.04 * scale,
        stroke_color=GOLD,
        stroke_width=2.0 * scale,
        fill_color=CARD,
        fill_opacity=0.9,
    )
    stem.next_to(bulb, DOWN, buff=-0.02 * scale)
    rays = VGroup()
    for angle in (45, 90, 135, 210, 330):
        start = np.array([math.cos(angle * DEGREES), math.sin(angle * DEGREES), 0]) * 0.52 * scale
        end = np.array([math.cos(angle * DEGREES), math.sin(angle * DEGREES), 0]) * 0.72 * scale
        ray = Line(start, end, stroke_color=GOLD, stroke_width=1.8 * scale, stroke_opacity=0.75)
        rays.add(ray)
    return VGroup(rays, bulb, stem)


def create_speech_bubble(text: str, color: str = RED, scale: float = 1.0, width: float = 1.65) -> VGroup:
    label = make_arabic_text(text, size=18 * scale, color=WHITE, weight="BOLD", max_width=width * scale - 0.35)
    box = RoundedRectangle(
        width=width * scale,
        height=max(0.46 * scale, label.height + 0.14 * scale),
        corner_radius=0.10 * scale,
        stroke_color=color,
        stroke_width=1.5 * scale,
        fill_color=color,
        fill_opacity=0.12,
    )
    label.move_to(box)
    return VGroup(box, label)


def create_node_icon(kind: str, scale: float = 1.0, color: str = CYAN) -> VGroup:
    if kind == "diploma":
        doc = create_document("ديبلوم", width=0.95 * scale, height=1.18 * scale, accent=color)
        ribbon = Circle(radius=0.12 * scale, stroke_color=GOLD, stroke_width=1.6 * scale, fill_color=GOLD, fill_opacity=0.18)
        ribbon.move_to(doc[0].get_bottom() + UP * 0.18 * scale + RIGHT * 0.26 * scale)
        return VGroup(doc, ribbon)

    if kind == "bac":
        paper = create_document("BAC", width=0.95 * scale, height=1.10 * scale, accent=color)
        mini = VGroup(
            make_pill("طب", GOLD, size=12 * scale, width=0.48 * scale),
            make_pill("AI", CYAN, size=12 * scale, width=0.50 * scale),
        ).arrange(RIGHT, buff=0.05 * scale)
        mini.next_to(paper, DOWN, buff=0.07 * scale)
        return VGroup(paper, mini)

    if kind == "idea":
        return create_idea_icon(scale=scale)

    if kind == "phone":
        return create_phone(scale=0.78 * scale, accent=color)

    if kind == "pressure":
        core = create_glow_dot(ORIGIN, color=RED, radius=0.07 * scale)
        ring = Circle(radius=0.46 * scale, stroke_color=RED, stroke_width=1.8 * scale, stroke_opacity=0.54)
        bubbles = VGroup()
        for angle in (35, 150, 270):
            bubble = Circle(radius=0.085 * scale, fill_color=RED, fill_opacity=0.28, stroke_opacity=0)
            bubble.move_to(np.array([math.cos(angle * DEGREES), math.sin(angle * DEGREES), 0]) * 0.55 * scale)
            bubbles.add(bubble)
        return VGroup(ring, bubbles, core)

    return create_glow_dot(ORIGIN, color=color, radius=0.08 * scale)


def create_social_node(label: str, kind: str, color: str = CYAN) -> VGroup:
    shell = Circle(radius=0.66, stroke_color=color, stroke_width=2.4, fill_color=CARD, fill_opacity=0.92)
    icon = create_node_icon(kind, scale=0.78, color=color)
    icon.move_to(shell)
    text = make_arabic_text(label, size=20, color=WHITE, weight="BOLD", max_width=1.55)
    text.next_to(shell, DOWN, buff=0.13)
    return VGroup(shell, icon, text)


def pulse_line_between(p1: Iterable[float], p2: Iterable[float], color: str = CYAN, width: float = 3) -> VGroup:
    line = Line(np.array(p1), np.array(p2), stroke_color=color, stroke_width=width, stroke_opacity=0.72)
    pulse = Dot(line.get_start(), radius=0.045, color=GOLD)
    return VGroup(line, pulse)


def connect_concepts(start_mob: Mobject, end_mob: Mobject, label: str | None = None, color: str = CYAN) -> VGroup:
    line = Line(start_mob.get_center(), end_mob.get_center(), color=color, stroke_width=2.5)
    line.set_opacity(0.72)
    pulse = Dot(line.get_start(), color=GOLD).scale(0.55)
    group = VGroup(line, pulse)
    if label:
        tag = make_arabic_text(label, size=17, color=MUTED, max_width=1.4)
        tag.move_to(line.point_from_proportion(0.5) + UP * 0.15)
        group.add(tag)
    return group


def create_magnifier(scale: float = 1.0) -> VGroup:
    lens = Circle(radius=0.42 * scale, stroke_color=CYAN, stroke_width=2.3 * scale, fill_color=CYAN, fill_opacity=0.055)
    handle = Line(
        lens.get_bottom() + RIGHT * 0.28 * scale,
        lens.get_bottom() + RIGHT * 0.72 * scale + DOWN * 0.48 * scale,
        stroke_color=CYAN,
        stroke_width=2.5 * scale,
    )
    shine = Arc(radius=0.27 * scale, start_angle=55 * DEGREES, angle=72 * DEGREES, stroke_color=WHITE, stroke_width=1.3 * scale, stroke_opacity=0.42)
    shine.move_to(lens)
    return VGroup(lens, shine, handle)


def create_brain_icon(scale: float = 1.0) -> VGroup:
    lobes = VGroup()
    for point in (LEFT * 0.24 + UP * 0.10, ORIGIN + UP * 0.22, RIGHT * 0.24 + UP * 0.10, LEFT * 0.12 + DOWN * 0.12, RIGHT * 0.14 + DOWN * 0.12):
        circle = Circle(radius=0.18 * scale, stroke_color=CYAN, stroke_width=1.7 * scale, fill_color=CYAN, fill_opacity=0.08)
        circle.move_to(point * scale)
        lobes.add(circle)
    stem = Line(DOWN * 0.18 * scale, DOWN * 0.42 * scale, stroke_color=CYAN, stroke_width=1.8 * scale)
    return VGroup(lobes, stem)


def create_heart_icon(scale: float = 1.0) -> VGroup:
    left = Circle(radius=0.18 * scale, fill_color=RED, fill_opacity=0.16, stroke_color=RED, stroke_width=1.8 * scale)
    right = left.copy().shift(RIGHT * 0.25 * scale)
    left.shift(LEFT * 0.25 * scale)
    bottom = Square(side_length=0.36 * scale, fill_color=RED, fill_opacity=0.16, stroke_color=RED, stroke_width=1.8 * scale)
    bottom.rotate(45 * DEGREES)
    bottom.shift(DOWN * 0.13 * scale)
    return VGroup(left, right, bottom)


def create_compass(scale: float = 1.0) -> VGroup:
    ring = Circle(radius=1.0 * scale, stroke_color=MUTED, stroke_width=1.8 * scale, stroke_opacity=0.55)
    inner = Circle(radius=0.64 * scale, stroke_color=CYAN, stroke_width=1.2 * scale, stroke_opacity=0.28)
    needle = Polygon(
        UP * 0.78 * scale,
        LEFT * 0.08 * scale,
        RIGHT * 0.08 * scale,
        stroke_color=GOLD,
        stroke_width=1.5 * scale,
        fill_color=GOLD,
        fill_opacity=0.82,
    )
    counter = Polygon(
        DOWN * 0.62 * scale,
        LEFT * 0.06 * scale,
        RIGHT * 0.06 * scale,
        stroke_color=MUTED,
        stroke_width=1.2 * scale,
        fill_color=MUTED,
        fill_opacity=0.45,
    )
    center = Dot(radius=0.055 * scale, color=WHITE)
    return VGroup(ring, inner, needle, counter, center)


def make_phone_card(platform: str, image_path: Path | None = None, scale: float = 1.0) -> Group:
    platform_colors = {
        "Facebook": "#1877F2",
        "Instagram": "#E1306C",
        "TikTok": "#25F4EE",
    }
    accent = platform_colors.get(platform, CYAN)

    phone = RoundedRectangle(
        width=2.08,
        height=4.24,
        corner_radius=0.22,
        stroke_color=accent,
        stroke_width=2.1,
        fill_color=DEEP_BG,
        fill_opacity=0.96,
    )
    screen = RoundedRectangle(
        width=1.86,
        height=3.84,
        corner_radius=0.14,
        stroke_color=WHITE,
        stroke_width=0.7,
        stroke_opacity=0.16,
        fill_color=CARD,
        fill_opacity=0.95,
    ).move_to(phone)

    if image_path and image_path.exists():
        image = ImageMobject(str(image_path))
        fit_to_frame(image, max_width=1.72, max_height=3.60)
        image.move_to(screen)
        content: Mobject = Group(image)
    else:
        avatar = Circle(radius=0.34, stroke_color=GOLD, stroke_width=2.0, fill_color=GOLD, fill_opacity=0.12)
        avatar.move_to(screen.get_top() + DOWN * 0.68)
        avatar_text = make_arabic_text("\u200fنمط\u200f", size=21, color=GOLD, weight="BOLD", max_width=0.78)
        avatar_text.move_to(avatar)
        name = make_arabic_text("\u200eنمط - Namat\u200e", size=16, color=WHITE, weight="BOLD", max_width=1.78)
        name.next_to(avatar, DOWN, buff=0.15)
        handle = make_english_text("@namat.dz", size=15, color=MUTED, weight="BOLD", max_width=1.35)
        handle.next_to(name, DOWN, buff=0.07)
        button = RoundedRectangle(
            width=1.23,
            height=0.34,
            corner_radius=0.08,
            stroke_opacity=0,
            fill_color=accent,
            fill_opacity=0.82,
        )
        button.next_to(handle, DOWN, buff=0.15)
        button_text = make_english_text("Follow", size=13, color=DEEP_BG, weight="BOLD", max_width=0.95)
        button_text.move_to(button)
        thumbs = VGroup()
        for i in range(3):
            thumb = RoundedRectangle(
                width=0.48,
                height=0.58,
                corner_radius=0.05,
                stroke_color=accent,
                stroke_width=1.1,
                fill_color=accent,
                fill_opacity=0.10 + i * 0.03,
            )
            arc = Arc(radius=0.15, start_angle=(20 + i * 30) * DEGREES, angle=230 * DEGREES)
            arc.set_stroke(GOLD if i == 1 else CYAN, width=1.1, opacity=0.62)
            arc.move_to(thumb)
            thumbs.add(VGroup(thumb, arc))
        thumbs.arrange(RIGHT, buff=0.10)
        thumbs.move_to(screen.get_bottom() + UP * 0.67)
        content = VGroup(avatar, avatar_text, name, handle, button, button_text, thumbs)

    platform_label = make_english_text(platform, size=17, color=WHITE, weight="BOLD", max_width=1.55)
    platform_label.next_to(phone, DOWN, buff=0.16)
    card = Group(phone, screen, content, platform_label)
    card.scale(scale)
    return card


def morph_points_to_word(points_group: VGroup, word_text: Text) -> Animation:
    return ReplacementTransform(points_group, word_text)


class NamatIntroVideo(MovingCameraScene):
    """Cinematic social-analysis short that reveals the hidden concept نمط."""

    def construct(self) -> None:
        self.rng = random.Random(71)
        self.setup_scene()
        self.scene_00_pre_hook()
        self.scene_01_social_montage()
        self.scene_02_pattern_network()
        self.scene_03_invisible_script()
        self.scene_04_detective_board()
        self.scene_05_maze()
        self.scene_06_missing_letters()
        self.scene_07_namat_reveal()
        self.scene_08_project_meaning()
        self.scene_09_moral_depth()
        self.scene_10_profiles_reveal()
        self.scene_11_existing_outro()

    def setup_scene(self) -> None:
        self.camera.background_color = BG
        self.background = full_screen_background(seed=21)
        self.add(self.background)

    def reset_camera(self) -> None:
        self.camera.frame.move_to(ORIGIN)
        self.camera.frame.set(width=config.frame_width)

    def clear_scene(self, run_time: float = 0.52) -> None:
        self.reset_camera()
        removable = [m for m in self.mobjects if m is not self.background]
        if removable:
            self.play(FadeOut(Group(*removable), shift=DOWN * 0.10), run_time=run_time)

    def pulse_camera(self, scale: float = 0.96, run_time: float = 0.22) -> None:
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(scale), run_time=run_time, rate_func=smooth)
        self.play(Restore(self.camera.frame), run_time=run_time, rate_func=smooth)

    def scene_00_pre_hook(self) -> None:
        self.clear_scene(run_time=0.05)
        dot = Dot(ORIGIN, radius=0.055, color=WHITE)
        halo = Circle(radius=0.35, stroke_opacity=0, fill_color=CYAN, fill_opacity=0.0)
        glitch_dots = VGroup()
        for _ in range(36):
            angle = self.rng.uniform(0, TAU)
            radius = self.rng.uniform(0.35, 3.4)
            point = np.array([math.cos(angle) * radius, math.sin(angle) * radius * 1.35, 0])
            small = Dot(point, radius=self.rng.uniform(0.008, 0.018), color=CYAN if self.rng.random() > 0.35 else GOLD)
            small.set_opacity(self.rng.uniform(0.15, 0.48))
            glitch_dots.add(small)

        hook = safe_title("كاين حاجة راهي تتعاود...", y=1.12, size=39, color=WHITE)
        self.play(GrowFromCenter(dot), run_time=0.20)
        self.play(
            dot.animate.scale(2.3).set_color(GOLD),
            halo.animate.set_fill(opacity=0.13).scale(2.4),
            run_time=0.28,
            rate_func=there_and_back,
        )
        self.play(FadeIn(glitch_dots, scale=0.65), FadeIn(hook, shift=UP * 0.12), run_time=0.65)
        self.wait(0.35)

        split_points = [
            LEFT * 2.9 + UP * 2.6,
            RIGHT * 2.3 + UP * 2.2,
            LEFT * 2.5 + DOWN * 0.85,
            RIGHT * 2.7 + DOWN * 1.0,
            UP * 0.15,
        ]
        seeds = VGroup(*[Dot(ORIGIN, radius=0.046, color=CYAN if i % 2 else GOLD) for i in range(5)])
        self.play(
            FadeOut(hook, shift=UP * 0.18),
            FadeOut(glitch_dots, scale=1.1),
            FadeOut(halo),
            TransformFromCopy(dot, seeds),
            run_time=0.35,
        )
        self.play(
            AnimationGroup(*[seed.animate.move_to(point) for seed, point in zip(seeds, split_points)], lag_ratio=0.04),
            FadeOut(dot),
            run_time=0.62,
            rate_func=smooth,
        )
        self.seed_dots = seeds

    def create_montage_scene(self, kind: str, title: str, color: str = CYAN) -> VGroup:
        header = safe_title(title, y=5.45, size=38, color=WHITE)
        anchor = VGroup()

        if kind == "diploma":
            doc = create_document("ديبلوم", width=1.82, height=2.35, accent=CYAN)
            doc.move_to(LEFT * 1.45 + UP * 0.52)
            chair = VGroup(
                RoundedRectangle(width=0.88, height=0.62, corner_radius=0.10, stroke_color=MUTED, fill_color=CARD, fill_opacity=0.55),
                Line(LEFT * 0.32 + DOWN * 0.31, LEFT * 0.45 + DOWN * 1.0, stroke_color=MUTED, stroke_width=3),
                Line(RIGHT * 0.32 + DOWN * 0.31, RIGHT * 0.45 + DOWN * 1.0, stroke_color=MUTED, stroke_width=3),
                Line(LEFT * 0.43 + DOWN * 0.02, RIGHT * 0.43 + DOWN * 0.02, stroke_color=MUTED, stroke_width=3),
            )
            chair.move_to(RIGHT * 1.35 + UP * 0.1)
            job = make_pill("Job", color=GOLD, size=24, width=1.55)
            job.next_to(chair, UP, buff=0.36)
            clock = create_clock(scale=1.1)
            clock.move_to(UP * 2.35)
            anchor.add(doc, chair, job, clock)

        elif kind == "bac":
            result = create_document("نتيجة الباك", width=1.75, height=2.05, accent=GOLD)
            result.move_to(UP * 0.92)
            cards = VGroup()
            labels = ["الطب", "الإعلام الآلي", "الحقوق", "المدرسة العليا", "البيولوجيا"]
            for index, label in enumerate(labels):
                card = make_pill(label, color=RED if index in (0, 3) else CYAN, size=19, width=1.55)
                angle = PI / 2 - index * TAU / len(labels)
                card.move_to(np.array([2.45 * math.cos(angle), 1.55 * math.sin(angle) - 0.35, 0]))
                cards.add(card)
            anchor.add(result, cards)

        elif kind == "idea":
            idea = create_idea_icon(scale=1.75)
            idea.move_to(UP * 0.84)
            idea_label = make_pill("الفكرة", color=GOLD, size=28, width=1.42)
            idea_label.next_to(idea, DOWN, buff=0.34)
            bubbles = VGroup(
                create_speech_bubble("ما تصلحش هنا", RED, scale=1.0, width=1.9),
                create_speech_bubble("شكون يشري؟", RED, scale=1.0, width=1.65),
                create_speech_bubble("خليك مضمون", RED, scale=1.0, width=1.78),
            )
            for bubble, point in zip(bubbles, [LEFT * 2.55 + UP * 1.95, RIGHT * 2.45 + UP * 1.45, RIGHT * 1.8 + DOWN * 1.52]):
                bubble.move_to(point)
            anchor.add(idea, idea_label, bubbles)

        elif kind == "phone":
            phone = create_phone(scale=1.55, accent=CYAN)
            phone.move_to(LEFT * 0.95 + UP * 0.35)
            likes = VGroup()
            for index in range(9):
                heart = VGroup(
                    Circle(radius=0.045, stroke_opacity=0, fill_color=RED, fill_opacity=0.88),
                    Circle(radius=0.045, stroke_opacity=0, fill_color=RED, fill_opacity=0.88),
                    Square(side_length=0.083, stroke_opacity=0, fill_color=RED, fill_opacity=0.88).rotate(45 * DEGREES),
                )
                heart[0].shift(LEFT * 0.035 + UP * 0.018)
                heart[1].shift(RIGHT * 0.035 + UP * 0.018)
                heart.scale(self.rng.uniform(0.75, 1.15))
                heart.move_to(RIGHT * self.rng.uniform(1.0, 2.4) + DOWN * self.rng.uniform(-1.4, 1.8))
                likes.add(heart)
            path = VGroup(
                Line(LEFT * 0.25, RIGHT * 1.05, stroke_color=MUTED, stroke_width=3, stroke_opacity=0.50),
                Line(RIGHT * 1.05, RIGHT * 1.55 + UP * 0.58, stroke_color=GOLD, stroke_width=3, stroke_opacity=0.78),
            )
            path.move_to(DOWN * 2.1)
            anchor.add(phone, likes, path)

        elif kind == "pressure":
            center = Dot(ORIGIN + UP * 0.15, radius=0.12, color=GOLD)
            rings = VGroup()
            for radius, opacity in ((0.85, 0.35), (1.35, 0.23), (1.9, 0.16)):
                ring = Circle(radius=radius, stroke_color=RED, stroke_width=2.2, stroke_opacity=opacity)
                rings.add(ring)
            bubbles = VGroup()
            # use difff sentences of comparison to create a more dynamic scene (diff meaning but same pressure)
            comparison_sentences = [
                (90, "واش يقولوا الناس؟"),
                (35, "فلان واش دارت؟"),
                (-35, "ولد خالك نجح"),
                (-110, "وعلاه مكش كيما فلان؟"),
                (178, "علاه مكش كيما فلان"),
            ]
            for angle, sentence in comparison_sentences:
                bubble = create_speech_bubble(sentence, RED, scale=0.86, width=2.0)
                bubble.move_to(np.array([math.cos(angle * DEGREES) * 2.45, math.sin(angle * DEGREES) * 2.45 + 0.1, 0]))
                bubbles.add(bubble)
            anchor.add(rings, center, bubbles)

        caption = make_caption("قصص مختلفة... ونفس الإشارة", y=-4.55, color=WHITE, accent=color)
        return VGroup(header, anchor, caption)

    def animate_montage_moment(self, kind: str, group: VGroup) -> None:
        content = group[1]
        if kind == "diploma":
            clock = content[-1]
            self.play(Rotate(clock[2], angle=-TAU * 0.95, about_point=clock.get_center()), run_time=0.85, rate_func=linear)
        elif kind == "bac":
            cards = content[1]
            self.play(LaggedStart(*[Indicate(card, color=RED if i in (0, 3) else CYAN, scale_factor=1.04) for i, card in enumerate(cards)], lag_ratio=0.08), run_time=1.0)
        elif kind == "idea":
            idea = content[0]
            bubbles = content[2]
            self.play(LaggedStart(*[FadeIn(bubble, shift=DOWN * 0.12) for bubble in bubbles], lag_ratio=0.12), idea.animate.set_opacity(0.60), run_time=0.9)
        elif kind == "phone":
            likes = content[1]
            self.play(LaggedStart(*[FadeIn(heart, shift=UP * 0.22, scale=0.80) for heart in likes], lag_ratio=0.035), run_time=0.9)
        elif kind == "pressure":
            rings = content[0]
            self.play(rings.animate.scale(1.06).set_opacity(0.72), run_time=0.45, rate_func=there_and_back)

    def scene_01_social_montage(self) -> None:
        moments = [
            ("diploma", "ديبلوم... واستنى الخدمة", CYAN),
            ("bac", "اختيار حياة في ليلة", RED),
            ("idea", "فكرة تموت قبل ما تبدأ", GOLD),
            ("phone", "المقارنة تسرق الطريق", CYAN),
            ("pressure", "واش يقولوا الناس؟", RED),
        ]

        current = None
        for index, (kind, title, color) in enumerate(moments):
            scene = self.create_montage_scene(kind, title, color)
            if current is None:
                self.play(FadeOut(self.seed_dots, scale=0.82), FadeIn(scene, shift=UP * 0.15), run_time=0.68)
            else:
                self.play(ReplacementTransform(current, scene), run_time=0.66, rate_func=smooth)
            self.pulse_camera(scale=0.985, run_time=0.10)
            self.animate_montage_moment(kind, scene)
            self.wait(0.22)
            current = scene

        node_specs = [
            ("ديبلوم", "diploma", LEFT * 2.55 + UP * 2.15, CYAN),
            ("باك", "bac", RIGHT * 2.35 + UP * 1.75, RED),
            ("فكرة", "idea", LEFT * 2.45 + DOWN * 1.15, GOLD),
            ("هاتف", "phone", RIGHT * 2.45 + DOWN * 1.10, CYAN),
            ("الناس", "pressure", UP * 0.15, RED),
        ]
        nodes = VGroup()
        for label, kind, point, color in node_specs:
            node = create_social_node(label, kind, color)
            node.move_to(point)
            nodes.add(node)

        self.play(ReplacementTransform(current, nodes), run_time=0.85, rate_func=smooth)
        self.social_nodes = nodes
        self.wait(0.25)

    def scene_02_pattern_network(self) -> None:
        title = safe_title("تشوفهم قصص مختلفة؟", y=5.55, size=40, color=WHITE)
        focus = safe_title("ركز مليح...", y=5.55, size=42, color=GOLD)
        self.play(FadeIn(title, shift=UP * 0.12), run_time=0.40)
        self.wait(0.35)
        self.play(ReplacementTransform(title, focus), run_time=0.45)

        pairs = [(0, 4), (1, 4), (2, 4), (3, 4), (0, 1), (2, 3), (1, 3)]
        lines = VGroup()
        pulses = VGroup()
        for start, end in pairs:
            group = pulse_line_between(self.social_nodes[start][0].get_center(), self.social_nodes[end][0].get_center(), color=CYAN, width=2.1)
            lines.add(group[0])
            pulses.add(group[1])

        self.play(LaggedStart(*[Create(line) for line in lines], lag_ratio=0.08), run_time=1.05)
        for line, pulse in zip(lines[:5], pulses[:5]):
            pulse.move_to(line.get_start())
            self.play(FadeIn(pulse), MoveAlongPath(pulse, line), run_time=0.22, rate_func=smooth)

        labels = VGroup()
        label_specs = [
            ("نفس الخوف", 0, RED),
            ("نفس الضغط", 1, RED),
            ("نفس المقارنة", 3, GOLD),
            ("نفس الهروب", 2, MUTED),
            ("واش يقولوا الناس؟", 4, GOLD),
        ]
        offsets = [LEFT * 1.0 + UP * 0.45, RIGHT * 0.85 + UP * 0.52, RIGHT * 0.92 + DOWN * 0.36, LEFT * 1.0 + DOWN * 0.36, DOWN * 1.16]
        for (text, node_index, color), offset in zip(label_specs, offsets):
            label = make_pill(text, color=color, size=22, width=2.32 if len(text) < 13 else 2.75)
            label.move_to(self.social_nodes[node_index].get_center() + offset)
            labels.add(label)
            self.play(FadeIn(label, shift=UP * 0.08), run_time=0.22)

        network = VGroup(lines, pulses, labels, self.social_nodes, focus)
        self.play(Rotate(VGroup(lines, self.social_nodes), angle=4 * DEGREES, about_point=ORIGIN), run_time=0.9, rate_func=smooth)
        self.network_group = network
        self.wait(0.45)

    def scene_03_invisible_script(self) -> None:
        self.clear_scene(run_time=0.48)
        title = safe_title("المشكل ماشي دايماً في القرار", y=5.55, size=38, color=WHITE)
        token = VGroup(
            RegularPolygon(n=6, radius=0.94, stroke_color=GOLD, stroke_width=2.6, fill_color=GOLD, fill_opacity=0.08),
            make_arabic_text("قرار", size=35, color=GOLD, weight="BOLD", max_width=1.35),
        )
        token[1].move_to(token[0])
        token.move_to(DOWN * 0.45)

        pressure_labels = [
            ("ضغط العائلة", LEFT * 3.05 + UP * 4.2),
            ("حكم المجتمع", LEFT * 1.55 + UP * 4.75),
            ("عين المقارنة", ORIGIN + UP * 4.95),
            ("ص_وت ال_خوف", RIGHT * 1.55 + UP * 4.75),
            ("ق_وة الع_ادة", RIGHT * 3.05 + UP * 4.2),
            ("طريق الاستسلام", RIGHT * 2.7 + UP * 3.1),
        ]
        labels = VGroup()
        strings = VGroup()
        for text, point in pressure_labels:
            label = make_pill(text, color=RED if text in ("ص_وت ال_خوف", "طريق الاستسلام") else CYAN, size=18, width=2.10)
            label.move_to(point)
            labels.add(label)
            string = Line(label.get_bottom(), token[0].point_from_proportion(0.15 + 0.12 * len(strings)), stroke_color=MUTED, stroke_width=1.8, stroke_opacity=0.62)
            strings.add(string)

        self.play(FadeIn(title, shift=UP * 0.10), FadeIn(token, scale=0.72), run_time=0.62)
        self.play(LaggedStart(*[FadeIn(label, shift=DOWN * 0.08) for label in labels], lag_ratio=0.08), run_time=0.78)
        self.play(LaggedStart(*[Create(string) for string in strings], lag_ratio=0.06), run_time=0.8)
        self.play(token.animate.shift(LEFT * 0.18 + UP * 0.06), strings.animate.set_stroke(color=RED, opacity=0.70), run_time=0.35, rate_func=there_and_back)

        second = safe_title("مرات في السكريبت اللي يسبق القرار", y=-3.85, size=33, color=WHITE)
        commands = VGroup(
            make_pill("تسويف", RED, size=25, width=1.25),
            make_pill("ال_خوف", RED, size=25, width=1.10),
            make_pill("مات_بداش", RED, size=23, width=1.65),
            make_pill("دير كيما الناس", RED, size=21, width=2.15),
            make_pill("ما تخاطرش", RED, size=21, width=1.75),
        )
        positions = [LEFT * 2.55 + DOWN * 1.85, LEFT * 0.75 + DOWN * 2.35, RIGHT * 1.05 + DOWN * 1.82, RIGHT * 2.55 + DOWN * 2.65, ORIGIN + DOWN * 3.05]
        for command, point in zip(commands, positions):
            command.rotate(self.rng.uniform(-7, 7) * DEGREES)
            command.move_to(point)

        self.play(FadeIn(second, shift=UP * 0.12), run_time=0.46)
        for command in commands:
            self.play(FadeIn(command, scale=1.20), run_time=0.18)
            self.play(Indicate(command, color=RED, scale_factor=1.03), run_time=0.15)
        self.script_group = VGroup(title, second, token, labels, strings, commands)
        self.wait(0.55)

    def make_concept_pin(self, text: str, point: np.ndarray, color: str = CYAN) -> VGroup:
        dot = Dot(point, radius=0.065, color=color)
        halo = Circle(radius=0.16, stroke_opacity=0, fill_color=color, fill_opacity=0.13).move_to(dot)
        label = make_arabic_text(text, size=19, color=WHITE, weight="BOLD", max_width=1.52)
        label.next_to(dot, DOWN, buff=0.10)
        return VGroup(halo, dot, label)

    def scene_04_detective_board(self) -> None:
        self.clear_scene(run_time=0.48)
        title = safe_title("الخريطة الخفية", y=5.75, size=41, color=WHITE)
        subtitle = make_arabic_text("علاش نعاودو نفس الغلطة... ونسميوها ظروف؟", size=29, color=MUTED, max_width=7.0)
        subtitle.next_to(title, DOWN, buff=0.18)

        board = RoundedRectangle(
            width=8.05,
            height=10.7,
            corner_radius=0.22,
            stroke_color=CYAN,
            stroke_width=1.4,
            stroke_opacity=0.32,
            fill_color=CARD,
            fill_opacity=0.50,
        )
        board.move_to(DOWN * 0.55)

        concept_positions = {
            "ديبلو م": LEFT * 3.00 + UP * 3.30,
            "الخدمة": LEFT * 0.80 + UP * 3.65,
            "الباك": RIGHT * 1.15 + UP * 3.25,
            "التخصص": RIGHT * 3.05 + UP * 2.55,
            "المشروع": LEFT * 2.65 + UP * 1.25,
            "الخـوف": LEFT * 0.55 + UP * 0.95,
            "سوشيال ميديا": RIGHT * 2.55 + UP * 0.65,
            "المقارنات": RIGHT * 1.05 + DOWN * 0.45,
            "الإحباط": RIGHT * 3.05 + DOWN * 1.42,
            "العا ئلة": LEFT * 2.85 + DOWN * 0.80,
            "الزواج": LEFT * 1.05 + DOWN * 2.20,
            "الضغط": RIGHT * 0.75 + DOWN * 2.35,
            "الهروب": RIGHT * 2.72 + DOWN * 3.02,
            "نفس الغلطة": LEFT * 2.85 + DOWN * 3.20,
            "واش يقولوا الناس؟": ORIGIN + DOWN * 0.55,
        }
        nodes: dict[str, VGroup] = {}
        node_group = VGroup()
        for key, point in concept_positions.items():
            color = GOLD if key in ("واش يقولوا الناس؟", "نفس الغلطة") else RED if key in ("الخوف", "الضغط", "الهروب") else CYAN
            pin = self.make_concept_pin(key, point, color=color)
            nodes[key] = pin
            node_group.add(pin)

        self.play(FadeIn(title, shift=UP * 0.12), FadeIn(subtitle, shift=UP * 0.08), Create(board), run_time=0.72)
        self.play(LaggedStart(*[FadeIn(node, scale=0.78) for node in node_group], lag_ratio=0.035), run_time=1.15)

        edge_specs = [
            ("ديبلو م", "الخدمة", CYAN),
            ("الباك", "التخصص", CYAN),
            ("التخصص", "العا ئلة", MUTED),
            ("المشروع", "الخـوف", RED),
            ("سوشيال ميديا", "المقارنات", CYAN),
            ("المقارنات", "الإحباط", RED),
            ("العا ئلة", "واش يقولوا الناس؟", GOLD),
            ("الزواج", "الضغط", RED),
            ("الضغط", "الهروب", RED),
            ("الهروب", "نفس الغلطة", GOLD),
        ]
        connections = VGroup()
        for start, end, color in edge_specs:
            connection = connect_concepts(nodes[start][1], nodes[end][1], color=color)
            connections.add(connection)

        for connection in connections:
            line, pulse = connection[0], connection[1]
            pulse.move_to(line.get_start())
            self.play(Create(line), FadeIn(pulse), MoveAlongPath(pulse, line), run_time=0.24, rate_func=smooth)
            self.play(pulse.animate.set_opacity(0.0), run_time=0.05)

        lens = create_magnifier(scale=1.28)
        lens.move_to(LEFT * 3.0 + UP * 2.8)
        sweep = Rectangle(width=1.3, height=10.4, stroke_opacity=0, fill_color=CYAN, fill_opacity=0.035)
        sweep.move_to(lens)
        self.play(FadeIn(lens, scale=0.86), FadeIn(sweep), run_time=0.25)
        self.play(lens.animate.move_to(RIGHT * 3.0 + DOWN * 2.6), sweep.animate.move_to(RIGHT * 3.0 + DOWN * 2.6), run_time=1.35, rate_func=smooth)
        self.play(FadeOut(lens), FadeOut(sweep), run_time=0.22)

        self.detective_group = VGroup(board, title, subtitle, node_group, connections)
        self.wait(0.45)

    def scene_05_maze(self) -> None:
        self.clear_scene(run_time=0.50)
        title = safe_title("كي نفس السلوك يرجع...", y=5.65, size=39, color=WHITE)
        outline = make_arabic_text("نمط", size=92, color=GOLD, weight="BOLD", max_width=3.0)
        outline.set_opacity(0.09)
        outline.move_to(UP * 3.55)

        walls = VGroup()
        wall_segments = [
            ((-3.2, 2.2), (2.6, 2.2)),
            ((-3.2, 2.2), (-3.2, -2.9)),
            ((2.6, 2.2), (2.6, -2.7)),
            ((-3.2, -2.9), (2.6, -2.9)),
            ((-2.2, 1.25), (1.6, 1.25)),
            ((-2.2, 1.25), (-2.2, -1.65)),
            ((-1.15, 0.35), (2.0, 0.35)),
            ((1.05, 1.25), (1.05, -1.65)),
            ((-0.2, -0.62), (2.05, -0.62)),
            ((-2.2, -1.65), (0.70, -1.65)),
            ((-3.2, 0.10), (-2.2, 0.10)),
            ((1.65, -0.62), (1.65, -2.05)),
        ]
        for start, end in wall_segments:
            line = Line(np.array([start[0], start[1], 0]), np.array([end[0], end[1], 0]), stroke_color=CYAN, stroke_width=3.0, stroke_opacity=0.68)
            walls.add(line)

        dead_words = VGroup()
        for text, point in [
            ("اك تستنى", LEFT * 2.65 + UP * 1.62),
            ("اك تقارن", RIGHT * 2.05 + UP * 1.45),
            ("اك تخاف", LEFT * 1.65 + DOWN * 1.1),
            ("اك تلوم", RIGHT * 2.18 + DOWN * 1.42),
            ("اك تقلد", LEFT * 2.35 + DOWN * 2.35),
        ]:
            word = make_pill(text, color=RED if text in ("اك تخاف", "اك نقلد") else GOLD, size=20, width=1.25)
            word.move_to(point)
            word.set_opacity(0)
            dead_words.add(word)

        route_points = [
            LEFT * 2.85 + UP * 1.85,
            LEFT * 2.45 + UP * 1.85,
            LEFT * 2.45 + UP * 0.55,
            LEFT * 1.05 + UP * 0.55,
            LEFT * 1.05 + DOWN * 1.18,
            RIGHT * 0.48 + DOWN * 1.18,
            RIGHT * 0.48 + UP * 0.05,
            RIGHT * 1.95 + UP * 0.05,
            RIGHT * 1.95 + DOWN * 1.52,
        ]
        route = VMobject()
        route.set_points_as_corners(route_points)
        route.set_stroke(GOLD, width=2.2, opacity=0.25)
        token = create_glow_dot(route_points[0], color=GOLD, radius=0.055)

        self.play(FadeIn(title, shift=UP * 0.12), FadeIn(outline, scale=0.94), run_time=0.55)
        self.play(LaggedStart(*[Create(wall) for wall in walls], lag_ratio=0.035), run_time=0.95)
        self.play(FadeIn(token, scale=0.75), Create(route), run_time=0.45)
        self.play(MoveAlongPath(token, route), run_time=2.0, rate_func=smooth)
        for word in dead_words:
            self.play(word.animate.set_opacity(1.0), run_time=0.16)

        caption = safe_title("كاين كلمة ناقصة", y=-4.62, size=35, color=GOLD)
        self.play(FadeIn(caption, shift=UP * 0.12), outline.animate.set_opacity(0.18), run_time=0.52)
        self.maze_group = VGroup(title, outline, walls, route, token, dead_words, caption)
        self.wait(0.55)

    def scene_06_missing_letters(self) -> None:
        self.clear_scene(run_time=0.45)
        caption = safe_title("كاين كلمة ناقصة...", y=4.45, size=39, color=WHITE)
        letters = VGroup(
            make_arabic_text("ن", size=118, color=GOLD, weight="BOLD", max_width=1.6),
            make_arabic_text("م", size=118, color=GOLD, weight="BOLD", max_width=1.6),
            make_arabic_text("ط", size=118, color=GOLD, weight="BOLD", max_width=1.6),
        )
        targets = [LEFT * 2.25 + UP * 0.85, RIGHT * 1.25 + UP * 1.45, DOWN * 1.10]
        rotations = [-10 * DEGREES, 8 * DEGREES, -5 * DEGREES]
        for letter, point, rotation in zip(letters, targets, rotations):
            letter.move_to(point)
            letter.rotate(rotation)

        orbit = VGroup()
        for index in range(18):
            angle = index * TAU / 18
            dot = Dot(np.array([math.cos(angle) * 2.65, math.sin(angle) * 1.55, 0]), radius=0.018, color=CYAN if index % 3 else GOLD)
            dot.set_opacity(0.44)
            orbit.add(dot)

        self.play(FadeIn(caption, shift=UP * 0.12), run_time=0.38)
        self.play(LaggedStart(*[FadeIn(letter, scale=0.76) for letter in letters], lag_ratio=0.18), FadeIn(orbit), run_time=1.1)
        self.play(Rotate(orbit, angle=14 * DEGREES, about_point=ORIGIN), letters.animate.set_opacity(0.94), run_time=1.05, rate_func=smooth)
        self.missing_letters = letters
        self.orbit = orbit
        self.missing_caption = caption
        self.wait(0.5)

    def scene_07_namat_reveal(self) -> None:
        word = make_arabic_text("نمط", size=128, color=GOLD, weight="BOLD", max_width=3.0)
        word.move_to(UP * 0.74)
        latin = make_english_text("NAMAT", size=42, color=WHITE, weight="BOLD", max_width=3.4)
        latin.next_to(word, DOWN, buff=0.14)
        explanation = make_arabic_text("النمط هو الشي اللي يتعاود فينا...\nحتى نوليو نحسبوه طبيعة.", size=29, color=WHITE, max_width=7.0)
        explanation.move_to(DOWN * 2.35)
        ripple = VGroup()
        for radius, opacity in ((0.75, 0.22), (1.32, 0.12), (2.05, 0.07)):
            circle = Circle(radius=radius, stroke_color=GOLD, stroke_width=2.0, stroke_opacity=opacity)
            circle.move_to(word)
            ripple.add(circle)

        constellation = VGroup()
        for index in range(28):
            angle = index * TAU / 28
            rad = 2.2 + 0.42 * math.sin(index)
            point = np.array([math.cos(angle) * rad, math.sin(angle) * rad * 0.92 + 0.45, 0])
            dot = Dot(point, radius=0.015 if index % 4 else 0.027, color=CYAN if index % 5 else GOLD)
            dot.set_opacity(0.25 if index % 4 else 0.48)
            constellation.add(dot)
        constellation_lines = VGroup()
        for index in range(0, len(constellation) - 2, 3):
            line = Line(constellation[index].get_center(), constellation[index + 2].get_center(), stroke_color=MUTED, stroke_width=0.8, stroke_opacity=0.16)
            constellation_lines.add(line)

        self.camera.frame.save_state()
        self.play(
            FadeOut(self.missing_caption, shift=UP * 0.10),
            FadeIn(constellation_lines),
            FadeIn(constellation),
            TransformMatchingShapes(self.missing_letters, word),
            FadeOut(self.orbit, scale=1.06),
            self.camera.frame.animate.scale(0.92),
            run_time=0.85,
            rate_func=smooth,
        )
        self.play(FadeIn(ripple, scale=0.72), FadeIn(latin, shift=UP * 0.10), run_time=0.52)
        self.play(Restore(self.camera.frame), FadeIn(explanation, shift=UP * 0.14), run_time=0.75)
        self.namat_word = word
        self.reveal_group = VGroup(constellation_lines, constellation, ripple, word, latin, explanation)
        self.wait(0.75)

    def scene_08_project_meaning(self) -> None:
        self.clear_scene(run_time=0.55)
        header = make_arabic_text("نمط", size=72, color=GOLD, weight="BOLD", max_width=2.0)
        header.move_to(UP * 5.55)
        subtitle = make_arabic_text("ما جاش باش يحكم عليك", size=30, color=WHITE, max_width=6.8)
        subtitle.next_to(header, DOWN, buff=0.12)

        planes = VGroup()
        plane_specs = [
            ("من أمامك", "المجتمع", UP * 1.45, CYAN),
            ("في داخلك", "خوف وأفكار", ORIGIN + DOWN * 0.15, GOLD),
            ("من حولك", "عائلة وإعلام وضغط", DOWN * 1.75, GREEN),
        ]
        for short, long, point, color in plane_specs:
            plane = RoundedRectangle(
                width=6.9,
                height=1.12,
                corner_radius=0.16,
                stroke_color=color,
                stroke_width=2.0,
                fill_color=color,
                fill_opacity=0.075,
            )
            plane.move_to(point)
            short_text = make_arabic_text(f"\u200f{short}\u200f", size=30, color=color, weight="BOLD", max_width=1.55)
            short_text.move_to(plane.get_right() + LEFT * 1.20)
            long_text = make_arabic_text(f"\u200f{long}\u200f", size=24, color=WHITE, max_width=3.95)
            long_text.move_to(plane.get_left() + RIGHT * 2.60)
            planes.add(VGroup(plane, short_text, long_text))

        lens = create_magnifier(scale=1.0)
        lens.move_to(LEFT * 3.15 + UP * 1.45)
        words = VGroup(
            make_pill("ماشي حكم", RED, size=27, width=1.95),
            make_pill("فهـم", CYAN, size=31, width=1.25),
            make_pill("وعـي", GOLD, size=31, width=1.25),
        )
        words.arrange(RIGHT, buff=0.36)
        words.move_to(DOWN * 4.25)
        cross = Line(LEFT * 0.62, RIGHT * 0.62, stroke_color=RED, stroke_width=4)
        cross.rotate(-12 * DEGREES)
        cross.move_to(words[0])

        self.play(FadeIn(header, shift=UP * 0.12), FadeIn(subtitle, shift=UP * 0.08), run_time=0.52)
        self.play(LaggedStart(*[FadeIn(plane, shift=UP * 0.14) for plane in planes], lag_ratio=0.12), run_time=1.0)
        self.play(FadeIn(lens, scale=0.82), run_time=0.22)
        self.play(lens.animate.move_to(RIGHT * 3.0 + DOWN * 1.75), run_time=1.05, rate_func=smooth)
        self.play(FadeOut(lens), run_time=0.16)
        self.play(FadeIn(words[0], shift=UP * 0.12), run_time=0.22)
        self.play(Create(cross), run_time=0.25)
        self.play(FadeIn(words[1], shift=UP * 0.12), FadeIn(words[2], shift=UP * 0.12), run_time=0.42)
        self.play(Indicate(words[2], color=GOLD, scale_factor=1.08), run_time=0.55)
        self.meaning_words = words
        self.meaning_group = VGroup(header, subtitle, planes, words, cross)
        self.wait(0.65)

    def scene_09_moral_depth(self) -> None:
        self.clear_scene(run_time=0.48)
        title = safe_title("الوعي ماشي ضد الدين", y=5.55, size=39, color=WHITE)
        compass = create_compass(scale=1.42)
        compass.move_to(UP * 0.35)
        glow = Circle(radius=2.1, stroke_opacity=0, fill_color=GOLD, fill_opacity=0.055)
        glow.move_to(compass)
        awareness = make_pill("بصيرة", GOLD, size=27, width=1.62)
        awareness.move_to(compass.get_top() + UP * 0.78)

        brain = create_brain_icon(scale=1.25)
        brain.move_to(LEFT * 2.7 + DOWN * 0.25)
        brain_label = make_pill("تفكير", CYAN, size=23, width=1.45)
        brain_label.next_to(brain, DOWN, buff=0.22)
        heart = create_heart_icon(scale=1.28)
        heart.move_to(RIGHT * 2.65 + DOWN * 0.22)
        heart_label = make_pill("رحمة", RED, size=23, width=1.35)
        heart_label.next_to(heart, DOWN, buff=0.22)

        values = make_pill("مبادئ", GOLD, size=23, width=1.45)
        values.move_to(UP * 3.15)
        ray = Line(values.get_bottom() + DOWN * 0.05, compass.get_top() + DOWN * 0.10, stroke_color=GOLD, stroke_width=3, stroke_opacity=0.68)
        sentence = make_arabic_text("ربي عطانا تفكير باش نتدبرو، ورحمة باش نرحمو،\nومبادئ باش ما نضيعوش وسط الزحام.", size=27, color=WHITE, max_width=7.3)
        sentence.move_to(DOWN * 4.45)

        self.play(FadeIn(title, shift=UP * 0.12), FadeIn(glow, scale=0.75), FadeIn(compass, scale=0.84), run_time=0.75)
        self.play(FadeIn(values, shift=DOWN * 0.10), Create(ray), FadeIn(awareness, shift=DOWN * 0.10), run_time=0.55)
        self.play(FadeIn(brain, shift=RIGHT * 0.12), FadeIn(brain_label), FadeIn(heart, shift=LEFT * 0.12), FadeIn(heart_label), run_time=0.65)
        self.play(Rotate(compass[2], angle=18 * DEGREES, about_point=compass.get_center()), glow.animate.set_fill(opacity=0.095), run_time=0.72, rate_func=there_and_back)
        self.play(FadeIn(sentence, shift=UP * 0.12), run_time=0.55)
        self.moral_group = VGroup(title, glow, compass, awareness, brain, brain_label, heart, heart_label, values, ray, sentence)
        self.wait(0.8)

    def scene_10_profiles_reveal(self) -> None:
        self.clear_scene(run_time=0.50)
        title = safe_title("من هنا يبدأ نمط", y=5.65, size=39, color=WHITE)
        cards = Group(
            make_phone_card("Facebook", PROFILE_DIR / "facebook_profile.png", scale=0.92),
            make_phone_card("Instagram", PROFILE_DIR / "instagram_profile.png", scale=1.04),
            make_phone_card("TikTok", PROFILE_DIR / "tiktok_profile.png", scale=0.92),
        )
        cards[0].move_to(LEFT * 2.72 + DOWN * 0.05)
        cards[1].move_to(UP * 0.12)
        cards[2].move_to(RIGHT * 2.72 + DOWN * 0.05)

        path_center = Line(UP * 3.85, cards[1][0].get_top() + UP * 0.12, stroke_color=GOLD, stroke_width=2.5, stroke_opacity=0.78)
        path_left = Line(cards[1][0].get_left() + LEFT * 0.08, cards[0][0].get_right() + RIGHT * 0.08, stroke_color=CYAN, stroke_width=2.0, stroke_opacity=0.56)
        path_right = Line(cards[1][0].get_right() + RIGHT * 0.08, cards[2][0].get_left() + LEFT * 0.08, stroke_color=CYAN, stroke_width=2.0, stroke_opacity=0.56)
        caption = safe_title("وين ما كنت... شوف النمط.", y=-4.85, size=32, color=GOLD)

        self.play(FadeIn(title, shift=UP * 0.12), run_time=0.42)
        self.play(
            Create(path_center),
            DrawBorderThenFill(cards[1][0]),
            FadeIn(Group(*cards[1][1:]), shift=UP * 0.18),
            run_time=0.78,
        )
        self.play(Create(path_left), Create(path_right), run_time=0.42)
        self.play(
            DrawBorderThenFill(cards[0][0]),
            FadeIn(Group(*cards[0][1:]), shift=UP * 0.16),
            DrawBorderThenFill(cards[2][0]),
            FadeIn(Group(*cards[2][1:]), shift=UP * 0.16),
            run_time=0.85,
        )
        halos = VGroup()
        for card in cards:
            halo = SurroundingRectangle(card[0], color=CYAN, buff=0.12)
            halo.set_stroke(width=2.0, opacity=0.0)
            halos.add(halo)
        self.add(halos)
        self.play(halos.animate.set_stroke(opacity=0.65), run_time=0.22)
        self.play(halos.animate.set_stroke(opacity=0.0), run_time=0.45)
        self.play(FadeIn(caption, shift=UP * 0.10), run_time=0.38)
        self.profiles_group = Group(title, cards, path_center, path_left, path_right, caption, halos)
        self.wait(0.85)

    def scene_11_existing_outro(self) -> None:
        play_namat_closing(self, clear_existing=True, seed=24)


# Render:
# manim -pqh projects/namat_intro_hidden_pattern_vertical.py NamatIntroVideo
