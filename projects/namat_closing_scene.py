# -*- coding: utf-8 -*-
"""Standalone 16:9 closing scene for نمط - Namat.

Render from the project root:
    manim -pqh projects/namat_closing_scene.py NamatClosingScene

Transparent-background export:
    manim -qh -t projects/namat_closing_scene.py NamatClosingScene

For vertical/social formats, change pixel/frame dimensions below to 1080x1920
and 9x16. The common animation automatically adapts its spacing to the frame.
"""

from __future__ import annotations

import sys
from pathlib import Path

from manim import *

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common import play_namat_closing


config.pixel_width = 1920
config.pixel_height = 1080
config.frame_width = 16
config.frame_height = 9
config.frame_rate = 30


class NamatClosingScene(Scene):
    """Professional reusable end card for the Namat social-analysis brand."""

    def construct(self) -> None:
        play_namat_closing(self, clear_existing=False, seed=24)
