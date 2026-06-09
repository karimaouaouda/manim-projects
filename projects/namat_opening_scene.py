# -*- coding: utf-8 -*-
"""Standalone vertical opening scene for نمط - Namat.

Render from the project root:
    manim -pqh projects/namat_opening_scene.py NamatOpeningScene

Horizontal export:
    Change pixel/frame dimensions below to 1920x1080 and 16x9.
"""

from __future__ import annotations

import sys
from pathlib import Path

from manim import *

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common import play_namat_opening


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30


class NamatOpeningScene(Scene):
    """Reusable intro: scattered social noise resolves into the Namat pattern."""

    def construct(self) -> None:
        play_namat_opening(self, clear_existing=False, seed=42)
