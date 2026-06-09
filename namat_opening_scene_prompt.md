# Codex Prompt — Professional Opening Scene for “نمط - Namat”

## 1. Role and Goal

You are a senior Manim developer and motion designer.  
Create a **professional opening scene** for a short-form Arabic social-analysis video brand called:

# **نمط - Namat**

The page analyzes **Arab society phenomena** in a simple, visual, thoughtful way, usually using Manim-style explanation.

The opening must feel:
- intelligent,
- modern,
- cinematic,
- calm but attractive,
- suitable for Facebook, Instagram Reels, TikTok, and YouTube Shorts,
- connected to the idea of “patterns behind social behavior.”

The scene should work as a reusable intro before any episode.

---

## 2. Core Brand Idea

The brand name is:

**نمط - Namat**

Meaning: **Pattern**.

The concept:
> Every social phenomenon has a hidden pattern.  
> The channel reveals that pattern in a simple visual way.

The opening should visually communicate:
1. Society is full of scattered events and reactions.
2. These events are not random.
3. Behind them, there is a pattern.
4. The pattern forms the brand name: **نمط - Namat**.

---

## 3. Scene Duration

Target duration: **6 to 8 seconds**.

Recommended timing:
- **0.0s – 1.5s:** scattered social signals appear.
- **1.5s – 3.5s:** signals connect and form pattern lines.
- **3.5s – 5.5s:** pattern compresses into the brand mark/name.
- **5.5s – 7.0s:** tagline appears and the scene transitions smoothly into the main video.

Keep it fast enough for social media, but not rushed.

---

## 4. Format and Aspect Ratios

The scene must support:
- **Vertical:** 1080x1920, primary target for Reels/TikTok/Shorts.
- **Horizontal:** 1920x1080, optional reusable version.
- **Square:** 1080x1080, optional.

Implement the Manim scene in a way that can easily adapt to different `config.frame_width` and `config.frame_height`.

Prefer vertical composition by default.

---

## 5. Visual Style

Use a premium dark theme.

### Background
Use a dark radial or subtle gradient-like background:
- Main background: very dark navy/charcoal.
- Suggested colors:
  - `#0B0F19`
  - `#111827`
  - `#020617`

Manim does not directly support CSS gradients by default, so simulate depth using:
- large low-opacity circles,
- translucent rectangles,
- soft glows,
- background grid dots,
- faint moving particles.

### Accent Colors
Use a controlled palette:
- Warm gold: `#F2C94C`
- Soft cyan: `#38BDF8`
- White: `#F8FAFC`
- Muted gray: `#94A3B8`
- Deep blue: `#1E293B`

Avoid overusing colors. The final brand must feel clean and serious.

---

## 6. Typography

Use Arabic-compatible text rendering.

Important:
- Use `Text` or `MarkupText` for Arabic, not `Tex`/`MathTex`.
- Make sure Arabic appears correctly right-to-left.
- Use a clean Arabic font if available, such as:
  - `Cairo`
  - `Tajawal`
  - `Noto Kufi Arabic`
  - `Noto Sans Arabic`
  - `Amiri`
- If the chosen font is not installed, fall back gracefully to Manim’s default font.

Primary title:
```text
نمط - Namat
```

Tagline:
```text
كل ظاهرة لها نمط
```

Optional second tagline:
```text
نفهم المجتمع… لا نحكم عليه
```

Prefer using only one tagline in the final animation to avoid clutter.

---

## 7. Opening Scene Concept

### Scene title
**From Noise to Pattern**

### Visual metaphor
Start with many small social “signals” spread around the screen:
- small dots,
- speech bubbles,
- tiny phone icons,
- heart/like symbols,
- warning symbols,
- small human silhouettes,
- small comment boxes,
- question marks,
- short Arabic words like:
  - ترند
  - رأي
  - عادة
  - ضغط
  - خوف
  - مقارنة
  - قطيع
  - مظهر

These signals should appear scattered, as if society is noisy and chaotic.

Then:
- dots slowly move,
- lines connect them,
- the random signals become a clean network,
- the network starts forming an abstract fingerprint/pattern shape,
- the fingerprint/pattern shape compresses or morphs into the brand name:
  **نمط - Namat**

The viewer should feel:
> “There is order behind the noise.”

---

## 8. Detailed Animation Sequence

### Phase 1 — Social Noise Appears
Duration: ~1.5 seconds

Create 12–20 small elements around the screen:
- dots,
- small outlined speech bubbles,
- small rectangles like social posts,
- short Arabic keywords.

Animation:
- use `FadeIn` with slight random shifts,
- each element appears with small delay using `LaggedStart`,
- use soft opacity, not full brightness,
- keep elements in the safe area, away from edges.

Motion:
- slight floating movement using `animate.shift(...)`,
- tiny rotations for rectangles,
- no chaotic fast movement.

Mood:
- mysterious,
- modern,
- “many things are happening.”

---

