# -*- coding: utf-8 -*-
"""Cinematic 9:16 Namat video about judging without knowing the full story.

Render from the project root:
    manim -pqh projects/namat_spiderman_yemen_cinematic.py NamatSpidermanYemenCinematic

Root wrapper:
    manim -pqh main.py NamatSpidermanYemenCinematic

Asset placeholders expected by the brief:
    assets/videos/hook_fall_blur.mp4
    assets/crater_background.png
    assets/namat/namat_character.svg
    assets/phone_frame.svg
    assets/social_icons/

The hook video is treated as symbolic and blurred. If the asset is missing,
the scene stays renderable through Manim vector placeholders.
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

from common import (
    BLACK,
    CYAN,
    GOLD,
    GREEN,
    NAVY,
    RED,
    SAFE_WIDTH,
    SOFT_WHITE,
    SURFACE,
    blurred_video_placeholder,
    cinematic_background,
    cinematic_fade_in,
    comment_storm,
    create_analysis_node,
    create_comment_bubble,
    create_crater_shape,
    create_human_silhouette,
    create_scale_icon,
    line_network_transition,
    make_latin_text,
    mercy_rewrite_transition,
    namat_signature_outro,
    phone_screen_container,
    safe_ar_text,
    slow_camera_push,
    typewriter_text,
    word_cloud_reveal,
)


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30


WHITE = "#F4F7FB"
MUTED = "#9FB3C8"
DEEP = "#030A12"
DARK_CARD = "#0C1B2D"

HOOK_VIDEO = ROOT / "assets" / "videos" / "hook_fall_blur.mp4"
LEGACY_HOOK_VIDEO = ROOT / "assets" / "hook_blurred_fall.mp4"


VOICE_OVER = {
    "01_hook": {
        "duration": 9.0,
        "text": "هو سقط مرة...\nلكن بعض القلوب سقطت بعده ألف مرة.",
    },
    "02_comments": {
        "duration": 13.0,
        "text": "كي مات القعقاع، كاين ناس دعاتلو بالرحمة... وكاين ناس حكمت عليه. وكاين ناس... ضحكت.",
    },
    "03_wrong_question": {
        "duration": 13.0,
        "text": "قالوا: علاه يدير هك؟ السؤال في ظاهرو مفهوم... بصح بعد الموت، وبطريقة قاسية، يولي ظلم.",
    },
    "04_human": {
        "duration": 14.0,
        "text": "سمّوه سبايدرمان اليمن. بصح قبل اللقب، قبل الترند، قبل الفيديو... كان إنسان.",
    },
    "05_content": {
        "duration": 14.0,
        "text": "في السوشيال ميديا، الإنسان يتحول بسرعة إلى محتوى. تعليق، لايك، مشاركة... مرات تولي ضغط.",
    },
    "06_unseen": {
        "duration": 17.0,
        "text": "إحنا شفنا فيديو. ما شفناش حياتو. أنت شفت عشر ثواني... ما شفتش ثلاثين سنة.",
    },
    "07_cruel": {
        "duration": 14.0,
        "text": "اللي يكتب: مليح كي مات... لازم يوقف لحظة. تخيل أمو تقراها. تخيل خوتو يشوفوها.",
    },
    "08_mercy": {
        "duration": 15.0,
        "text": "ديننا ما علمناش نفرحو في موت الناس. الكلمة بعد الموت أمانة.",
    },
    "09_before_comment": {
        "duration": 15.0,
        "text": "قبل ما تكتب تعليق، اسأل روحك: هل نعرف قصتو؟ هل الكلمة رحمة ولا جرح؟",
    },
    "10_namat": {
        "duration": 16.0,
        "text": "القصة ماشي فقط قصة القعقاع. القصة قصتنا إحنا... كيفاش نحكمو بسرعة.",
    },
    "11_final": {
        "duration": 12.0,
        "text": "أنت شفت النهاية... ما شفتش القصة. قبل ما تقول علاه دار هك، قول: ربي يرحمو.",
    },
}


class NamatSpidermanYemenCinematic(MovingCameraScene):
    """Vertical cinematic social-analysis short for نمط - Namat."""

    def construct(self) -> None:
        self.rng = random.Random(44)
        self.setup_scene()
        self.scene_01_blurred_fall_hook()
        self.scene_02_comment_invasion()
        self.scene_03_wrong_question()
        self.scene_04_who_was_he()
        self.scene_05_human_to_content()
        self.scene_06_unseen_story()
        self.scene_07_cruel_comment()
        self.scene_08_mercy_reflection()
        self.scene_09_before_comment()
        self.scene_10_namat_reveal()
        self.scene_11_final_hit_and_closing()

    def setup_scene(self) -> None:
        self.camera.background_color = NAVY
        self.background = cinematic_background(seed=12)
        self.add(self.background)

    def reset_camera(self) -> None:
        self.camera.frame.move_to(ORIGIN)
        self.camera.frame.set(width=config.frame_width)

    def clear_scene(self, run_time: float = 0.56, shift: np.ndarray = DOWN * 0.12) -> None:
        self.reset_camera()
        removable = [mobject for mobject in self.mobjects if mobject is not self.background]
        if removable:
            self.play(FadeOut(Group(*removable), shift=shift), run_time=run_time, rate_func=smooth)

    def title(
        self,
        text: str,
        y: float = 5.35,
        size: float = 42,
        color: str = WHITE,
        max_width: float = SAFE_WIDTH,
    ) -> Text:
        label = safe_ar_text(text, font_size=size, color=color, weight="BOLD", max_width=max_width)
        label.move_to([0, y, 0])
        return label

    def caption(
        self,
        text: str,
        y: float = -5.10,
        size: float = 30,
        color: str = WHITE,
        accent: str = CYAN,
        width: float = 7.25,
    ) -> VGroup:
        label = safe_ar_text(text, font_size=size, color=color, weight="BOLD", max_width=width - 0.7)
        box = RoundedRectangle(
            width=min(width, max(2.1, label.width + 0.64)),
            height=max(0.72, label.height + 0.24),
            corner_radius=0.15,
            stroke_color=accent,
            stroke_width=1.7,
            fill_color=DARK_CARD,
            fill_opacity=0.84,
        )
        label.move_to(box)
        group = VGroup(box, label)
        group.move_to([0, y, 0])
        return group

    def pulse_pause(self, target: Mobject, color: str = GOLD, run_time: float = 0.58) -> None:
        self.play(Circumscribe(target, color=color, buff=0.16), run_time=run_time)

    def make_social_metric(self, text: str, color: str, width: float = 1.35) -> VGroup:
        metric = create_analysis_node(text, color=color, width=width)
        metric.scale(0.72)
        return metric

    def scene_01_blurred_fall_hook(self) -> None:
        self.clear_scene(run_time=0.05)
        # VO:
        # "هو سقط مرة..."
        # "لكن بعض القلوب سقطت بعده ألف مرة."
        # Duration target: 9.0s
        hook_path = HOOK_VIDEO if HOOK_VIDEO.exists() else LEGACY_HOOK_VIDEO
        hook = blurred_video_placeholder(hook_path, label="assets/videos/hook_fall_blur.mp4")
        hook.set_z_index(-5)
        hook.save_state()

        preview_scale = 0.38
        preview_center = UP * 3.48
        full_preview_border = RoundedRectangle(
            width=config.frame_width - 0.34,
            height=config.frame_height - 0.56,
            corner_radius=0.30,
            stroke_color=CYAN,
            stroke_width=2.0,
            fill_opacity=0,
        )
        full_preview_border.set_stroke(opacity=0.36)
        full_preview_border.set_z_index(12)

        compact_preview_border = RoundedRectangle(
            width=(config.frame_width + 0.35) * preview_scale + 0.34,
            height=(config.frame_height + 0.35) * preview_scale + 0.30,
            corner_radius=0.18,
            stroke_color=CYAN,
            stroke_width=2.4,
            fill_opacity=0,
        )
        compact_preview_border.move_to(preview_center)
        compact_preview_border.set_stroke(opacity=0.82)
        compact_preview_border.set_z_index(12)

        note = safe_ar_text("المشهد مطموس احترامًا للميت", font_size=18, color=MUTED, max_width=5.8)
        note.next_to(compact_preview_border, DOWN, buff=0.18)
        note.set_opacity(0.74)

        line_1 = typewriter_text("هذا ليس مجرد سقوط...", font_size=43, color=WHITE, max_width=6.9)
        line_1.move_to(DOWN * 1.12)
        line_2 = typewriter_text("السقوط الحقيقي جاء بعده.", font_size=44, color=WHITE, max_width=6.9)
        line_2.move_to(DOWN * 2.18)

        self.play(FadeIn(hook, scale=1.02), Create(full_preview_border), run_time=0.85, rate_func=smooth)
        slow_camera_push(self, scale=0.965, duration=1.35)
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).set(width=config.frame_width),
            hook.animate.scale(preview_scale).move_to(preview_center),
            Transform(full_preview_border, compact_preview_border),
            run_time=1.05,
            rate_func=smooth,
        )
        self.wait(0.18)
        self.play(Write(line_1), run_time=1.05)
        self.wait(0.70)

        freeze_flash = Rectangle(
            width=config.frame_width + 0.4,
            height=config.frame_height + 0.4,
            fill_color=WHITE,
            fill_opacity=0,
            stroke_opacity=0,
        )
        freeze_flash.set_z_index(30)
        self.add(freeze_flash)
        self.play(freeze_flash.animate.set_fill(opacity=0.11), run_time=0.07)
        self.play(freeze_flash.animate.set_fill(opacity=0), run_time=0.16)
        self.remove(freeze_flash)

        self.play(
            FadeIn(note, shift=UP * 0.08),
            line_1.animate.shift(UP * 0.52).set_opacity(0.34),
            run_time=0.55,
            rate_func=smooth,
        )
        self.play(FadeIn(line_2, shift=UP * 0.16, scale=0.97), run_time=0.78, rate_func=smooth)
        self.wait(2.25)

        self.hook_frame = hook
        self.hook_preview_border = full_preview_border
        self.hook_preview_scale = preview_scale
        self.hook_note = note
        self.hook_line_1 = line_1
        self.hook_line_2 = line_2

    def scene_02_comment_invasion(self) -> None:
        # VO:
        # "كي مات القعقاع، كاين ناس دعاتلو بالرحمة..."
        # "وكاين ناس حكمت عليه. وكاين ناس... ضحكت."
        # Duration target: 13.0s
        comments = [
            "علاه يدير هك؟",
            "كان يحوس على الشهرة",
            "مليح كي مات...",
            "هههههه",
            "يستاهل",
            "وش كان يستنى؟",
            "غير مغامرة وخلاص",
        ]
        bubbles = comment_storm(comments)
        for index, bubble in enumerate(bubbles):
            bubble.set_opacity(0)
            bubble.shift(UP * (0.08 * (index % 2)) + OUT * 0.01)

        self.play(
            self.hook_frame.animate.scale(1 / self.hook_preview_scale).move_to(ORIGIN).set_opacity(0.72),
            FadeOut(self.hook_preview_border, scale=1.04),
            self.hook_line_1.animate.set_opacity(0.16),
            self.hook_line_2.animate.set_opacity(0.28),
            run_time=0.64,
            rate_func=smooth,
        )
        self.play(
            LaggedStart(
                *[
                    bubble.animate.set_opacity(0.96).shift(DOWN * (0.08 * (index % 2))).scale(1.0)
                    for index, bubble in enumerate(bubbles)
                ],
                lag_ratio=0.12,
            ),
            run_time=2.15,
            rate_func=smooth,
        )

        silence = self.caption("كي يموت الإنسان... تبان قلوب الناس.", y=-4.78, size=29, accent=RED)
        self.wait(1.50)
        self.play(FadeIn(silence, shift=UP * 0.12), run_time=0.62)
        self.wait(1.05)
        self.play(
            LaggedStart(
                *[Indicate(bubble, color=RED, scale_factor=1.025) for bubble in (bubbles[3], bubbles[4])],
                lag_ratio=0.24,
            ),
            run_time=1.10,
        )
        self.wait(0.55)

        selected = bubbles[0]
        other_comments = VGroup(*[bubble for index, bubble in enumerate(bubbles) if index != 0])
        question = typewriter_text("علاه يدير هك؟", font_size=68, color=WHITE, weight="BOLD", max_width=7.0)
        question.move_to(ORIGIN)

        self.play(
            other_comments.animate.set_opacity(0.13).shift(DOWN * 0.22),
            selected.animate.scale(1.36).move_to(ORIGIN),
            silence.animate.set_opacity(0.12),
            run_time=0.82,
            rate_func=smooth,
        )
        self.play(
            ReplacementTransform(selected, question),
            FadeOut(other_comments, scale=1.04),
            FadeOut(self.hook_frame),
            FadeOut(self.hook_note),
            FadeOut(self.hook_line_1),
            FadeOut(self.hook_line_2),
            FadeOut(silence),
            run_time=0.86,
            rate_func=smooth,
        )
        self.wait(0.35)
        self.crash_question = question

    def scene_03_wrong_question(self) -> None:
        # VO:
        # "قالوا: علاه يدير هك؟ السؤال في ظاهرو مفهوم..."
        # "السؤال الأعمق هو: واش خلاه يوصل لهنا؟"
        # Duration target: 13.0s
        self.play(
            self.crash_question.animate.to_edge(UP, buff=1.05).scale(0.66).set_color(RED),
            run_time=0.72,
            rate_func=smooth,
        )
        strike = Line(
            self.crash_question.get_left() + LEFT * 0.12,
            self.crash_question.get_right() + RIGHT * 0.12,
            stroke_color=RED,
            stroke_width=4.4,
        )
        strike.rotate(-4 * DEGREES)
        self.play(Create(strike), run_time=0.32)

        deeper_specs = [
            ("علاه الخطر ولى طريق؟", LEFT * 2.35 + UP * 2.45, CYAN),
            ("علاه الموهبة بلا حماية؟", RIGHT * 2.05 + UP * 1.55, CYAN),
            ("علاه الفقر يدفع للحافة؟", LEFT * 2.15 + DOWN * 0.40, GOLD),
            ("علاه الخوارزمية تحب المخاطرة؟", RIGHT * 2.15 + DOWN * 1.35, GOLD),
        ]
        nodes = VGroup()
        lines = VGroup()
        for text, position, color in deeper_specs:
            node = create_analysis_node(text, color=color, width=2.78)
            node.move_to(position)
            nodes.add(node)
            line = Line(self.crash_question.get_bottom() + DOWN * 0.10, node.get_top() + UP * 0.05)
            line.set_stroke(color, width=1.45, opacity=0.44)
            lines.add(line)

        main = safe_ar_text(
            "السؤال ماشي فقط: علاه خاطر؟\nالسؤال: واش خلاه يوصل لهنا؟",
            font_size=35,
            color=WHITE,
            weight="BOLD",
            max_width=7.15,
        )
        main.move_to(DOWN * 4.30)

        self.wait(1.05)
        self.play(LaggedStart(*[Create(line) for line in lines], lag_ratio=0.09), run_time=0.82)
        self.play(LaggedStart(*[FadeIn(node, scale=0.82) for node in nodes], lag_ratio=0.10), run_time=1.05)
        self.wait(1.50)
        self.play(FadeIn(main, shift=UP * 0.12), run_time=0.66)
        self.pulse_pause(main, color=GOLD, run_time=0.78)
        self.wait(1.25)

        human = create_human_silhouette(scale=1.34, color=SOFT_WHITE, accent=CYAN)
        human.move_to(UP * 0.70)
        crater = create_crater_shape(width=7.75, height=3.30)
        crater.move_to(DOWN * 2.70)
        human.set_z_index(6)
        crater.set_z_index(2)

        mind_map = VGroup(self.crash_question, strike, lines, nodes, main)
        self.play(
            mind_map.animate.scale(0.92).set_opacity(0.10).shift(UP * 0.22),
            run_time=0.45,
            rate_func=smooth,
        )
        self.play(
            ReplacementTransform(mind_map, human),
            FadeIn(crater, shift=UP * 0.12),
            run_time=1.18,
            rate_func=smooth,
        )
        self.wait(0.45)
        self.human = human
        self.crater = crater

    def scene_04_who_was_he(self) -> None:
        # VO:
        # "سمّوه سبايدرمان اليمن..."
        # "بصح قبل اللقب، قبل الترند، قبل الفيديو... كان إنسان."
        # Duration target: 14.0s
        title = self.title("من كان قبل الترند؟", y=5.50, size=39)
        name = safe_ar_text("سمّوه: سبايدرمان اليمن", font_size=39, color=WHITE, weight="BOLD", max_width=6.7)
        name.move_to(UP * 3.55)
        human_line = safe_ar_text("لكن قبل اللقب...\nكان إنسان.", font_size=45, color=GOLD, weight="BOLD", max_width=6.6)
        human_line.move_to(DOWN * 4.10)

        left_label = create_analysis_node("الناس شافت لقب", color=RED, width=2.45)
        right_label = create_analysis_node("لكن كان عندو حياة", color=GOLD, width=2.65)
        left_label.move_to(LEFT * 2.25 + UP * 1.55)
        right_label.move_to(RIGHT * 2.25 + UP * 1.55)

        life_words = word_cloud_reveal(["أهل", "ظروف", "قصة", "ألم", "حياة"])
        life_words.scale(0.78)
        for word in life_words:
            word.set_opacity(0.0)

        self.play(FadeIn(title, shift=UP * 0.12), FadeIn(name, shift=UP * 0.10), run_time=0.70)
        self.play(
            self.human.animate.scale(1.04).move_to(UP * 0.66),
            self.crater.animate.set_opacity(0.62),
            run_time=0.80,
            rate_func=smooth,
        )
        self.wait(1.15)
        self.play(FadeIn(left_label, shift=RIGHT * 0.12), FadeIn(right_label, shift=LEFT * 0.12), run_time=0.66)
        self.play(LaggedStart(*[word.animate.set_opacity(0.74) for word in life_words], lag_ratio=0.10), run_time=0.95)
        self.play(FadeIn(human_line, shift=UP * 0.14), run_time=0.78)
        self.wait(1.25)

        phone = phone_screen_container(width=4.60, height=8.45, accent=CYAN)
        phone.move_to(DOWN * 0.12)
        ghost = self.human.copy()
        ghost.scale(1.62)
        ghost.move_to(RIGHT * 2.45 + UP * 0.45)
        ghost.set_opacity(0.13)

        self.play(
            Create(phone),
            FadeIn(ghost, scale=0.96),
            self.human.animate.scale(0.74).move_to(phone[1].get_center() + UP * 0.02),
            self.crater.animate.set_opacity(0.12),
            run_time=1.05,
            rate_func=smooth,
        )
        self.play(
            FadeOut(ghost),
            FadeOut(title),
            FadeOut(name),
            FadeOut(left_label),
            FadeOut(right_label),
            FadeOut(life_words),
            FadeOut(human_line),
            FadeOut(self.crater),
            run_time=0.50,
        )
        self.content_phone = phone
        self.phone_human = self.human

    def scene_05_human_to_content(self) -> None:
        # VO:
        # "في السوشيال ميديا، الإنسان يتحول بسرعة إلى محتوى..."
        # "تعليق؟ لايك؟ مشاركة؟ كلها تبان بسيطة... بصح مرات تولي ضغط."
        # Duration target: 14.0s
        title = self.title("في الشاشة: محتوى", y=5.42, size=41, color=WHITE)
        outside = self.title("خارج الشاشة: إنسان", y=-5.45, size=36, color=GOLD)

        self.play(
            self.content_phone.animate.scale(0.84).move_to(UP * 0.20),
            self.phone_human.animate.scale(0.84).move_to(UP * 0.20),
            FadeIn(title, shift=UP * 0.10),
            run_time=0.82,
            rate_func=smooth,
        )
        

        metrics = VGroup(
            self.make_social_metric("لايك", CYAN),
            self.make_social_metric("تعليق", GOLD, width=1.55),
            self.make_social_metric("مشاركة", CYAN, width=1.70),
            self.make_social_metric("مشاهدة", RED, width=1.70),
        )
        metric_positions = [
            LEFT * 1.15 + UP * 2.52,
            RIGHT * 1.00 + UP * 1.95,
            LEFT * 1.10 + DOWN * 1.80,
            RIGHT * 1.05 + DOWN * 2.45,
        ]
        for metric, position in zip(metrics, metric_positions):
            metric.move_to(position)
            metric.set_z_index(12)

        self.play(LaggedStart(*[FadeIn(metric, shift=UP * 0.12) for metric in metrics], lag_ratio=0.14), run_time=1.05)
        self.play(LaggedStart(*[Indicate(metric, color=RED if index == 3 else GOLD, scale_factor=1.08) for index, metric in enumerate(metrics)], lag_ratio=0.10), run_time=1.25)
        self.wait(0.75)

        stones = VGroup()
        for index, metric in enumerate(metrics):
            stone = RoundedRectangle(
                width=0.76,
                height=0.48,
                corner_radius=0.08,
                stroke_color=RED,
                stroke_width=1.6,
                fill_color=RED,
                fill_opacity=0.18 + index * 0.04,
            )
            stone.rotate((index * 7 - 10) * DEGREES)
            stone.move_to(DOWN * (2.55 + index * 0.18) + LEFT * (0.52 - index * 0.35))
            stones.add(stone)

        
        pressure = safe_ar_text("مرات التفاعل يولي ضغط.", font_size=34, color=RED, weight="BOLD", max_width=6.5)
        pressure.move_to(DOWN * 4.05)

        self.play(
            ReplacementTransform(metrics.copy(), stones),
            self.content_phone.animate.shift(DOWN * 0.18),
            self.phone_human.animate.set_opacity(0.62),
            run_time=1.10,
            rate_func=smooth,
        )
        self.play(FadeIn(pressure, shift=UP * 0.10), run_time=0.60)
        self.wait(1.05)

        self.play(FadeIn(outside, shift=UP * 0.10), run_time=0.55)

        self.wait(1.05)

        self.content_title = title
        self.content_outside = outside
        self.metrics = metrics
        self.stones = stones
        self.pressure_text = pressure

    def scene_06_unseen_story(self) -> None:
        # VO:
        # "إحنا شفنا فيديو. ما شفناش حياتو."
        # "أنت شفت عشر ثواني... ما شفتش ثلاثين سنة."
        # Duration target: 17.0s
        self.play(
            FadeOut(self.metrics, shift=DOWN * 0.10),
            self.content_phone.animate.set_opacity(0.20).scale(0.98),
            self.phone_human.animate.set_opacity(0.18),
            self.stones.animate.set_opacity(0.20),
            FadeOut(self.content_title, shift=UP * 0.08),
            FadeOut(self.content_outside, shift=DOWN * 0.08),
            FadeOut(self.pressure_text, shift=DOWN * 0.08),
            run_time=0.72,
            rate_func=smooth,
        )

        headline = self.title("وش ما شفناش؟", y=5.42, size=42, color=WHITE)
        hidden_words = word_cloud_reveal(
            ["أهل", "ظروف", "فقر", "ألم", "موهبة بلا حماية", "حياة كاملة", "ضغط", "قصة"],
            colors=[GOLD, CYAN, SOFT_WHITE, RED],
        )
        hidden_words.set_z_index(8)
        center = safe_ar_text("شفنا فيديو...\nما شفناش حياتو.", font_size=45, color=WHITE, weight="BOLD", max_width=6.8)
        center.move_to(UP * 0.10)

        self.play(FadeIn(headline, shift=UP * 0.10), run_time=0.48)
        self.play(LaggedStart(*[FadeIn(word, scale=0.82) for word in hidden_words], lag_ratio=0.09), run_time=1.25)

        self.wait(3.05)
        self.play(FadeIn(center, shift=UP * 0.16), run_time=0.80)
        self.pulse_pause(center, color=GOLD, run_time=0.78)
        self.wait(1.25)

        ten = create_analysis_node("10 ثواني", color=RED, width=2.05)
        thirty = create_analysis_node("30 سنة", color=GOLD, width=2.05)
        ten.move_to(LEFT * 1.85 + DOWN * 3.65)
        thirty.move_to(RIGHT * 1.85 + DOWN * 3.65)
        connector = Line(ten.get_right(), thirty.get_left(), stroke_color=MUTED, stroke_width=2.0, stroke_opacity=0.36)
        self.play(FadeIn(ten, shift=UP * 0.10), Create(connector), FadeIn(thirty, shift=UP * 0.10), run_time=0.85)
        self.wait(1.80)

        scale_icon = create_scale_icon(scale=1.18)
        scale_icon.move_to(DOWN * 1.95)
        time_group = VGroup(ten, connector, thirty)
        self.play(
            ReplacementTransform(time_group.copy(), scale_icon),
            center.animate.set_opacity(0.26),
            hidden_words.animate.set_opacity(0.22),
            run_time=0.95,
            rate_func=smooth,
        )
        self.wait(0.55)

        self.unseen_headline = headline
        self.hidden_words = hidden_words
        self.unseen_center = center
        self.time_group = time_group
        self.scale_icon = scale_icon

    def scene_07_cruel_comment(self) -> None:
        # VO:
        # "اللي يكتب: مليح كي مات... لازم يوقف لحظة."
        # "تخيل أمو تقراها. تخيل خوتو يشوفوها."
        # Duration target: 14.0s
        self.play(
            FadeOut(self.content_phone),
            FadeOut(self.phone_human),
            FadeOut(self.stones),
            FadeOut(self.unseen_headline),
            FadeOut(self.hidden_words),
            FadeOut(self.unseen_center),
            FadeOut(self.time_group),
            self.scale_icon.animate.scale(0.70).to_edge(UP, buff=1.28).set_opacity(0.22),
            run_time=0.72,
            rate_func=smooth,
        )

        cruel_title = self.title("اللي يكتب هذي...", y=5.20, size=38, color=WHITE)
        bad = create_comment_bubble("مليح كي مات...", tone="harsh", width=6.45, font_size=35)
        bad.move_to(UP * 1.25)
        bad.set_z_index(12)
        pause = safe_ar_text("لازم يوقف لحظة.", font_size=42, color=GOLD, weight="BOLD", max_width=6.4)
        pause.move_to(DOWN * 0.55)

        family_words = VGroup(
            create_analysis_node("أمو تقراها", color=GOLD, width=2.22),
            create_analysis_node("خوتو يشوفوها", color=GOLD, width=2.45),
            create_analysis_node("أهلو يبحثو على دعوة", color=CYAN, width=3.05),
        )
        family_words.arrange(DOWN, buff=0.30)
        family_words.move_to(DOWN * 3.20)

        dead_line = safe_ar_text(
            "الميت ما يقدرش يرد.\nما يقدرش يقولك: هذه قصتي.",
            font_size=31,
            color=SOFT_WHITE,
            weight="BOLD",
            max_width=7.1,
        )
        dead_line.move_to(DOWN * 5.25)

        self.play(FadeIn(cruel_title, shift=UP * 0.12), run_time=0.45)
        self.play(FadeIn(bad, scale=0.86), run_time=0.74)
        self.play(Indicate(bad, color=RED, scale_factor=1.025), run_time=0.55)
        self.wait(0.60)
        self.play(FadeIn(pause, shift=UP * 0.12), run_time=0.62)
        self.play(LaggedStart(*[FadeIn(word, shift=UP * 0.12) for word in family_words], lag_ratio=0.18), run_time=1.05)
        self.wait(1.50)
        self.play(FadeIn(dead_line, shift=UP * 0.12), run_time=0.65)
        self.wait(1.20)

        self.cruel_title = cruel_title
        self.bad_comment = bad
        self.pause_text = pause
        self.family_words = family_words
        self.dead_line = dead_line

    def scene_08_mercy_reflection(self) -> None:
        # VO:
        # "ديننا ما علمناش نفرحو في موت الناس."
        # "الكلمة بعد الموت... أمانة."
        # Duration target: 15.0s
        self.play(
            FadeOut(self.cruel_title, shift=UP * 0.06),
            FadeOut(self.pause_text, shift=DOWN * 0.06),
            FadeOut(self.family_words, shift=DOWN * 0.08),
            FadeOut(self.dead_line, shift=DOWN * 0.08),
            FadeOut(self.scale_icon),
            run_time=0.45,
        )

        mercy = mercy_rewrite_transition(self, self.bad_comment, good_text="رحمه الله", position=UP * 2.05, font_size=58)
        amanah = safe_ar_text("الكلمة بعد الموت... أمانة.", font_size=43, color=WHITE, weight="BOLD", max_width=7.1)
        amanah.move_to(UP * 0.35)
        verse = safe_ar_text(
            "﴿مَا يَلْفِظُ مِنْ قَوْلٍ إِلَّا لَدَيْهِ رَقِيبٌ عَتِيدٌ﴾",
            font_size=28,
            color=GOLD,
            weight="BOLD",
            max_width=7.4,
        )
        verse.move_to(DOWN * 1.35)
        guidance = safe_ar_text(
            "ما نحكموش على القلوب من لقطة.\nربي وحدو يعلم واش كان في الداخل.",
            font_size=30,
            color=SOFT_WHITE,
            max_width=7.15,
        )
        guidance.move_to(DOWN * 3.45)

        self.play(FadeIn(amanah, shift=UP * 0.12), run_time=0.70)
        self.play(FadeIn(verse, shift=UP * 0.10), run_time=0.78)
        self.wait(1.50)
        self.play(FadeIn(guidance, shift=UP * 0.12), run_time=0.72)
        self.pulse_pause(mercy, color=GOLD, run_time=0.75)
        self.wait(1.20)

        cursor = Line(UP * 0.32, DOWN * 0.32, stroke_color=GOLD, stroke_width=4.0)
        cursor.move_to(DOWN * 4.78 + RIGHT * 2.90)
        self.play(
            FadeOut(amanah, shift=UP * 0.10),
            FadeOut(verse, shift=UP * 0.10),
            FadeOut(guidance, shift=DOWN * 0.10),
            mercy.animate.scale(0.58).move_to(DOWN * 4.78 + LEFT * 1.10),
            FadeIn(cursor),
            run_time=0.82,
            rate_func=smooth,
        )
        self.mercy_phrase = mercy
        self.comment_cursor = cursor

    def scene_09_before_comment(self) -> None:
        # VO:
        # "قبل ما تكتب تعليق، اسأل روحك..."
        # "هل نعرف قصتو؟ هل الكلمة رحمة ولا جرح؟"
        # Duration target: 15.0s
        comment_box = RoundedRectangle(
            width=7.35,
            height=1.05,
            corner_radius=0.18,
            stroke_color=GOLD,
            stroke_width=2.0,
            fill_color=SURFACE,
            fill_opacity=0.86,
        )
        comment_box.move_to(DOWN * 4.78)
        prompt = safe_ar_text("اكتب تعليقًا...", font_size=23, color=MUTED, max_width=4.0)
        prompt.move_to(comment_box.get_center() + LEFT * 1.20)

        title = self.title("قبل ما تحكم... اسأل.", y=5.35, size=42, color=GOLD)
        self.play(FadeIn(comment_box), FadeIn(prompt), self.comment_cursor.animate.move_to(comment_box.get_center() + RIGHT * 2.88), run_time=0.58)
        self.play(FadeIn(title, shift=UP * 0.12), run_time=0.62)

        questions = VGroup(
            create_analysis_node("هل نعرف قصتو؟", color=CYAN, width=3.0),
            create_analysis_node("هل نعرف واش عاش؟", color=CYAN, width=3.35),
            create_analysis_node("هل الكلمة رحمة ولا جرح؟", color=GOLD, width=4.2),
        )
        questions.arrange(DOWN, buff=0.38)
        questions.move_to(UP * 1.12)

        mother_line = safe_ar_text(
            "ولو كانت أمو تقرا التعليقات...\nهل كنت راح تكتب نفس الشي؟",
            font_size=34,
            color=WHITE,
            weight="BOLD",
            max_width=7.2,
        )
        mother_line.move_to(DOWN * 2.25)

        self.play(LaggedStart(*[FadeIn(question, shift=UP * 0.12) for question in questions], lag_ratio=0.17), run_time=1.15)
        self.wait(2.00)
        self.play(FadeIn(mother_line, shift=UP * 0.12), run_time=0.72)
        self.play(Indicate(questions[-1], color=GOLD, scale_factor=1.04), run_time=0.72)
        self.wait(1.25)

        self.comment_box = VGroup(comment_box, prompt, self.comment_cursor, self.mercy_phrase)
        self.before_title = title
        self.before_questions = questions
        self.mother_line = mother_line

    def scene_10_namat_reveal(self) -> None:
        # VO:
        # "القصة ماشي فقط قصة القعقاع. القصة قصتنا إحنا."
        # "كيفاش السوشيال ميديا مرات تنقص الرحمة فينا."
        # Duration target: 16.0s
        self.play(
            FadeOut(self.comment_box, shift=DOWN * 0.08),
            FadeOut(self.before_title, shift=UP * 0.08),
            FadeOut(self.mother_line, shift=DOWN * 0.08),
            self.before_questions.animate.scale(0.78).move_to(UP * 2.65).set_opacity(0.32),
            run_time=0.70,
            rate_func=smooth,
        )

        brand = safe_ar_text("نمط", font_size=76, color=GOLD, weight="BOLD", max_width=2.2)
        brand.move_to(UP * 4.70)
        title = safe_ar_text("القصة ماشي فقط قصة القعقاع.\nالقصة قصتنا إحنا.", font_size=38, color=WHITE, weight="BOLD", max_width=7.3)
        title.move_to(UP * 3.10)

        nodes = VGroup(
            create_analysis_node("حكم سريع", color=RED, width=2.15),
            create_analysis_node("تعليق قاسي", color=RED, width=2.35),
            create_analysis_node("خوارزمية", color=CYAN, width=2.10),
            create_analysis_node("رحمة ناقصة", color=GOLD, width=2.45),
            create_analysis_node("قصة مخفية", color=CYAN, width=2.35),
        )
        node_positions = [
            LEFT * 2.55 + UP * 0.95,
            RIGHT * 2.35 + UP * 0.70,
            LEFT * 2.25 + DOWN * 0.95,
            RIGHT * 2.15 + DOWN * 1.35,
            ORIGIN + DOWN * 0.12,
        ]
        for node, position in zip(nodes, node_positions):
            node.move_to(position)
        network_lines = line_network_transition(list(nodes), color=CYAN)

        reflection = safe_ar_text(
            "السوشيال ميديا عطتنا سرعة في الحكم...\nونقصت لنا الرحمة.",
            font_size=34,
            color=SOFT_WHITE,
            weight="BOLD",
            max_width=7.2,
        )
        reflection.move_to(DOWN * 4.42)

        self.play(FadeIn(brand, scale=0.85), FadeIn(title, shift=UP * 0.12), run_time=0.80)
        self.play(
            ReplacementTransform(self.before_questions, nodes),
            LaggedStart(*[Create(line) for line in network_lines], lag_ratio=0.10),
            run_time=1.15,
            rate_func=smooth,
        )
        self.wait(2.00)
        self.play(FadeIn(reflection, shift=UP * 0.12), run_time=0.72)
        self.play(ShowPassingFlash(network_lines.copy().set_stroke(GOLD, width=3.2, opacity=0.72), time_width=0.48), run_time=0.72)
        self.wait(1.35)

        self.namat_brand = brand
        self.namat_title = title
        self.namat_nodes = nodes
        self.namat_lines = network_lines
        self.namat_reflection = reflection

    def scene_11_final_hit_and_closing(self) -> None:
        # VO:
        # "أنت شفت النهاية... ما شفتش القصة."
        # "قبل ما تقول: علاه دار هك؟ قول: ربي يرحمو. وبعدها حاول تفهم."
        # Duration target: 12.0s before the Namat vertical closing.
        self.play(
            FadeOut(self.namat_brand, shift=UP * 0.08),
            FadeOut(self.namat_title, shift=UP * 0.08),
            FadeOut(self.namat_nodes, scale=0.95),
            FadeOut(self.namat_lines),
            FadeOut(self.namat_reflection, shift=DOWN * 0.08),
            run_time=0.70,
            rate_func=smooth,
        )

        mercy = safe_ar_text("رحم الله القعقاع.", font_size=38, color=GOLD, weight="BOLD", max_width=6.7)
        mercy.move_to(UP * 4.48)
        ending = safe_ar_text("أنت شفت النهاية...", font_size=47, color=WHITE, weight="BOLD", max_width=6.8)
        ending.move_to(UP * 1.60)
        story = safe_ar_text("ما شفتش القصة.", font_size=50, color=GOLD, weight="BOLD", max_width=6.8)
        story.move_to(UP * 0.42)

        before = create_comment_bubble("علاه دار هك؟", tone="harsh", width=4.25, font_size=30)
        before.move_to(DOWN * 1.72)
        after = create_comment_bubble("ربي يرحمو... وبعدها حاول تفهم.", tone="mercy", width=6.60, font_size=27)
        after.move_to(DOWN * 3.35)
        arrow = Arrow(
            before.get_bottom() + DOWN * 0.10,
            after.get_top() + UP * 0.10,
            stroke_width=3,
            color=GOLD,
            max_tip_length_to_length_ratio=0.16,
        )

        self.play(FadeIn(mercy, shift=UP * 0.12), run_time=0.58)
        self.play(FadeIn(ending, shift=UP * 0.14), run_time=0.72)
        self.play(FadeIn(story, shift=UP * 0.12), run_time=0.72)
        self.wait(0.70)
        self.play(FadeIn(before, scale=0.88), run_time=0.55)
        self.play(GrowArrow(arrow), FadeIn(after, shift=UP * 0.10), run_time=0.82)
        self.pulse_pause(after, color=GOLD, run_time=0.78)
        self.wait(1.35)

        final_group = VGroup(mercy, ending, story, before, arrow, after)
        self.play(final_group.animate.set_opacity(0.30).scale(0.96), run_time=0.45, rate_func=smooth)
        namat_signature_outro(self, clear_existing=True, seed=24)


# Render:
# manim -pqh projects/namat_spiderman_yemen_cinematic.py NamatSpidermanYemenCinematic
