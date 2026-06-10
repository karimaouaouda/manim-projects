# Codex Task: Draw and Animate the “Namat - نمط” Thinking Character in Manim

## Goal
Create a **Manim vector character** inspired by the provided reference image of **Namat - نمط**. The character must feel like a **thinker, philosopher, analyzer, and idea-composer**, not a simple narrator or robot mascot.

The final output should be a Manim scene where the character appears on a **dark navy background**, is drawn with **clean white 2D vector strokes**, uses **small teal and golden accents**, and performs a simple **talking animation** that looks like the character is speaking/thinking during a video.

If an image reference is available, use it as the main visual guide:

```text
assets/namat_reference.png
```

The reference character is the selected design: a minimal abstract humanoid/philosopher with a round head, a spiral thought antenna, simple oval eyes, a golden abstract nose, a robe-like body, one hand on the chin, and subtle geometric/thinking symbols.

---

## Important Identity Rules
Do **not** create a generic cartoon, anime character, realistic person, robot, or mascot narrator.

The character must preserve these identity traits:

1. **Abstract philosopher look**
   - No realistic face details.
   - No realistic nose, eyebrows, hair, ears, or human anatomy.
   - The face should be symbolic and simple.

2. **Namat visual language**
   - Dark navy background.
   - Thin white outline strokes.
   - Golden-yellow abstract angular nose.
   - Teal/cyan accent elements.
   - Small orbiting/geometric thought symbols: dots, circle, triangle, square, tiny star, question mark, idea light.

3. **Thinker pose**
   - One hand should touch the chin.
   - The posture should suggest contemplation and analysis.
   - The character should look calm, curious, focused, and intelligent.

4. **Manim-friendly construction**
   - Draw everything with Manim primitives: `Circle`, `Ellipse`, `Arc`, `Line`, `VMobject`, `Dot`, `Polygon`, `VGroup`, `CubicBezier`, `ParametricFunction`, etc.
   - Avoid raster images except for optional reference comparison.
   - Keep the design simple enough to animate by changing shapes and moving groups.

---

## Required Visual Style
Use this palette:

```python
BG = "#061A33"          # deep navy background
WHITE = "#F7F7F2"       # warm white strokes
YELLOW = "#F6C445"      # philosophical nose / idea accents
TEAL = "#38D6C6"        # analysis / data / thought accents
TEAL_DARK = "#1D9EAA"   # secondary teal
SHADOW = "#020B16"      # soft grounding shadow
```

Stroke style:

```python
stroke_width_main = 5
stroke_width_detail = 3
stroke_width_symbol = 2.5
```

The character should have **almost no fill**. Most parts should be transparent or match the background, with visible white outlines.

---

## Character Geometry Specification
Build a reusable class named:

```python
class NamatThinker(VGroup):
```

The class should generate the character from subgroups so each part can be animated independently.

### 1. Head
- A simple round/oval head.
- Use a `Circle` or slightly stretched `Ellipse`.
- White stroke, no fill.
- Position: upper center of the character.
- It should be large enough to carry facial animation.

Approximate placement:

```python
head = Circle(radius=1.05)
head.set_stroke(WHITE, width=5)
head.set_fill(opacity=0)
head.move_to(UP * 1.0)
```

### 2. Spiral thought antenna
At the top of the head, create a small spiral-like curl, inspired by the reference.

It should look like a symbolic “thought sprout,” not hair.

Implementation options:
- Use `ParametricFunction` for a small spiral.
- Or use a small `Arc` plus a tiny `Dot` above it.

Required details:
- White spiral stroke.
- Tiny yellow dot at the top.
- Optional teal dot/circle near the spiral.

### 3. Eyes
- Two simple white vertical ovals.
- No pupils, no realistic eyes.
- The eyes should look thoughtful and calm.
- Add optional eyelid lines above them for thinking expression.

Approximate:

```python
left_eye = Ellipse(width=0.16, height=0.38)
right_eye = Ellipse(width=0.16, height=0.38)
```

### 4. Nose
The nose is the most important identity feature.

It must be:
- A **single golden-yellow angular line**.
- Abstract, almost like a bent line or small lightning-shaped profile.
- Not realistic.

Use a `VMobject` path with 3 points:

```python
nose = VMobject()
nose.set_points_as_corners([
    LEFT * 0.08 + UP * 1.20,
    RIGHT * 0.06 + UP * 0.90,
    LEFT * 0.08 + UP * 0.72,
])
nose.set_stroke(YELLOW, width=4)
```

### 5. Mouth
The mouth must be built as a separate subgroup so it can animate.

Create at least 4 mouth shapes:

```python
neutral_mouth   # small horizontal line
small_open      # small oval / short arc
wide_open       # larger oval or rounded rectangle
soft_smile      # small curved smile
```

The animation should switch between these shapes using `Transform` or `ReplacementTransform` to simulate talking.

The mouth should stay minimal, white or white + tiny yellow lower accent.

### 6. Body / robe
The body should look like a simple philosopher robe or abstract cloak, not a robot torso.

Use a `VMobject` outline shaped like a soft triangular robe:
- Narrow at neck.
- Wider at bottom.
- Slight curve on one side.
- No buttons.
- No shirt details.

The body can be a single curved white outline, inspired by the large character in the reference.

Suggested points:

```python
body = VMobject()
body.set_points_smoothly([
    LEFT * 0.55 + DOWN * 0.05,
    LEFT * 0.95 + DOWN * 1.0,
    LEFT * 0.75 + DOWN * 2.25,
    RIGHT * 0.75 + DOWN * 2.25,
    RIGHT * 0.95 + DOWN * 1.0,
    RIGHT * 0.55 + DOWN * 0.05,
])
body.set_stroke(WHITE, width=5)
body.set_fill(opacity=0)
```

Add a small golden spiral symbol on the chest, inspired by the Namat identity.

### 7. Arms and hands
The main pose must show the character thinking:

- One arm crosses the body.
- One hand touches the chin.
- The hand can be very simple: 2 or 3 rounded arcs / small circles.
- Keep it abstract and Manim-friendly.

Use curves, not realistic fingers.

Recommended subgroups:

```python
self.arm_support
self.arm_chin
self.hand_chin
```

The chin hand should be animated slightly upward/downward while talking, like the character is thinking while speaking.

### 8. Thought symbols
Create a small reusable function:

```python
def make_thought_symbols():
```

It should return a `VGroup` containing:
- Tiny teal triangle.
- Tiny white square.
- Small yellow dot.
- Small teal circle.
- Optional white star/spark.
- Optional `?` symbol near the head.

These symbols should float near the top/right of the character and subtly move/rotate.

Do not make the scene crowded. Keep it elegant.

---

## Required Animation Scene
Create a Manim scene named:

```python
class NamatTalkingTest(Scene):
```

### Scene behavior
The scene should demonstrate the character as if used in a video explaining an idea.

Timeline:

1. **Intro draw**
   - Background fades in.
   - Character is drawn using `Create` or `LaggedStart`.
   - Thought symbols appear with `FadeIn` and slight upward movement.

2. **Thinking idle**
   - Character performs small breathing/bobbing motion.
   - Spiral/dot gently moves.
   - Thought symbols float and rotate slowly.

3. **Talking animation**
   - Mouth cycles between neutral, small open, wide open, soft smile.
   - Chin hand moves very slightly.
   - Eyes blink once or twice.
   - Head makes tiny nods.
   - Thought symbols pulse softly when the character says an important idea.

4. **Analytical gesture**
   - One hand or side arm opens slightly.
   - A tiny graph/data icon appears near the character.
   - Then the hand returns to the chin pose.

5. **End pose**
   - Character returns to calm thinking expression.
   - Mouth becomes neutral/small smile.
   - Thought symbols settle.

---

## Talking Animation Requirements
The talking effect should not be voice-generated. It should be visual only.

Create a method inside `NamatThinker`:

```python
def get_mouth(self, mode: str) -> VMobject | VGroup:
```

Supported modes:

```python
"neutral"
"small_open"
"wide_open"
"smile"
```

Then create another method:

```python
def talk(self, scene: Scene, duration: float = 3.0):
```

This method should:
- Switch mouth shapes repeatedly.
- Use short random-looking timing, but deterministic code is fine.
- Use `Transform` or `ReplacementTransform`.
- Include subtle head movement.
- Include subtle chin-hand movement.

Example rhythm:

```python
mouth_sequence = [
    "small_open", "neutral", "wide_open", "small_open", "smile",
    "neutral", "small_open", "wide_open", "neutral"
]
```

Each mouth change should last around `0.12` to `0.22` seconds.

Do not make it too exaggerated. The character is thoughtful, not childish.

---

## Blinking Animation
Add a method:

```python
def blink(self, scene: Scene):
```

Blink by transforming the two oval eyes into short horizontal lines, then back to ovals.

Keep the blink fast:

```python
0.08 seconds close
0.10 seconds open
```

---

## File Structure
Create or update this file:

```text
scenes/namat_character_test.py
```

Expected structure:

```python
from manim import *

BG = "#061A33"
WHITE = "#F7F7F2"
YELLOW = "#F6C445"
TEAL = "#38D6C6"
TEAL_DARK = "#1D9EAA"
SHADOW = "#020B16"

class NamatThinker(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Build all subparts here.

    def get_mouth(self, mode: str):
        # Return mouth shape positioned correctly.

    def set_mouth(self, mode: str):
        # Replace current mouth.

    def blink(self, scene: Scene):
        # Eye blink animation.

    def talk(self, scene: Scene, duration: float = 3.0):
        # Mouth cycle + subtle motion.

class NamatTalkingTest(Scene):
    def construct(self):
        self.camera.background_color = BG
        namat = NamatThinker().scale(1.15).move_to(LEFT * 2.1 + DOWN * 0.1)
        # Animate drawing + talking test.
```

---

## Quality Requirements
Before finishing, check these points:

- The character still looks like the selected Namat reference.
- It looks like a philosopher/analyzer, not a robot.
- The shape is simple enough to reuse in many Manim videos.
- The mouth is separated and can animate independently.
- The eyes are separated and can blink.
- The thought symbols are separated and can float/pulse.
- The code is clean and reusable.
- The scene can render with:

```bash
manim -pqh scenes/namat_character_test.py NamatTalkingTest
```

---

## Optional Extra
Add a second scene named:

```python
class NamatPoseSheet(Scene):
```

This scene should show 3 small poses of the same character:

1. Thinking with hand on chin.
2. Explaining with one hand raised.
3. Analyzing with a small floating chart.

This helps verify that the character can be reused across future videos.

---

## Final Expected Result
A clean Manim implementation of the Namat character that can be reused as a talking character in educational/social-analysis videos.

The character should feel like:

> “A quiet abstract thinker who observes society, detects patterns, connects ideas, and explains them calmly.”

