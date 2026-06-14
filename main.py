# -*- coding: utf-8 -*-
"""Root render entry for available Manim project scenes.

Render:
    manim -pqh main.py NamatSpidermanYemenCinematic
    manim -pqh main.py ManimJourneyTeaser
"""

from projects.manim_journey_teaser import ManimJourneyTeaser
from projects.namat_spiderman_yemen_cinematic import NamatSpidermanYemenCinematic


__all__ = ["ManimJourneyTeaser", "NamatSpidermanYemenCinematic"]