### Phase 2 — Hidden Connections
Duration: ~2 seconds

Create thin lines between selected dots/elements.

Animation:
- lines should draw progressively using `Create`.
- use cyan or muted blue lines with low opacity.
- connect items into a network/pattern.
- some keywords fade out as the structure becomes clearer.

Focus:
- guide the viewer’s eye toward the center.

Implementation idea:
- place invisible anchor points in a circular/spiral arrangement.
- animate scattered elements moving toward these anchor points.
- connect anchor points with lines.
- use `VGroup` to manage the whole network.

---

### Phase 3 — Pattern Formation
Duration: ~1.5 seconds

The connected network should become a recognizable abstract “pattern”:
- fingerprint-like curves,
- spiral network,
- geometric social graph,
- or nested lines.

Recommended style:
- A circular fingerprint-like pattern made with curved arcs.
- It should look like a “social behavior pattern,” not a literal logo.

Animation:
- transform scattered network into a centered pattern using `ReplacementTransform` or `Transform`.
- fade low-priority elements away.
- keep 3–5 small glowing nodes on the pattern.

The pattern should sit above or behind the title for a moment.

---

### Phase 4 — Brand Reveal
Duration: ~1.5 seconds

Reveal the title:

```text
نمط - Namat
```

Animation:
- pattern gently shrinks upward or behind the text.
- title appears from the center using:
  - `FadeIn(title, shift=UP * 0.15)`
  - or letter-by-letter reveal if stable.
- highlight the Arabic word **نمط** in warm gold.
- keep `Namat` in white or muted cyan.
- the hyphen/separator should be subtle gray.

Possible composition:
- Arabic title large and centered.
- `Namat` smaller but aligned visually.
- tagline below.

---

### Phase 5 — Tagline and Transition to Main Scene
Duration: ~1 second

Tagline:
```text
كل ظاهرة لها نمط
```

Animation:
- fade in gently under the title.
- use a small line or glow below it.
- after a short hold, transition to the main content by:
  - fading brand group upward,
  - or zooming into the pattern,
  - or using the central node as a transition circle.

End state:
- leave screen ready for first main scene.
- do not hard cut unless necessary.

---

## 9. Composition Rules

For vertical video:
- Keep the main brand title around vertical center.
- Keep particles and social signals mostly in the upper and middle areas.
- Do not place important text near the bottom 15% because social media UI may cover it.
- Keep safe margin around all sides.

Suggested layout:
- Top 20%: faint floating social signals.
- Middle 50%: pattern + title.
- Lower 20%: tagline.
- Bottom 10%: empty safe space.

---

## 10. Manim Implementation Requirements

Create a Manim class named:

```python
class NamatOpeningScene(Scene):
    ...
```

Use Manim Community Edition.

Expected imports:
```python
from manim import *
import numpy as np
import random
```

If using custom rate functions:
```python
from manim.utils import rate_functions
```

Recommended Manim tools:
- `Text`
- `MarkupText`
- `VGroup`
- `Dot`
- `Circle`
- `Line`
- `Arc`
- `RoundedRectangle`
- `FadeIn`
- `FadeOut`
- `Create`
- `Transform`
- `ReplacementTransform`
- `LaggedStart`
- `AnimationGroup`
- `MoveToTarget`
- `always_redraw` only if needed
- `rate_functions.ease_in_out_cubic`
- `smooth`

Avoid:
- overcomplicated SVG dependencies,
- external image files,
- fonts that are not guaranteed to exist,
- extremely dense objects that slow rendering.

---

## 11. Arabic Text Handling

Use `Text` or `MarkupText`.

Example:
```python
title_ar = Text("نمط", font="Cairo", font_size=72, color=GOLD)
title_en = Text("Namat", font="Cairo", font_size=38, color=WHITE)
```

If font problems occur:
- define a helper function:
```python
def safe_text(text, font_size=48, color=WHITE, font="Cairo"):
    try:
        return Text(text, font=font, font_size=font_size, color=color)
    except Exception:
        return Text(text, font_size=font_size, color=color)
```

Do not use `Tex` for Arabic brand text.

---

## 12. Suggested Visual Elements

### Social keywords
Use short words, not long sentences:
```python
keywords = [
    "ترند",
    "رأي",
    "عادة",
    "ضغط",
    "خوف",
    "مقارنة",
    "مظهر",
    "قطيع",
]
```

Render them small:
- `font_size=22` to `28`
- color: muted gray or soft cyan
- opacity: 0.45 to 0.75

### Social post cards
Create small rounded rectangles:
- width: 1.0 to 1.6
- height: 0.35 to 0.55
- stroke opacity low
- fill opacity around 0.08

Add small dots inside as fake text lines.

### Pattern nodes
Use dots:
- radius: 0.035 to 0.065
- cyan or gold
- some with glow circles behind them.

### Connection lines
Use:
- `Line(start, end)`
- stroke width: 1.0 to 1.8
- opacity: 0.25 to 0.55

