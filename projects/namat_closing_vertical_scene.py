# -*- coding: utf-8 -*-
"""Standalone 9:16 closing scene for نمط - Namat.

Render from the project root:
    manim -pqh projects/namat_closing_vertical_scene.py NamatClosingVerticalScene

This version is designed for Reels, TikTok, Shorts, and other vertical formats.
"""

from __future__ import annotations

import sys
from pathlib import Path

from manim import *

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common import play_namat_closing


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30


class NamatClosingVerticalScene(Scene):
    """Vertical reusable end card for the Namat social-analysis brand."""

    def construct(self) -> None:
        play_namat_closing(self, clear_existing=False, seed=24)
