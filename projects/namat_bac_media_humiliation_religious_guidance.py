# -*- coding: utf-8 -*-
"""Namat BAC media humiliation awareness video.

Render from the project root:
    manim -ql projects/namat_bac_media_humiliation_religious_guidance.py BacMediaHumiliationReligiousGuidance
    manim -qh projects/namat_bac_media_humiliation_religious_guidance.py BacMediaHumiliationReligiousGuidance
"""

from __future__ import annotations

import math
import random
import sys
from pathlib import Path

import numpy as np
from manim import *

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common import create_check_icon, create_student_icon, fit_to_frame, make_ar_text, make_latin_text


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30


BG = "#07162E"
WHITE = "#F7F9FF"
SOFT_WHITE = "#DCE6FF"
BLUE = "#1E4FFF"
CYAN = "#35D4FF"
GOLD = "#F2B84B"
RED = "#FF4D5B"
GREEN = "#39D98A"
DARK_CARD = "#101D3A"
GRAY = "#8EA0C2"
BLACK = "#050A16"

ASSETS_DIR = ROOT / "projects" / "assets"
COMMENTS_DIR = ASSETS_DIR / "comments"


def full_screen_background() -> VGroup:
    """Create the calm dark Namat background used across the whole piece."""

    base = Rectangle(
        width=config.frame_width + 0.4,
        height=config.frame_height + 0.4,
        fill_color=BG,
        fill_opacity=1,
        stroke_opacity=0,
    )

    grid = VGroup()
    for x in np.linspace(-4.0, 4.0, 9):
        line = Line([x, -8.2, 0], [x, 8.2, 0])
        line.set_stroke(SOFT_WHITE, width=0.55, opacity=0.045)
        grid.add(line)
    for y in np.linspace(-7.0, 7.0, 8):
        line = Line([-4.7, y, 0], [4.7, y, 0])
        line.set_stroke(SOFT_WHITE, width=0.55, opacity=0.04)
        grid.add(line)

    depth = VGroup()
    for center, radius, color, opacity in (
        (UP * 4.5 + LEFT * 2.6, 3.2, CYAN, 0.045),
        (DOWN * 4.2 + RIGHT * 2.5, 3.0, GOLD, 0.026),
        (ORIGIN, 4.9, BLUE, 0.035),
    ):
        glow = Circle(radius=radius, stroke_opacity=0, fill_color=color, fill_opacity=opacity)
        glow.move_to(center)
        depth.add(glow)

    return VGroup(base, depth, grid).set_z_index(-100)


def title_text(content: str, font_size: float = 48, color: str = WHITE, max_width: float = 7.8) -> Text:
    return make_ar_text(content, font_size=font_size, color=color, weight="BOLD", max_width=max_width)


def subtitle_text(content: str, font_size: float = 30, color: str = SOFT_WHITE, max_width: float = 7.4) -> Text:
    return make_ar_text(content, font_size=font_size, color=color, max_width=max_width)


def create_camera_icon(scale: float = 1.0, color: str = SOFT_WHITE) -> VGroup:
    body = RoundedRectangle(
        width=0.42 * scale,
        height=0.25 * scale,
        corner_radius=0.04 * scale,
        stroke_color=color,
        stroke_width=2.0 * scale,
        fill_color=color,
        fill_opacity=0.10,
    )
    lens = Circle(radius=0.065 * scale, stroke_color=color, stroke_width=1.8 * scale)
    lens.move_to(body.get_center() + RIGHT * 0.04 * scale)
    top = Polygon(
        body.get_left() + UP * 0.04 * scale,
        body.get_left() + LEFT * 0.14 * scale + UP * 0.13 * scale,
        body.get_left() + LEFT * 0.14 * scale + DOWN * 0.13 * scale,
        body.get_left() + DOWN * 0.04 * scale,
        stroke_color=color,
        stroke_width=1.5 * scale,
        fill_color=color,
        fill_opacity=0.08,
    )
    return VGroup(top, body, lens)


def create_microphone_icon(scale: float = 1.0, color: str = SOFT_WHITE) -> VGroup:
    head = RoundedRectangle(
        width=0.18 * scale,
        height=0.34 * scale,
        corner_radius=0.08 * scale,
        stroke_color=color,
        stroke_width=2.0 * scale,
        fill_color=color,
        fill_opacity=0.12,
    )
    stem = Line(DOWN * 0.16 * scale, DOWN * 0.42 * scale, stroke_color=color, stroke_width=2.0 * scale)
    base = Line(LEFT * 0.13 * scale, RIGHT * 0.13 * scale, stroke_color=color, stroke_width=2.0 * scale)
    base.move_to(stem.get_end())
    return VGroup(head, stem, base)


def create_phone_icon(scale: float = 1.0, color: str = SOFT_WHITE, fill: str = DARK_CARD) -> VGroup:
    phone = RoundedRectangle(
        width=0.62 * scale,
        height=1.05 * scale,
        corner_radius=0.10 * scale,
        stroke_color=color,
        stroke_width=2.2 * scale,
        fill_color=fill,
        fill_opacity=0.78,
    )
    notch = Line(LEFT * 0.10 * scale, RIGHT * 0.10 * scale, stroke_color=color, stroke_width=1.5 * scale)
    notch.move_to(phone.get_top() + DOWN * 0.12 * scale)
    dot = Dot(phone.get_bottom() + UP * 0.10 * scale, radius=0.025 * scale, color=color)
    return VGroup(phone, notch, dot)


