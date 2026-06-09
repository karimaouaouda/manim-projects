# -*- coding: utf-8 -*-
"""BAC DZ awareness video.

Render from the project root:
    manim -ql projects/bac_dz_awareness.py BACDzAwarenessVideo
    manim -qh projects/bac_dz_awareness.py BACDzAwarenessVideo
"""

from __future__ import annotations

from functools import lru_cache
import math
import sys
from pathlib import Path

import numpy as np
from manim import *

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@lru_cache(maxsize=1)

def _installed_fonts() -> set[str]:
    try:
        import manimpango

        return set(manimpango.list_fonts())
    except Exception:
        return set()

from common import (
    BG,
    CALM,
    MUTED,
    PRESSURE,
    SUCCESS,
    WHITE,
    YELLOW,
    create_card,
    create_glow_circle,
    create_paper,
    create_student_icon,
    fit_to_frame,
    make_ar_text,
    make_latin_text,
    play_namat_closing,
)


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30


class BACDzAwarenessVideo(MovingCameraScene):
    """A calm cinematic awareness message about BAC pressure in Algeria."""

    def construct(self) -> None:
        #self.register_fonts(ROOT / "assets" / "fonts" / "Amiri")
        self.setup_scene()
        self.scene_1_hook()
        self.scene_2_pressure()
        self.scene_3_grade_overload()
        self.scene_4_reality_check()
        self.scene_5_comparison()
        self.scene_6_solution()
        self.scene_7_final_message()
        play_namat_closing(self, clear_existing=False, seed=24)


    def register_fonts(self, fonts_dir: Path) -> None:
        print(f"Registering fonts from directory: {fonts_dir}")
        print(f"Found font files: {[font_file.name for font_file in fonts_dir.glob('*.ttf')]}")
        for font_file in fonts_dir.glob("*.ttf"):
            font_name = font_file.stem
            try:
                register_font(str(font_file))
                print(f"Registered font '{font_name}' from file '{font_file}'.")
            except ValueError:
                print(f"Warning: Could not register font '{font_name}' from file '{font_file}'.")
            except Exception as e:
                print(f"Error registering font '{font_name}' from file '{font_file}': {e}")

            # show the installed fonts after each registration attempt
            installed_fonts = _installed_fonts()
            print(f"Installed fonts: {sorted(installed_fonts)}")
    def setup_scene(self) -> None:
        self.camera.background_color = BG
        self.camera.frame.save_state()

    def fade_current(
        self,
        *except_mobjects: Mobject,
        run_time: float = 0.7,
        shift: np.ndarray = DOWN * 0.16,
    ) -> None:
        keep = set(except_mobjects)
        removable = [mobject for mobject in self.mobjects if mobject not in keep]
        if removable:
            self.play(FadeOut(Group(*removable), shift=shift), run_time=run_time)

    def pressure_phrase(self, content: str, font_size: float = 29) -> Mobject:
        if content == "mention":
            return make_latin_text("Mention?", font_size=font_size - 2, color=PRESSURE, weight="BOLD")
        return make_ar_text(content, font_size=font_size, color=PRESSURE, max_width=3.1)

    def bullet_row(
        self,
        content: str,
        color: str,
        font_size: float = 24,
        max_width: float = 2.95,
    ) -> VGroup:
        label = make_ar_text(content, font_size=font_size, color=WHITE, max_width=max_width)
        dot = Dot(radius=0.065, color=color)
        return VGroup(label, dot).arrange(RIGHT, buff=0.18)

    def comparison_bubble(self, content: str) -> VGroup:
        label = make_ar_text(content, font_size=24, color=WHITE, max_width=4.6)
        width = min(max(label.width + 0.72, 2.45), 5.4)
        bubble = RoundedRectangle(
            width=width,
            height=0.75,
            corner_radius=0.2,
            stroke_color=PRESSURE,
            stroke_width=2,
            fill_color=PRESSURE,
            fill_opacity=0.13,
        )
        label.move_to(bubble)
        return VGroup(bubble, label)

    def comparison_weight(self, color: str = PRESSURE) -> VGroup:
        rope = Line(UP * 0.34, UP * 0.02, stroke_color=color, stroke_width=2.4)
        body = RoundedRectangle(
            width=0.68,
            height=0.58,
            corner_radius=0.08,
            stroke_color=color,
            stroke_width=2.5,
            fill_color=color,
            fill_opacity=0.25,
        ).shift(DOWN * 0.25)
        return VGroup(rope, body)

    def final_bac_line(self) -> VGroup:
        bac = make_latin_text("BAC", font_size=43, color=CALM, weight="BOLD")
        ar_line = make_ar_text("مرحلة... ماشي نهاية الحياة", font_size=34, color=WHITE, max_width=5.7)
        line = VGroup(ar_line, bac).arrange(RIGHT, buff=0.22)
        return fit_to_frame(line, max_width=7.8)

    def scene_1_hook(self) -> None:
        # The opening is intentionally sparse: one word, one pulse, one short idea.
        self.wait(0.2)
        self.hook_pulse = create_glow_circle(radius=1.35, color=CALM)
        self.hook_pulse.set_z_index(-2)
        self.bac_word = make_latin_text("BAC", font_size=132, color=WHITE, weight="BOLD")
        self.hook_subtitle = make_ar_text("كلمة صغيرة... ضغط كبير", font_size=36, color=WHITE, max_width=7.2)
        self.hook_subtitle.next_to(self.bac_word, DOWN, buff=0.55)

        self.play(
            FadeIn(self.hook_pulse, scale=0.72),
            FadeIn(self.bac_word, scale=0.82),
            run_time=1.0,
        )
        self.play(
            self.camera.frame.animate.scale(0.93),
            self.hook_pulse.animate.scale(1.08),
            run_time=1.15,
            rate_func=smooth,
        )
        self.play(FadeIn(self.hook_subtitle, shift=UP * 0.14), run_time=0.75)
        self.play(Indicate(self.bac_word, color=CALM, scale_factor=1.035), run_time=0.7)
        self.wait(1.0)

    def scene_2_pressure(self) -> None:
        # Social phrases close in around the anchor word without overcrowding.
        self.play(FadeOut(self.hook_subtitle, shift=DOWN * 0.12), run_time=0.45)
        self.play(self.camera.frame.animate.scale(1.09), run_time=0.9)

        phrase_specs = [
            ("واش جبت؟", LEFT * 2.85 + UP * 4.45, 29),
            ("دخلت طب؟", RIGHT * 2.75 + UP * 4.25, 29),
            ("mention", LEFT * 3.0 + UP * 1.05, 28),
            ("وش قالو الناس؟", RIGHT * 3.0 + UP * 0.95, 26),
            ("ما تخيبناش", LEFT * 2.75 + DOWN * 3.7, 28),
            ("مستقبلك هنا", RIGHT * 2.75 + DOWN * 3.85, 28),
        ]
        phrases = VGroup()
        entrances = []
        for content, position, size in phrase_specs:
            phrase = self.pressure_phrase(content, font_size=size)
            phrase.move_to(position)
            phrase.set_z_index(4)
            phrases.add(phrase)
            entrances.append(FadeIn(phrase, shift=(-position / 12), scale=0.92))

        self.pressure_words = phrases
        self.play(LaggedStart(*entrances, lag_ratio=0.18), run_time=3.2)
        self.play(
            LaggedStart(
                *[phrase.animate.shift(-phrase.get_center() * 0.13) for phrase in phrases],
                lag_ratio=0.04,
            ),
            self.bac_word.animate.set_color(WHITE),
            run_time=1.7,
            rate_func=smooth,
        )
        self.play(
            LaggedStart(
                *[Indicate(phrase, color=YELLOW, scale_factor=1.03) for phrase in phrases],
                lag_ratio=0.08,
            ),
            run_time=1.25,
        )

        ring_radius = 2.25
        ring_moves = []
        for index, phrase in enumerate(phrases):
            angle = TAU * index / len(phrases) + PI / 8
            target = np.array([ring_radius * math.cos(angle), ring_radius * math.sin(angle), 0])
            ring_moves.append(phrase.animate.move_to(target).scale(0.82))
        self.play(
            LaggedStart(*ring_moves, lag_ratio=0.05),
            self.bac_word.animate.scale(0.86),
            self.hook_pulse.animate.scale(0.82),
            run_time=1.8,
        )
        self.wait(1.0)

    def scene_3_grade_overload(self) -> None:
        # The pressure ring becomes a paper that visually outweighs the student.
        student = create_student_icon(scale_factor=1.2, accent=YELLOW)
        student.move_to(DOWN * 3.0)
        paper = create_paper(width=3.55, height=4.35, accent=PRESSURE)
        paper.move_to(UP * 0.55)
        pressure_source = Group(self.hook_pulse, self.bac_word, self.pressure_words)

        self.play(
            ReplacementTransform(pressure_source, paper),
            FadeIn(student, shift=UP * 0.25),
            run_time=1.45,
        )

        marks = VGroup()
        mark_positions = [UP * 0.55, UP * 0.05, DOWN * 0.45]
        for mark, position in zip(("10/20", "14/20", "17/20"), mark_positions):
            mark_text = make_latin_text(mark, font_size=34, color=YELLOW, weight="BOLD")
            mark_text.move_to(paper.get_center() + position)
            marks.add(mark_text)
            self.play(FadeIn(mark_text, scale=0.85), run_time=0.32)
            self.play(Indicate(mark_text, color=PRESSURE, scale_factor=1.06), run_time=0.35)

        exam_group = VGroup(paper, marks)
        self.play(
            exam_group.animate.scale(1.16).move_to(DOWN * 0.15),
            student.animate.set_opacity(0.38).shift(DOWN * 0.1),
            run_time=1.65,
            rate_func=smooth,
        )
        self.wait(0.8)

        self.key_sentence = make_ar_text(
            "النقطة ما تلخّصش الإنسان",
            font_size=45,
            color=WHITE,
            weight="BOLD",
            max_width=7.65,
        )
        self.play(
            exam_group.animate.set_opacity(0.28),
            student.animate.set_opacity(0.22),
            FadeIn(self.key_sentence, shift=UP * 0.2),
            run_time=0.95,
        )
        self.play(Circumscribe(self.key_sentence, color=YELLOW, buff=0.18), run_time=1.05)
        self.wait(2.25)

    def scene_4_reality_check(self) -> None:
        # A balanced split: BAC has consequences, but it is not a verdict.
        self.fade_current(self.key_sentence, run_time=0.75)
        self.play(
            self.key_sentence.animate.to_edge(UP, buff=0.85).scale(0.62).set_color(MUTED),
            run_time=0.75,
        )

        panel_height = 7.3
        left_box = RoundedRectangle(
            width=4.05,
            height=panel_height,
            corner_radius=0.18,
            stroke_color=CALM,
            stroke_width=2.5,
            fill_color=CALM,
            fill_opacity=0.06,
        ).move_to(LEFT * 2.12 + DOWN * 0.18)
        right_box = RoundedRectangle(
            width=4.05,
            height=panel_height,
            corner_radius=0.18,
            stroke_color=SUCCESS,
            stroke_width=2.5,
            fill_color=SUCCESS,
            fill_opacity=0.06,
        ).move_to(RIGHT * 2.12 + DOWN * 0.18)

        left_title = VGroup(
            make_latin_text("BAC", font_size=31, color=CALM, weight="BOLD"),
            make_ar_text("يقدر يحدد:", font_size=25, color=WHITE, max_width=3.2),
        ).arrange(DOWN, buff=0.04)
        right_title = make_ar_text("بصح ما يحددش:", font_size=26, color=WHITE, weight="BOLD", max_width=3.35)
        left_title.move_to(left_box.get_top() + DOWN * 0.82)
        right_title.move_to(right_box.get_top() + DOWN * 0.82)

        left_rows = VGroup(
            self.bullet_row("الدخول للجامعة", CALM),
            self.bullet_row("بعض الاختيارات", CALM),
            self.bullet_row("أول طريق أكاديمي", CALM, font_size=23),
        ).arrange(DOWN, buff=0.58)
        right_rows = VGroup(
            self.bullet_row("ذكاءك كامل", SUCCESS),
            self.bullet_row("قيمتك الإجتاعية", SUCCESS),
            self.bullet_row("قدرتك على الإبداع", SUCCESS),
            self.bullet_row("مستقبلك كامل", SUCCESS, font_size=23),
        ).arrange(DOWN, buff=0.58)
        left_rows.move_to(left_box.get_center() + DOWN * 0.55)
        right_rows.move_to(right_box.get_center() + DOWN * 0.48)

        self.play(
            Create(left_box),
            Create(right_box),
            FadeIn(left_title, shift=UP * 0.12),
            FadeIn(right_title, shift=UP * 0.12),
            run_time=1.05,
        )

        visible_rows: list[Mobject] = []
        for row in left_rows:
            self.play(
                *[old.animate.set_opacity(0.55) for old in visible_rows],
                FadeIn(row, shift=UP * 0.12),
                run_time=0.58,
            )
            self.play(Indicate(row, color=CALM, scale_factor=1.025), run_time=0.35)
            visible_rows.append(row)

        self.wait(0.8)
        for row in right_rows:
            self.play(
                *[old.animate.set_opacity(0.55) for old in visible_rows],
                FadeIn(row, shift=UP * 0.12),
                run_time=0.58,
            )
            self.play(Indicate(row, color=SUCCESS, scale_factor=1.025), run_time=0.35)
            visible_rows.append(row)

        self.future_label = right_rows[-1][0]
        self.wait(3.0)

    def scene_5_comparison(self) -> None:
        # The last future item becomes a path, then comparison turns into weight.
        future_copy = self.future_label.copy()
        self.add(future_copy)
        path = Line(LEFT * 3.55, RIGHT * 3.55, stroke_color=CALM, stroke_width=6)
        path.move_to(DOWN * 2.35)
        to_fade = Group(*[mobject for mobject in self.mobjects if mobject is not future_copy])
        self.play(
            FadeOut(to_fade, shift=DOWN * 0.2),
            ReplacementTransform(future_copy, path),
            run_time=1.1,
        )

        student = create_student_icon(scale_factor=0.98, accent=CALM)
        student.move_to(path.get_start() + UP * 0.88)
        self.play(FadeIn(student, shift=UP * 0.2), run_time=0.65)
        self.play(student.animate.shift(RIGHT * 0.72), run_time=0.9)

        bubble_specs = [
            ("ولد فلان جاب 18", LEFT * 1.65 + UP * 3.65, 0.52),
            ("بنت خالتك دخلت طب", RIGHT * 1.25 + UP * 4.25, 0.42),
            ("جبت معدل 12؟", LEFT * 1.25 + UP * 2.55, 0.30),
            ("عاودت العام؟", RIGHT * 1.95 + UP * 2.75, 0.18),
        ]
        weights = VGroup()
        for index, (content, position, step) in enumerate(bubble_specs):
            bubble = self.comparison_bubble(content)
            bubble.move_to(position)
            self.play(FadeIn(bubble, shift=UP * 0.16), run_time=0.48)
            weight = self.comparison_weight()
            weight.move_to(student.get_center() + DOWN * (1.05 + index * 0.13) + LEFT * (0.24 - index * 0.11))
            move_old_weights = [weight_mob.animate.shift(RIGHT * step * 0.45 + DOWN * 0.03) for weight_mob in weights]
            self.wait(1.0)
            self.play(
                Transform(bubble, weight),
                student.animate.shift(RIGHT * step).scale(0.985),
                *move_old_weights,
                run_time=0.72,
            )
            weights.add(bubble)
            self.wait(0.18)

        self.comparison_label = make_ar_text(
            "المقارنة تقتل الثقة",
            font_size=45,
            color=PRESSURE,
            weight="BOLD",
            max_width=7.4,
        ).to_edge(UP, buff=1.45)
        self.play(FadeIn(self.comparison_label, shift=UP * 0.18), run_time=0.65)
        self.play(Circumscribe(self.comparison_label, color=PRESSURE, buff=0.18), run_time=0.95)
        self.wait(2.7)

        self.comparison_path = path
        self.comparison_student = student
        self.comparison_weights = weights

    def scene_6_solution(self) -> None:
        # Weights drop away, then support cards replace pressure with practical care.
        falling = [
            weight.animate.shift(DOWN * 2.15).set_opacity(0)
            for weight in self.comparison_weights
        ]
        self.play(
            LaggedStart(*falling, lag_ratio=0.08),
            FadeOut(self.comparison_label, shift=UP * 0.1),
            self.comparison_path.animate.set_color(SUCCESS).set_opacity(0.55),
            run_time=1.25,
        )
        self.remove(*self.comparison_weights)

        centered_student = create_student_icon(scale_factor=1.15, accent=SUCCESS)
        centered_student.move_to(UP * 3.35)
        self.play(
            Transform(self.comparison_student, centered_student),
            FadeOut(self.comparison_path),
            run_time=0.85,
        )

        cards = VGroup(
            create_card("نحضّرو بجدية", width=5.85, color=CALM),
            create_card("ما نقارنوش", width=5.85, color=SUCCESS),
            create_card("نساندو لي ما وفقش", width=5.85, color=CALM, font_size=29),
        ).arrange(DOWN, buff=0.36)
        cards.move_to(DOWN * 0.45)
        final_card = create_card(
            "نفرحو بالناجح... وما نكسروش لي تعثر",
            width=7.55,
            height=1.34,
            color=SUCCESS,
            font_size=27,
            fill_opacity=0.15,
        )
        final_card.next_to(cards, DOWN, buff=0.58)

        active_cards: list[Mobject] = []
        for card in cards:
            self.play(
                *[old.animate.set_opacity(0.58) for old in active_cards],
                FadeIn(card, shift=UP * 0.32),
                run_time=0.72,
            )
            self.play(Indicate(card[1], color=SUCCESS, scale_factor=1.2), run_time=0.36)
            active_cards.append(card)

        self.wait(1.1)

        self.play(
            *[old.animate.set_opacity(0.62) for old in active_cards],
            FadeIn(final_card, shift=UP * 0.32),
            run_time=0.9,
        )
        self.play(Circumscribe(final_card, color=SUCCESS, buff=0.12), run_time=0.85)
        self.wait(1.1)

        target_center = UP * 0.42
        protected_student = create_student_icon(scale_factor=1.18, accent=SUCCESS)
        protected_student.move_to(target_center)
        support_circle = Circle(radius=2.05, stroke_color=SUCCESS, stroke_width=3)
        support_circle.move_to(target_center)
        support_circle.set_stroke(opacity=0.72)

        support_items = VGroup(*cards, final_card)
        angles = [PI / 2, 5 * PI / 6, PI / 6, -PI / 2]
        card_moves = []
        for card, angle in zip(support_items, angles):
            target = target_center + np.array([1.86 * math.cos(angle), 1.86 * math.sin(angle), 0])
            card_moves.append(card.animate.scale(0.36).move_to(target).set_opacity(0.68))

        self.play(
            Transform(self.comparison_student, protected_student),
            Create(support_circle),
            LaggedStart(*card_moves, lag_ratio=0.05),
            run_time=1.45,
            rate_func=smooth,
        )
        self.wait(1.9)

        self.support_circle = support_circle
        self.support_items = support_items
        self.final_student = self.comparison_student

    def scene_7_final_message(self) -> None:
        # The ending equalizes the student and the exam, then leaves the message.
        final_student_target = create_student_icon(scale_factor=1.25, accent=SUCCESS)
        final_student_target.move_to(LEFT * 1.7 + UP * 2.75)
        bac_paper = create_paper(title="BAC", width=2.35, height=2.95, accent=CALM)
        bac_paper.move_to(RIGHT * 1.7 + UP * 2.75)

        other_objects = Group(
            *[
                mobject
                for mobject in self.mobjects
                if mobject is not self.final_student
            ]
        )
        self.play(
            FadeOut(other_objects, shift=DOWN * 0.15),
            Transform(self.final_student, final_student_target),
            FadeIn(bac_paper, shift=LEFT * 0.18),
            run_time=1.1,
        )

        main_line = self.final_bac_line()
        main_line.move_to(DOWN * 0.55)
        second_line = make_ar_text(
            "الإنسان أكبر من ورقة نقاط",
            font_size=31,
            color=WHITE,
            max_width=7.4,
        )
        second_line.next_to(main_line, DOWN, buff=0.45)
        signature = make_ar_text("رسالة مواطن", font_size=22, color=CALM)
        signature.next_to(second_line, DOWN, buff=0.55)
        underline = Line(LEFT * 1.65, RIGHT * 1.65, stroke_color=SUCCESS, stroke_width=3)
        underline.next_to(signature, DOWN, buff=0.34)

        self.play(FadeIn(main_line, shift=UP * 0.22), run_time=0.65)
        self.play(
            FadeIn(second_line, shift=UP * 0.14),
            FadeIn(signature, shift=UP * 0.12),
            Create(underline),
            run_time=0.85,
        )
        self.wait(2.75)
        self.play(FadeOut(Group(*self.mobjects), shift=DOWN * 0.16), run_time=1.2)