---

## 13. Pattern Design Options

Choose one of these options:

### Option A — Network Pattern
Most reliable in Manim:
- scattered dots move into organized graph.
- graph becomes circular/spiral.
- title appears in center.

### Option B — Fingerprint Pattern
More premium:
- create 6–10 arcs with different radii.
- arcs have small gaps.
- dots sit on some arcs.
- this represents identity and hidden patterns.

### Option C — Lens Pattern
Connects to the old “under the lens” idea:
- network forms a circular lens outline.
- title appears inside the lens.
- a small scan line passes over the text.

Recommended: **Option B + small network elements**.

---

## 14. Opening Sound Design Notes

Do not generate audio unless requested, but structure the animation to fit sound.

Suggested sound feel:
- soft digital pulse when dots appear,
- subtle whoosh when lines connect,
- clean low hit when “نمط - Namat” appears,
- quiet shimmer when tagline appears.

Timing should leave space for a narrator voiceover to start after the intro.

---

## 15. Voiceover Compatibility

The opening should work with or without voiceover.

Optional short voiceover:
```text
كل ظاهرة لها نمط…
```

Then main video starts.

If voiceover is used, synchronize:
- “كل ظاهرة” with scattered society noise,
- “لها نمط” with pattern formation and logo reveal.

---

## 16. Transition into the Main Video

At the end, create one of these transition options:

### Preferred transition
The central glowing node expands into a full-screen dark overlay, then fades to the first scene title.

Implementation:
- create a small circle at center.
- animate it scaling up until it covers the whole frame.
- use it as a wipe transition.

### Alternative transition
The pattern lines stretch outward and become the first graph/diagram of the episode.

This is useful if the video starts directly with Manim explanation.

---

## 17. Quality Requirements

The result must:
- look premium and intentional,
- avoid childish icons,
- avoid too many colors,
- keep Arabic readable,
- keep motion smooth,
- keep object count reasonable,
- maintain visual hierarchy,
- work in vertical format,
- be reusable across episodes.

The scene should not feel like a generic logo animation.  
It should feel like the start of an intellectual visual essay.

---

## 18. Deliverable Expected from Codex

Generate:
1. A complete Manim Python file.
2. One scene class: `NamatOpeningScene`.
3. Clean helper functions for:
   - safe Arabic text,
   - background creation,
   - social signal creation,
   - network creation,
   - pattern arcs.
4. Clear comments explaining each section.
5. No external assets required.
6. The code should render without needing internet.

---

## 19. Suggested Code Architecture

Use this structure:

```python
from manim import *
import numpy as np
import random
from manim.utils import rate_functions


class NamatOpeningScene(Scene):
    def construct(self):
        self.camera.background_color = "#0B0F19"

        background = self.create_background()
        self.add(background)

        signals = self.create_social_signals()
        self.play_intro_noise(signals)

        network = self.create_network_from_signals(signals)
        self.play_network_reveal(signals, network)

        pattern = self.create_pattern_mark()
        self.play_pattern_transform(network, pattern)

        brand_group = self.create_brand_group()
        self.play_brand_reveal(pattern, brand_group)

        self.play_exit_transition(brand_group, pattern)

    def safe_text(self, text, font_size=48, color=WHITE, font="Cairo"):
        ...

    def create_background(self):
        ...

    def create_social_signals(self):
        ...

    def play_intro_noise(self, signals):
        ...

    def create_network_from_signals(self, signals):
        ...

    def play_network_reveal(self, signals, network):
        ...

    def create_pattern_mark(self):
        ...

    def play_pattern_transform(self, network, pattern):
        ...

    def create_brand_group(self):
        ...

    def play_brand_reveal(self, pattern, brand_group):
        ...

    def play_exit_transition(self, brand_group, pattern):
        ...
```

---

## 20. Important Creative Direction

Do not make it only a “logo reveal.”  
Make it tell a micro-story:

```text
ضجيج اجتماعي → روابط خفية → نمط واضح → نمط - Namat
```

This micro-story is the heart of the opening.

The final viewer emotion should be:
> “This page will help me understand what is behind what I see every day.”

---

## 21. Final Brand Frame

Final frame should show:

```text
نمط - Namat
كل ظاهرة لها نمط
```

Visual:
- title centered,
- subtle pattern behind or above it,
- small glow,
- clean dark background,
- no clutter.

Hold final frame for around **0.6 to 1.0 second** before transition.

---

## 22. Acceptance Checklist

Before finishing, verify:
- Arabic text is readable.
- Title is centered and balanced.
- The intro duration is 6–8 seconds.
- The scene is not overloaded.
- It works without external images.
- It visually communicates hidden social patterns.
- It ends smoothly into the first actual video scene.
- It uses `Text`/`MarkupText` for Arabic.
- It avoids `Tex`/`MathTex` for Arabic.
- It uses smooth transitions and professional timing.