def create_video_slot(label: str, slot_id: str = "VIDEO_SLOT", scale: float = 1.0) -> VGroup:
    """Create an anonymized vertical reel placeholder for later editor replacement."""

    width = 2.35 * scale
    height = 4.85 * scale
    outer = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.23 * scale,
        stroke_color=CYAN,
        stroke_width=2.4 * scale,
        fill_color=BLACK,
        fill_opacity=0.92,
    )
    inner = RoundedRectangle(
        width=width - 0.18 * scale,
        height=height - 0.22 * scale,
        corner_radius=0.18 * scale,
        stroke_color=SOFT_WHITE,
        stroke_width=0.8 * scale,
        stroke_opacity=0.16,
        fill_color=DARK_CARD,
        fill_opacity=0.96,
    )
    inner.move_to(outer)

    # Blur is simulated with transparent bands and generic silhouettes; no identity is shown.
    blur_shapes = VGroup()
    for index, (offset, color, opacity) in enumerate(
        (
            (UP * 1.18 + LEFT * 0.18, CYAN, 0.10),
            (DOWN * 0.05 + RIGHT * 0.18, SOFT_WHITE, 0.08),
            (DOWN * 1.45 + LEFT * 0.15, GOLD, 0.06),
        )
    ):
        ellipse = Ellipse(
            width=(1.65 - index * 0.18) * scale,
            height=(0.72 + index * 0.16) * scale,
            stroke_opacity=0,
            fill_color=color,
            fill_opacity=opacity,
        )
        ellipse.move_to(outer.get_center() + offset * scale)
        blur_shapes.add(ellipse)

    center_door = RoundedRectangle(
        width=1.28 * scale,
        height=1.55 * scale,
        corner_radius=0.05 * scale,
        stroke_color=GRAY,
        stroke_width=1.2 * scale,
        stroke_opacity=0.44,
        fill_color=BG,
        fill_opacity=0.34,
    )
    center_door.move_to(outer.get_center() + UP * 0.52 * scale)
    door_label = make_ar_text("باب المركز", font_size=13 * scale, color=GRAY, max_width=1.0 * scale)
    door_label.move_to(center_door.get_top() + DOWN * 0.18 * scale)

    student = create_student_icon(color=SOFT_WHITE, accent=GRAY, scale_factor=0.40 * scale, stroke_width=3.2 * scale)
    student.move_to(outer.get_center() + DOWN * 0.58 * scale)
    student.set_opacity(0.42)

    mic = create_microphone_icon(scale=0.82 * scale, color=SOFT_WHITE)
    mic.rotate(-14 * DEGREES)
    mic.move_to(outer.get_right() + LEFT * 0.42 * scale + DOWN * 0.06 * scale)
    camera = create_camera_icon(scale=0.72 * scale, color=SOFT_WHITE)
    camera.move_to(outer.get_left() + RIGHT * 0.48 * scale + DOWN * 1.55 * scale)

    rec_dot = Dot(radius=0.045 * scale, color=RED)
    rec_dot.move_to(outer.get_top() + DOWN * 0.30 * scale + LEFT * 0.82 * scale)
    rec = make_latin_text("REC", font_size=13 * scale, color=RED, weight="BOLD")
    rec.next_to(rec_dot, RIGHT, buff=0.05 * scale)
    rec_group = VGroup(rec_dot, rec)

    anonymized = make_ar_text("مموّه", font_size=18 * scale, color=SOFT_WHITE, max_width=1.5 * scale)
    anonymized.move_to(outer.get_center() + UP * 1.85 * scale)
    anonymized.set_opacity(0.76)

    label_text = make_ar_text(label, font_size=18 * scale, color=WHITE, max_width=width + 0.10 * scale)
    label_text.next_to(outer, DOWN, buff=0.16 * scale)
    slot_code = make_latin_text(slot_id, font_size=9 * scale, color=GRAY, weight="BOLD", max_width=width)
    slot_code.move_to(outer.get_bottom() + UP * 0.18 * scale)
    slot_code.set_opacity(0.66)

    slot = VGroup(
        outer,
        inner,
        blur_shapes,
        center_door,
        door_label,
        student,
        mic,
        camera,
        rec_group,
        anonymized,
        slot_code,
        label_text,
    )
    slot.set_z_index(5)
    return slot


def create_fake_comment(text: str, color: str = CYAN, danger: bool = False, width: float = 2.65) -> VGroup:
    label = make_ar_text(text, font_size=22, color=WHITE, weight="BOLD" if danger else "NORMAL", max_width=width - 0.58)
    height = max(0.64, label.height + 0.28)
    card = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.12,
        stroke_color=RED if danger else color,
        stroke_width=2.0,
        fill_color=DARK_CARD,
        fill_opacity=0.94,
    )
    avatar = Circle(
        radius=0.12,
        stroke_color=GRAY,
        stroke_width=1.2,
        fill_color=GRAY,
        fill_opacity=0.22,
    )
    avatar.move_to(card.get_right() + LEFT * 0.28)
    fit_to_frame(label, max_width=width - 0.62, max_height=height - 0.16)
    label.move_to(card.get_center() + LEFT * 0.18)
    label.next_to(avatar, LEFT, buff=0.14)
    return VGroup(card, avatar, label)


def load_comment_images(folder: Path = COMMENTS_DIR) -> list[Mobject]:
    """Load comment PNGs if present; otherwise create neutral fake cards."""

    if folder.exists():
        paths = sorted(folder.glob("*.png"))
        if paths:
            images: list[Mobject] = []
            for path in paths:
                image = ImageMobject(str(path))
                fit_to_frame(image, max_width=2.85, max_height=0.92)
                image.set_opacity(0.95)
                images.append(image)
            return images

    fallback_texts = [
        "شوف اللبسة",
        "جيل اليوم",
        "شوف المستوى",
        "واش هذا؟",
        "اضحك",
        "كارثة",
        "ما فهم والو",
        "زيد شوف التعليقات",
        "عيب تشاركها",
    ]
    return [create_fake_comment(text, color=CYAN if index % 2 else SOFT_WHITE) for index, text in enumerate(fallback_texts)]


def create_concept_word(text: str, color: str = WHITE) -> VGroup:
    label = make_ar_text(text, font_size=34, color=color, weight="BOLD", max_width=2.3)
    pill = RoundedRectangle(
        width=max(1.35, label.width + 0.54),
        height=max(0.62, label.height + 0.22),
        corner_radius=0.14,
        stroke_color=color,
        stroke_width=2.0,
        fill_color=color,
        fill_opacity=0.09,
    )
    label.move_to(pill)
    return VGroup(pill, label)


def create_algorithm_machine() -> tuple[VGroup, VGroup, VGroup, Arrow, Text]:
    machine_box = RoundedRectangle(
        width=3.45,
        height=3.55,
        corner_radius=0.20,
        stroke_color=CYAN,
        stroke_width=2.4,
        fill_color=DARK_CARD,
        fill_opacity=0.92,
    )
    title = make_ar_text("آلة التفاعل", font_size=31, color=WHITE, weight="BOLD")
    title.move_to(machine_box.get_top() + DOWN * 0.50)

    counters = VGroup()
    for offset, label in zip((0.45, 0.05, -0.35, -0.75), ("التعليقات", "المشاركة", "الضحك", "المشاهدات")):
        row = make_ar_text(label, font_size=23, color=SOFT_WHITE, max_width=2.1)
        row.move_to(machine_box.get_center() + DOWN * offset)
        counters.add(row)

    machine = VGroup(machine_box, title, counters)
    inputs = VGroup(
        create_concept_word("التعليق", CYAN),
        create_concept_word("المشاركة", CYAN),
        create_concept_word("الضحك", RED),
        create_concept_word("المشاهدة", GOLD),
    ).arrange(DOWN, buff=0.32)
    inputs.move_to(LEFT * 3.0 + UP * 0.08)

    arrows = VGroup()
    for item in inputs:
        arrow = Arrow(
            item.get_right() + RIGHT * 0.10,
            machine_box.get_left() + LEFT * 0.10 + UP * (item.get_center()[1] * 0.18),
            buff=0.02,
            stroke_width=3,
            color=GRAY,
            max_tip_length_to_length_ratio=0.14,
        )
        arrows.add(arrow)

    output_arrow = Arrow(
        machine_box.get_right() + RIGHT * 0.14,
        machine_box.get_right() + RIGHT * 1.85,
        buff=0.02,
        stroke_width=5,
        color=RED,
        max_tip_length_to_length_ratio=0.18,
    )
    output = make_ar_text("انتشار أكبر", font_size=35, color=RED, weight="BOLD", max_width=2.3)
    output.next_to(output_arrow, RIGHT, buff=0.18)
    return machine, inputs, arrows, output_arrow, output


def create_religious_guidance_cards() -> VGroup:
    cards = VGroup()
    quotes = [
        ("لا يسخر قوم من قوم", "الحجرات: 11"),
        ("ولا يغتب بعضكم بعضا", "الحجرات: 12"),
        ("فليقل خيرًا أو ليصمت", "البخاري ومسلم"),
    ]
    for quote, source in quotes:
        q = make_ar_text(quote, font_size=29, color=WHITE, weight="BOLD", max_width=5.7)
        s = make_ar_text(source, font_size=19, color=GOLD, max_width=4.6)
        texts = VGroup(q, s).arrange(DOWN, buff=0.10)
        card = RoundedRectangle(
            width=6.55,
            height=1.16,
            corner_radius=0.16,
            stroke_color=GOLD,
            stroke_width=2.2,
            fill_color=GOLD,
            fill_opacity=0.07,
        )
        texts.move_to(card)
        cards.add(VGroup(card, texts))
    cards.arrange(DOWN, buff=0.32)
    return cards


def create_action_card(text: str, color: str = GREEN) -> VGroup:
    label = make_ar_text(text, font_size=25, color=WHITE, max_width=5.25)
    box = RoundedRectangle(
        width=6.45,
        height=0.90,
        corner_radius=0.14,
        stroke_color=color,
        stroke_width=2.0,
        fill_color=color,
        fill_opacity=0.10,
    )
    check = create_check_icon(color=color, size=0.19)
    check.move_to(box.get_right() + LEFT * 0.44)
    label.next_to(check, LEFT, buff=0.22)
    return VGroup(box, check, label)


def create_book_icon(scale: float = 1.0) -> VGroup:
    left_page = RoundedRectangle(
        width=0.72 * scale,
        height=0.94 * scale,
        corner_radius=0.06 * scale,
        stroke_color=GOLD,
        stroke_width=2.0 * scale,
        fill_color=GOLD,
        fill_opacity=0.08,
    )
    right_page = left_page.copy()
    left_page.shift(LEFT * 0.35 * scale)
    right_page.shift(RIGHT * 0.35 * scale)
    spine = Line(UP * 0.43 * scale, DOWN * 0.43 * scale, stroke_color=GOLD, stroke_width=2.0 * scale)
    return VGroup(left_page, right_page, spine)


def create_loop_diagram() -> tuple[VGroup, VGroup]:
    labels = ["لقطة مختارة", "سخرية", "تعليقات", "المشاركات", "ثم الربح"]
    radius = 2.35
    nodes = VGroup()
    arrows = VGroup()
    points = []
    for index, label in enumerate(labels):
        angle = PI / 2 - index * TAU / len(labels)
        point = np.array([radius * math.cos(angle), radius * math.sin(angle), 0.0]) + UP * 0.25
        points.append(point)
        node = create_concept_word(label, RED if label in ("سخرية", "ثم الربح") else CYAN)
        node.scale(0.72)
        node.move_to(point)
        nodes.add(node)
    for start, end in zip(points, points[1:] + points[:1]):
        arrow = CurvedArrow(
            start + (end - start) * 0.23,
            end - (end - start) * 0.23,
            angle=-TAU / 7,
            color=GRAY,
            stroke_width=2.3,
        )
        arrows.add(arrow)
    return nodes, arrows


class BacMediaHumiliationReligiousGuidance(Scene):
    """Vertical social-awareness animation with anonymized placeholders only."""

    def construct(self) -> None:
        self.rng = random.Random(17)
        self.setup_scene()
        self.scene_0_cold_open()
        self.scene_1_pattern_reveal()
        self.scene_2_selected_clip()
        self.scene_3_comment_avalanche()
        self.scene_4_human_hidden()
        self.scene_5_comments_to_concepts()
        self.scene_6_who_wins()
        self.scene_7_algorithm()
        self.scene_8_audience_mirror()
        self.scene_9_religious_bridge()
        self.scene_10_guidance_cards()
        self.scene_11_practical_actions()
        self.scene_12_break_the_loop()
        self.scene_13_media_nuance()
        self.scene_14_restore_humanity()
        self.scene_15_final_punchline()

    def setup_scene(self) -> None:
        self.camera.background_color = BG
        self.background = full_screen_background()
        self.add(self.background)

    def clear_scene(self, run_time: float = 0.55, shift: np.ndarray = DOWN * 0.12) -> None:
        removable = [mobject for mobject in self.mobjects if mobject is not self.background]
        if removable:
            self.play(FadeOut(Group(*removable), shift=shift), run_time=run_time)

    def header(self, content: str, color: str = WHITE) -> Text:
        header = title_text(content, font_size=41, color=color, max_width=7.65)
        header.to_edge(UP, buff=0.72)
        return header

    def scene_0_cold_open(self) -> None:
        self.clear_scene(run_time=0.1)
        hook = self.header("تغطية الباك...", color=WHITE)
        slot = create_video_slot("خارج من الامتحان", "VIDEO_SLOT_01", scale=1.08)
        slot.move_to(DOWN * 0.12)
        slot.shift(DOWN * 1.1)
        flash = Rectangle(width=8.5, height=15.4, fill_color=WHITE, fill_opacity=0.0, stroke_opacity=0)

        self.play(slot.animate.shift(UP * 1.1), FadeIn(hook, shift=UP * 0.18), run_time=0.82, rate_func=smooth)
        self.play(flash.animate.set_fill(opacity=0.16), run_time=0.06)
        self.play(flash.animate.set_fill(opacity=0.0), run_time=0.18)
        self.play(Indicate(slot[8], color=RED, scale_factor=1.08), run_time=0.55)
        self.wait(0.55)

        self.primary_slot = slot
        self.hook_title = hook

    def scene_1_pattern_reveal(self) -> None:
        title = self.header("ماشي لقطة وحدة", color=SOFT_WHITE)
        slot_1_target = create_video_slot("خارج من الامتحان", "VIDEO_SLOT_01", scale=0.72)
        slot_2 = create_video_slot("سؤال بعد المادة", "VIDEO_SLOT_02", scale=0.72)
        slot_3 = create_video_slot("رد فعل تلميذ", "VIDEO_SLOT_03", scale=0.72)
        slot_1_target.move_to(LEFT * 2.55 + UP * 0.55)
        slot_2.move_to(UP * 0.82)
        slot_3.move_to(RIGHT * 2.55 + UP * 0.55)

        subtitle = subtitle_text("بعض التغطيات تحوس على اللقطة اللي تشعل التعليقات.", font_size=27, max_width=7.2)
        subtitle.to_edge(DOWN, buff=1.05)

        self.play(
            ReplacementTransform(self.hook_title, title),
            Transform(self.primary_slot, slot_1_target),
            run_time=0.85,
            rate_func=smooth,
        )
        self.play(
            LaggedStart(FadeIn(slot_2, shift=LEFT * 0.22), FadeIn(slot_3, shift=LEFT * 0.22), lag_ratio=0.18),
            FadeIn(subtitle, shift=UP * 0.12),
            run_time=1.05,
        )
        self.play(
            self.primary_slot.animate.shift(UP * 0.05),
            slot_2.animate.shift(UP * 0.12),
            slot_3.animate.shift(UP * 0.05),
            run_time=0.6,
            rate_func=there_and_back,
        )
        self.wait(0.7)
        self.video_slots = Group(self.primary_slot, slot_2, slot_3)
        self.pattern_title = title
        self.pattern_subtitle = subtitle

    def scene_2_selected_clip(self) -> None:
        self.play(FadeOut(self.pattern_subtitle, shift=DOWN * 0.1), run_time=0.35)

        lens = VGroup(
            Circle(radius=0.72, stroke_color=CYAN, stroke_width=2.5, fill_color=CYAN, fill_opacity=0.06),
            Circle(radius=0.42, stroke_color=SOFT_WHITE, stroke_width=1.2, stroke_opacity=0.42),
            Line(DOWN * 0.45, DOWN * 0.95, stroke_color=CYAN, stroke_width=4).rotate(-42 * DEGREES),
        )
        lens.move_to(LEFT * 3.1 + UP * 4.2)
        beam = Polygon(
            lens.get_center() + DOWN * 0.45,
            lens.get_center() + RIGHT * 1.0 + DOWN * 3.55,
            lens.get_center() + RIGHT * 2.25 + DOWN * 3.40,
            stroke_opacity=0,
            fill_color=CYAN,
            fill_opacity=0.09,
        )

        selected = title_text("لقطة مختارة", font_size=39, color=RED, max_width=4.6)
        bait = title_text("طُعم للتفاعل", font_size=37, color=RED, max_width=4.7)
        arrow = Arrow(selected.get_bottom(), bait.get_top(), buff=0.16, color=RED, stroke_width=3)
        selected.move_to(DOWN * 3.95)
        bait.next_to(selected, DOWN, buff=0.48)
        arrow = Arrow(selected.get_bottom(), bait.get_top(), buff=0.13, color=RED, stroke_width=3)
        hook = VGroup(
            Arc(radius=0.26, start_angle=-35 * DEGREES, angle=-245 * DEGREES, stroke_color=RED, stroke_width=3.2),
            Line(UP * 0.40, DOWN * 0.02, stroke_color=RED, stroke_width=3.2),
            make_ar_text("طُعم", font_size=22, color=RED, weight="BOLD"),
        )
        hook[2].next_to(hook[0], RIGHT, buff=0.12)
        hook.move_to(RIGHT * 3.0 + UP * 3.45)

        self.play(FadeIn(lens, scale=0.85), FadeIn(beam), run_time=0.45)
        scan_targets = [LEFT * 2.55 + UP * 2.72, UP * 3.0, RIGHT * 2.55 + UP * 2.72]
        for target, slot, tag in zip(scan_targets, self.video_slots, ("مرتبك", "إجابة متوترة", "ضحكة عفوية")):
            label = create_concept_word(tag, GOLD).scale(0.70)
            label.move_to(slot.get_top() + DOWN * 0.65)
            self.play(
                lens.animate.move_to(target),
                beam.animate.move_to(target + DOWN * 1.95),
                FadeIn(label, scale=0.84),
                Indicate(slot, color=GOLD, scale_factor=1.015),
                run_time=0.62,
            )
            self.play(FadeOut(label, scale=0.96), run_time=0.20)

        self.play(FadeOut(beam), lens.animate.move_to(hook.get_center()), FadeIn(selected, shift=UP * 0.16), run_time=0.58)
        self.play(ReplacementTransform(lens, hook), Create(arrow), FadeIn(bait, shift=UP * 0.12), run_time=0.58)
        self.wait(0.65)
        self.selection_title = VGroup(selected, arrow, bait, hook)

    def prepared_comments(self) -> list[Mobject]:
        comments = load_comment_images()
        if len(comments) < 8:
            base = comments[:]
            while len(comments) < 10:
                comments.append(base[len(comments) % len(base)].copy())
        return comments[:10]

    def scene_3_comment_avalanche(self) -> None:
        self.play(FadeOut(self.selection_title, shift=DOWN * 0.12), run_time=0.45)
        title = self.header("الجمهور يدخل", color=WHITE)
        self.play(ReplacementTransform(self.pattern_title, title), run_time=0.45)

        comments = Group()
        start_positions = [
            LEFT * 3.0 + UP * 3.7,
            RIGHT * 2.8 + UP * 3.45,
            LEFT * 3.2 + UP * 1.6,
            RIGHT * 3.0 + UP * 1.15,
            LEFT * 2.9 + DOWN * 0.9,
            RIGHT * 3.05 + DOWN * 1.4,
            LEFT * 2.25 + DOWN * 3.1,
            RIGHT * 2.45 + DOWN * 3.35,
            UP * 4.65,
            DOWN * 4.75,
        ]
        target_positions = [
            LEFT * 1.35 + UP * 1.85,
            RIGHT * 1.18 + UP * 1.65,
            LEFT * 1.75 + UP * 0.35,
            RIGHT * 1.55 + DOWN * 0.05,
            LEFT * 1.22 + DOWN * 1.45,
            RIGHT * 1.36 + DOWN * 1.55,
            LEFT * 0.42 + DOWN * 2.75,
            RIGHT * 0.52 + DOWN * 2.95,
            UP * 2.95,
            DOWN * 3.86,
        ]

        for index, comment in enumerate(self.prepared_comments()):
            comment.move_to(start_positions[index])
            comment.rotate(self.rng.uniform(-7, 7) * DEGREES)
            comment.set_z_index(18 + index)
            fit_to_frame(comment, max_width=3.0, max_height=1.05)
            self.play(FadeIn(comment, scale=0.70), run_time=0.16 + index * 0.015)
            self.play(
                comment.animate.scale(1.02 + index * 0.012).move_to(target_positions[index]),
                run_time=max(0.16, 0.40 - index * 0.015),
                rate_func=smooth,
            )
            comments.add(comment)

        harmful = create_fake_comment("فيمبوي", color=RED, danger=True, width=2.55)
        harmful.move_to(LEFT * 2.70 + DOWN * 3.85).rotate(-5 * DEGREES).set_z_index(40)
        replacement = create_fake_comment("وصم", color=RED, danger=True, width=2.25)
        replacement.move_to(harmful).rotate(-5 * DEGREES).set_z_index(40)
        self.play(FadeIn(harmful, scale=0.70), run_time=0.18)
        self.play(ReplacementTransform(harmful, replacement), run_time=0.32)
        comments.add(replacement)

        self.play(
            self.video_slots.animate.set_opacity(0.60),
            *[
                comment.animate.scale(1.04).shift(
                    np.array([self.rng.uniform(-0.16, 0.16), self.rng.uniform(-0.14, 0.16), 0])
                )
                for comment in comments
            ],
            run_time=0.82,
            rate_func=smooth,
        )
        self.wait(0.55)
        self.comments = comments
        self.avalanche_title = title

    def scene_4_human_hidden(self) -> None:
        student = create_student_icon(color=WHITE, accent=GOLD, scale_factor=0.92, stroke_width=4)
        student.move_to(ORIGIN + DOWN * 0.25)
        student.set_z_index(8)
        pressure_ring = Circle(radius=1.25, stroke_color=RED, stroke_width=2.5, stroke_opacity=0.58)
        pressure_ring.move_to(student)
        pressure_ring.set_z_index(7)
        caption = title_text("الطالب اختفى...\nوبقات السخرية.", font_size=42, color=WHITE, max_width=7.1)
        caption.to_edge(DOWN, buff=1.0)

        comment_moves = []
        for index, comment in enumerate(self.comments):
            angle = TAU * index / max(len(self.comments), 1)
            radius = 2.0 + 0.28 * (index % 3)
            target = student.get_center() + np.array([math.cos(angle) * radius, math.sin(angle) * radius, 0])
            comment_moves.append(comment.animate.move_to(target).scale(1.06 if index % 2 == 0 else 0.96))

        self.play(FadeIn(student, scale=0.85), Create(pressure_ring), run_time=0.55)
        self.play(
            self.video_slots.animate.set_opacity(0.20),
            LaggedStart(*comment_moves, lag_ratio=0.035),
            run_time=1.25,
            rate_func=smooth,
        )
        self.play(
            student.animate.scale(0.84).set_opacity(0.65),
            pressure_ring.animate.scale(1.18).set_stroke(opacity=0.38),
            FadeIn(caption, shift=UP * 0.18),
            run_time=0.85,
        )
        self.wait(0.8)
        self.hidden_student = student
        self.pressure_ring = pressure_ring
        self.hidden_caption = caption

    def scene_5_comments_to_concepts(self) -> None:
        main_sentence = title_text(
            "التعليقات ما كانتش نتيجة الفيديو...\nكانت هدفو.",
            font_size=39,
            color=WHITE,
            max_width=7.45,
        )
        main_sentence.move_to(DOWN * 2.55)

        concept_texts = ["السخرية", "محا كمة", "الضح_ك", "القذ ف", "الإذلال", "التفاعل"]
        concepts = VGroup()
        for index, word in enumerate(concept_texts):
            angle = PI / 2 - index * TAU / len(concept_texts)
            color = RED if word in ("التنمر", "الإذلال", "الوصم") else GOLD if word == "التفاعل" else CYAN
            concept = create_concept_word(word, color)
            concept.move_to(np.array([2.35 * math.cos(angle), 2.0 * math.sin(angle) + 0.95, 0]))
            concepts.add(concept)

        self.play(
            FadeOut(self.avalanche_title, shift=UP * 0.1),
            FadeOut(self.video_slots, shift=DOWN * 0.12),
            FadeOut(self.hidden_caption, shift=DOWN * 0.1),
            FadeOut(self.hidden_student, scale=0.92),
            FadeOut(self.pressure_ring, scale=1.12),
            run_time=0.58,
        )
        # Real comment screenshots are raster ImageMobjects.  Manim cannot
        # morph their point data into vector text reliably, so dissolve them
        # into the concept words instead of geometrically transforming them.
        self.play(
            FadeOut(self.comments, scale=0.96),
            FadeIn(concepts, scale=0.92),
            run_time=1.05,
            rate_func=smooth,
        )
        self.play(FadeIn(main_sentence, shift=UP * 0.22), run_time=0.72)
        self.play(Circumscribe(main_sentence, color=GOLD, buff=0.18), run_time=0.75)
        self.wait(0.9)
        self.concepts = concepts
        self.main_reveal = main_sentence

    def scene_6_who_wins(self) -> None:
        equation = title_text("سخرية الجمهور = تفاعل للصفحة", font_size=38, color=WHITE, max_width=7.6)
        equation.to_edge(UP, buff=1.15)

        board = RoundedRectangle(
            width=7.55,
            height=6.15,
            corner_radius=0.22,
            stroke_color=CYAN,
            stroke_width=2.2,
            fill_color=DARK_CARD,
            fill_opacity=0.76,
        )
        board.move_to(DOWN * 0.10)

        student_icon = create_student_icon(color=SOFT_WHITE, accent=RED, scale_factor=0.62, stroke_width=3.6)
        student_label = make_ar_text("الطالب؟ لا", font_size=28, color=SOFT_WHITE, max_width=2.1)
        student_group = VGroup(student_icon, student_label).arrange(DOWN, buff=0.26)
        student_group.move_to(LEFT * 2.45 + UP * 0.65)

        crowd = VGroup(*[create_phone_icon(0.66, color=SOFT_WHITE) for _ in range(3)]).arrange(RIGHT, buff=0.20)
        crowd_label = make_ar_text("الجمهور؟ لا", font_size=28, color=SOFT_WHITE, max_width=2.2)
        crowd_group = VGroup(crowd, crowd_label).arrange(DOWN, buff=0.26)
        crowd_group.move_to(RIGHT * 2.45 + UP * 0.65)

        page = create_video_slot("صفحة", "PAGE", scale=0.45)
        page_label = make_ar_text("الصفحة؟ نعم", font_size=31, color=GOLD, weight="BOLD", max_width=2.4)
        page_group = VGroup(page, page_label).arrange(DOWN, buff=0.18)
        page_group.move_to(DOWN * 2.05)

        formula = subtitle_text("تعليقات + مشاركة + وقت مشاهدة", font_size=27, color=CYAN, max_width=6.5)
        formula.move_to(DOWN * 0.70)
        down_arrow = Arrow(formula.get_bottom(), page_group.get_top(), buff=0.18, color=GOLD, stroke_width=3.2)

        self.play(
            FadeOut(self.main_reveal, shift=DOWN * 0.12),
            self.concepts.animate.scale(0.70).to_edge(UP, buff=2.10).set_opacity(0.48),
            FadeIn(board, scale=0.98),
            FadeIn(equation, shift=UP * 0.18),
            run_time=0.82,
        )
        self.play(FadeIn(student_group, shift=UP * 0.14), FadeIn(crowd_group, shift=UP * 0.14), run_time=0.62)
        self.play(FadeIn(formula, shift=UP * 0.10), Create(down_arrow), FadeIn(page_group, shift=UP * 0.16), run_time=0.82)
        self.play(Indicate(page_label, color=GOLD, scale_factor=1.05), run_time=0.55)
        self.wait(0.85)
        self.analysis_board = VGroup(board, equation, student_group, crowd_group, formula, down_arrow, page_group, self.concepts)

    def scene_7_algorithm(self) -> None:
        self.clear_scene(run_time=0.58)
        title = self.header("الخوارزمية ما تقراش نيتك", color=WHITE)
        sub = subtitle_text("تقرا تفاعلك.", font_size=35, color=CYAN, max_width=5.5)
        sub.next_to(title, DOWN, buff=0.25)

        machine, inputs, arrows, output_arrow, output = create_algorithm_machine()
        machine.move_to(DOWN * 0.30)
        inputs.move_to(LEFT * 3.15 + UP * 0.20)
        arrows = VGroup()
        for item in inputs:
            arrows.add(
                Arrow(
                    item.get_right() + RIGHT * 0.08,
                    machine[0].get_left() + LEFT * 0.10 + UP * (item.get_center()[1] * 0.08),
                    buff=0.02,
                    color=GRAY,
                    stroke_width=3,
                    max_tip_length_to_length_ratio=0.14,
                )
            )
        output_arrow.next_to(machine[0], RIGHT, buff=0.16)
        output.next_to(output_arrow, RIGHT, buff=0.15)

        duplicate_reels = VGroup()
        for index in range(5):
            reel = create_video_slot("", f"SPREAD_{index + 1:02d}", scale=0.25)
            reel.move_to(RIGHT * (1.15 + index * 0.46) + DOWN * (3.65 + (index % 2) * 0.18))
            reel.set_opacity(0.28)
            duplicate_reels.add(reel)

        self.play(FadeIn(title, shift=UP * 0.14), FadeIn(sub, shift=UP * 0.10), run_time=0.6)
        self.play(FadeIn(machine, scale=0.96), run_time=0.55)
        self.play(LaggedStart(*[FadeIn(item, shift=RIGHT * 0.16) for item in inputs], lag_ratio=0.12), run_time=0.85)
        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows], lag_ratio=0.08), run_time=0.72)
        self.play(GrowArrow(output_arrow), FadeIn(output, shift=LEFT * 0.10), run_time=0.55)
        self.play(FadeIn(duplicate_reels, shift=UP * 0.20), output_arrow.animate.set_stroke(width=7), run_time=0.75)
        self.wait(0.75)
        self.algorithm_group = VGroup(title, sub, machine, inputs, arrows, output_arrow, output, duplicate_reels)

    def scene_8_audience_mirror(self) -> None:
        self.clear_scene(run_time=0.58)
        title = self.header("هل راني ننتقد؟", color=WHITE)
        subtitle = title_text("ولا راني نكبر الأذى؟", font_size=37, color=GOLD, max_width=7.2)
        subtitle.next_to(title, DOWN, buff=0.24)

        mirror = RoundedRectangle(
            width=5.6,
            height=6.35,
            corner_radius=0.40,
            stroke_color=SOFT_WHITE,
            stroke_width=2.4,
            fill_color=SOFT_WHITE,
            fill_opacity=0.045,
        )
        mirror.move_to(DOWN * 0.10)

        phones = VGroup()
        for index, x in enumerate((-1.55, 0, 1.55)):
            phone = create_phone_icon(scale=1.02, color=CYAN if index != 1 else GOLD)
            phone.move_to([x, 0.45 - 0.30 * (index % 2), 0])
            phones.add(phone)

        page = create_video_slot("الفيديو", "PAGE_TARGET", scale=0.43)
        page.move_to(DOWN * 3.65)
        arrows = VGroup()
        for phone in phones:
            arrow = Arrow(phone.get_bottom() + DOWN * 0.08, page.get_top() + UP * 0.06, buff=0.05, color=RED, stroke_width=3)
            arrows.add(arrow)

        labels = VGroup(
            create_concept_word("الضحك", RED),
            create_concept_word("الحك_م", RED),
            create_concept_word("المشاركة", GOLD),
        ).arrange(RIGHT, buff=0.26)
        labels.scale(0.76)
        labels.move_to(UP * 2.35)

        self.play(FadeIn(title, shift=UP * 0.14), FadeIn(subtitle, shift=UP * 0.10), run_time=0.60)
        self.play(Create(mirror), FadeIn(phones, scale=0.84), run_time=0.82)
        self.play(LaggedStart(*[FadeIn(label, scale=0.70) for label in labels], lag_ratio=0.12), run_time=0.72)
        self.play(FadeIn(page, shift=UP * 0.16), LaggedStart(*[GrowArrow(arrow) for arrow in arrows], lag_ratio=0.12), run_time=0.82)
        self.play(Indicate(labels, color=GOLD, scale_factor=1.03), run_time=0.65)
        self.wait(0.78)
        self.mirror_group = VGroup(title, subtitle, mirror, phones, labels, page, arrows)

    def scene_9_religious_bridge(self) -> None:
        self.clear_scene(run_time=0.58)
        title = self.header("الدين قبل الخوارزمية", color=GOLD)
        icon = create_book_icon(scale=1.55)
        icon.move_to(UP * 2.75)
        glow = Circle(radius=1.62, stroke_opacity=0, fill_color=GOLD, fill_opacity=0.09)
        glow.move_to(icon)

        responsibility = VGroup(
            create_concept_word("لسا نك", GOLD),
            create_concept_word("تعليقك", GOLD),
            create_concept_word("مشاركتك", GOLD),
        ).arrange(DOWN, buff=0.35)
        responsibility.move_to(DOWN * 0.35)

        line = subtitle_text("المسلم ما يكونش سبب في فضح أو إهانة إنسان.", font_size=30, color=SOFT_WHITE, max_width=7.35)
        line.to_edge(DOWN, buff=1.10)

        self.play(FadeIn(title, shift=UP * 0.14), FadeIn(glow, scale=0.75), FadeIn(icon, scale=0.84), run_time=0.72)
        self.play(LaggedStart(*[FadeIn(item, shift=UP * 0.12) for item in responsibility], lag_ratio=0.15), run_time=0.92)
        self.play(FadeIn(line, shift=UP * 0.14), run_time=0.65)
        self.wait(0.9)
        self.bridge_group = VGroup(title, glow, icon, responsibility, line)

    def scene_10_guidance_cards(self) -> None:
        self.clear_scene(run_time=0.52)
        title = self.header("ميزان واضح", color=GOLD)
        cards = create_religious_guidance_cards()
        cards.move_to(UP * 0.45)
        note = subtitle_text("إرشاد مختصر: لا سخرية، لا غيبة، لا نشر للأذى.", font_size=28, color=SOFT_WHITE, max_width=7.3)
        note.to_edge(DOWN, buff=1.25)

        self.play(FadeIn(title, shift=UP * 0.12), run_time=0.42)
        self.play(LaggedStart(*[FadeIn(card, shift=UP * 0.16) for card in cards], lag_ratio=0.18), run_time=1.05)
        self.play(FadeIn(note, shift=UP * 0.12), run_time=0.55)
        self.wait(1.05)
        self.guidance_group = VGroup(title, cards, note)

    def scene_11_practical_actions(self) -> None:
        self.clear_scene(run_time=0.52)
        title = self.header("رفض الأذى ما يكونش بنشر الأذى", color=GREEN)
        cards = VGroup(
            create_action_card("ما تعلّقش بسخرية"),
            create_action_card("ما تشاركش الإهانة"),
            create_action_card("بلّغ إذا فيها تنمر أو كشف"),
            create_action_card("انتقد الفكرة... ما تفضحش الإنسان"),
        ).arrange(DOWN, buff=0.34)
        cards.move_to(DOWN * 0.08)

        self.play(FadeIn(title, shift=UP * 0.14), run_time=0.48)
        active: list[Mobject] = []
        for card in cards:
            self.play(*[old.animate.set_opacity(0.56) for old in active], FadeIn(card, shift=UP * 0.18), run_time=0.48)
            self.play(Indicate(card[1], color=GREEN, scale_factor=1.18), run_time=0.25)
            active.append(card)
        self.wait(0.9)
        self.actions_group = VGroup(title, cards)

    def scene_12_break_the_loop(self) -> None:
        self.clear_scene(run_time=0.55)
        title = self.header("الحلقة تتكسر عندك أنت", color=WHITE)
        nodes, arrows = create_loop_diagram()
        loop = VGroup(arrows, nodes)
        break_line = Line(LEFT * 1.10, RIGHT * 1.10, stroke_color=GREEN, stroke_width=7)
        break_line.rotate(-18 * DEGREES)
        break_line.move_to(DOWN * 2.02 + RIGHT * 0.85)
        break_text = title_text("توقف", font_size=34, color=GREEN, max_width=2.1)
        break_text.next_to(break_line, DOWN, buff=0.12)

        audience = VGroup(create_phone_icon(scale=0.92, color=GREEN), make_ar_text("المشاهدين", font_size=25, color=GREEN, weight="BOLD"))
        audience.arrange(DOWN, buff=0.22)
        audience.move_to(DOWN * 3.15)

        self.play(FadeIn(title, shift=UP * 0.14), run_time=0.45)
        self.play(LaggedStart(Create(arrows), FadeIn(nodes, scale=0.85), lag_ratio=0.15), run_time=1.0)
        self.play(FadeIn(audience, shift=UP * 0.14), run_time=0.45)
        self.play(Create(break_line), FadeIn(break_text, shift=UP * 0.08), arrows.animate.set_opacity(0.25), run_time=0.72)
        self.play(Indicate(audience, color=GREEN, scale_factor=1.05), run_time=0.55)
        self.wait(0.9)
        self.loop_group = VGroup(title, loop, break_line, break_text, audience)

    def scene_13_media_nuance(self) -> None:
        self.clear_scene(run_time=0.55)
        title = self.header("ماشي كل إعلام هكا", color=SOFT_WHITE)
        good = RoundedRectangle(
            width=3.55,
            height=5.45,
            corner_radius=0.18,
            stroke_color=GREEN,
            stroke_width=2.2,
            fill_color=GREEN,
            fill_opacity=0.07,
        )
        bad = RoundedRectangle(
            width=3.55,
            height=5.45,
            corner_radius=0.18,
            stroke_color=RED,
            stroke_width=2.2,
            fill_color=RED,
            fill_opacity=0.07,
        )
        good.move_to(LEFT * 2.05 + DOWN * 0.05)
        bad.move_to(RIGHT * 2.05 + DOWN * 0.05)

        good_title = title_text("تغطية محترمة", font_size=28, color=GREEN, max_width=2.9)
        bad_title = title_text("تغطية مؤذية", font_size=28, color=RED, max_width=2.9)
        good_title.move_to(good.get_top() + DOWN * 0.58)
        bad_title.move_to(bad.get_top() + DOWN * 0.58)

        good_rows = VGroup(
            create_action_card("تنقل الحدث", GREEN).scale(0.54),
            create_action_card("تحفظ الكرامة", GREEN).scale(0.54),
            create_action_card("تدعم الطالب", GREEN).scale(0.54),
        ).arrange(DOWN, buff=0.34)
        bad_rows = VGroup(
            create_concept_word("التص_يد", RED).scale(0.78),
            create_concept_word("السخرية", RED).scale(0.78),
            create_concept_word("الإذلال", RED).scale(0.78),
        ).arrange(DOWN, buff=0.44)
        good_rows.move_to(good.get_center() + DOWN * 0.45)
        bad_rows.move_to(bad.get_center() + DOWN * 0.45)

        self.play(FadeIn(title, shift=UP * 0.14), Create(good), Create(bad), run_time=0.75)
        self.play(FadeIn(good_title, shift=UP * 0.10), FadeIn(bad_title, shift=UP * 0.10), run_time=0.46)
        self.play(LaggedStart(FadeIn(good_rows, shift=UP * 0.12), FadeIn(bad_rows, shift=UP * 0.12), lag_ratio=0.15), run_time=0.85)
        self.play(Indicate(good_title, color=GREEN, scale_factor=1.03), run_time=0.45)
        self.wait(0.9)
        self.nuance_group = VGroup(title, good, bad, good_title, bad_title, good_rows, bad_rows)

    def scene_14_restore_humanity(self) -> None:
        self.clear_scene(run_time=0.55)
        student = create_student_icon(color=WHITE, accent=GREEN, scale_factor=1.08, stroke_width=4.2)
        student.move_to(UP * 1.10)
        glow = Circle(radius=1.55, stroke_opacity=0, fill_color=GOLD, fill_opacity=0.095)
        glow.move_to(student)
        headline = title_text("الطالب إنسان...\nماشي محتوى.", font_size=42, color=WHITE, max_width=7.2)
        headline.to_edge(UP, buff=0.92)

        support_words = VGroup(
            create_concept_word("ربي يوفقك", GREEN),
            create_concept_word("راك ماشي وحدك", GREEN),
            create_concept_word("الله يفتح عليك", GOLD),
            create_concept_word("كل مادة صفحة جديدة", CYAN),
        )
        positions = [LEFT * 2.35 + DOWN * 1.20, RIGHT * 2.25 + DOWN * 1.20, LEFT * 2.0 + DOWN * 2.55, RIGHT * 1.85 + DOWN * 2.55]
        for word, position in zip(support_words, positions):
            word.scale(0.75)
            word.move_to(position)

        self.play(FadeIn(headline, shift=UP * 0.14), FadeIn(glow, scale=0.70), FadeIn(student, scale=0.84), run_time=0.80)
        self.play(LaggedStart(*[FadeIn(word, shift=UP * 0.12) for word in support_words], lag_ratio=0.16), run_time=1.05)
        self.play(Circumscribe(student, color=GREEN, buff=0.18), run_time=0.70)
        self.wait(1.0)
        self.humanity_group = VGroup(headline, glow, student, support_words)

    def scene_15_final_punchline(self) -> None:
        self.clear_scene(run_time=0.65)
        broken_nodes, broken_arrows = create_loop_diagram()
        broken_loop = VGroup(broken_arrows, broken_nodes).scale(0.82)
        broken_loop.move_to(UP * 2.75)
        broken_loop.set_opacity(0.28)
        slash = Line(LEFT * 1.65, RIGHT * 1.65, stroke_color=GREEN, stroke_width=8)
        slash.rotate(-20 * DEGREES)
        slash.move_to(broken_loop)

        line_1 = title_text("لا تكن التفاعل الذي يبحثون عنه.", font_size=39, color=WHITE, max_width=7.5)
        line_2 = title_text("ولا تكن لسانًا يؤذي إنسانًا.", font_size=38, color=GOLD, max_width=7.35)
        lines = VGroup(line_1, line_2).arrange(DOWN, buff=0.34)
        lines.move_to(DOWN * 0.65)

        brand = make_ar_text("نمط - Namat", font_size=43, color=WHITE, weight="BOLD", max_width=6.5)
        brand.to_edge(DOWN, buff=1.25)
        slogan = subtitle_text("نفهمو الظاهرة... قبل ما نكرروها.", font_size=24, color=SOFT_WHITE, max_width=6.4)
        slogan.next_to(brand, DOWN, buff=0.22)

        self.play(FadeIn(broken_loop, scale=0.85), Create(slash), run_time=0.75)
        self.play(FadeIn(line_1, shift=UP * 0.18), run_time=0.65)
        self.play(FadeIn(line_2, shift=UP * 0.12), run_time=0.65)
        self.play(FadeIn(brand, shift=UP * 0.12), FadeIn(slogan, shift=UP * 0.08), run_time=0.62)
        self.play(Circumscribe(lines, color=GOLD, buff=0.18), run_time=0.85)
        self.wait(2.2)
