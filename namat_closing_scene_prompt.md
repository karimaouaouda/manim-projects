# Codex Prompt — Professional Closing Scene for “نمط - Namat”

## Role
You are a senior Manim Community developer, motion designer, and brand animation specialist. Build a polished **closing scene / end card** for a social-analysis video brand called:

> **نمط - Namat**

The page targets an **Arabic audience** and analyzes social phenomena in a simple visual way, usually using Manim-style explanations. The closing scene must feel intelligent, calm, modern, and memorable — not loud, not childish, and not political.

---

## Main Goal
Create a reusable Manim closing scene that can be appended to the end of any video. It should visually communicate:

- social patterns,
- observation,
- analysis,
- clarity,
- and the idea that every phenomenon has an underlying pattern.

The scene should end with the brand name clearly visible:

> **نمط - Namat**

and the slogan:

> **كل ظاهرة لها نمط… وكل نمط له سبب**

Optional small CTA:

> **تابعنا لنفهم المجتمع ببساطة**

---

## Scene Duration
Total duration: **6 to 8 seconds**.

Recommended timeline:

| Time | Action |
|---:|---|
| 0.0s - 1.2s | Abstract social dots appear and form loose clusters. |
| 1.2s - 2.7s | Lines connect the dots, revealing hidden patterns. |
| 2.7s - 4.2s | A subtle scanning lens passes over the network and simplifies it. |
| 4.2s - 5.6s | The network transforms into a clean circular emblem / pattern mark. |
| 5.6s - 7.5s | Brand name, slogan, and CTA appear with calm motion. |

---

## Visual Style
Use a clean editorial / educational style inspired by modern explainer channels.

### Background
- Dark navy / deep charcoal background.
- Add a very subtle radial gradient or soft vignette.
- Add faint grid lines or tiny particles, but keep them minimal.
- Avoid busy backgrounds.

Suggested colors:

```python
BACKGROUND = "#0B1020"      # deep navy
PRIMARY = "#EAF2FF"         # near-white text
ACCENT = "#38BDF8"          # cyan-blue analysis color
SECONDARY = "#A7F3D0"       # soft green for pattern highlights
MUTED = "#64748B"           # slate gray
WARM = "#FBBF24"            # optional subtle golden accent
```

### Typography
Use fonts available on the system. Prefer:

- Arabic: `Cairo`, `Tajawal`, `Noto Kufi Arabic`, or `Noto Sans Arabic`.
- Latin: `Inter`, `Montserrat`, `Poppins`, or `Noto Sans`.

If the exact font is unavailable, fall back gracefully to `DejaVu Sans` or Manim default.

Arabic text must render correctly. Use `Text` or `MarkupText` rather than `Tex` for Arabic. Keep RTL text natural and readable.

---

## Composition
Use a **16:9 horizontal layout** by default.

Safe composition:

- Main emblem centered slightly above the vertical center.
- Brand name centered under the emblem.
- Slogan under the brand name.
- CTA very small at the bottom.

Final frame layout:

```text
          [abstract circular network / pattern emblem]

                    نمط - Namat
        كل ظاهرة لها نمط… وكل نمط له سبب

              تابعنا لنفهم المجتمع ببساطة
```

Keep all text inside safe margins. Do not place important text near the edges.

---

## Animation Concept
The closing scene should feel like a social phenomenon becoming understandable.

### Phase 1 — Social Noise
Create 20–35 small dots distributed around the center, not perfectly random but organic.

- Some dots represent individuals.
- Some dots represent ideas/trends.
- Make them appear with `FadeIn` and slight upward movement.
- Use low opacity for most dots.
- Highlight 4–6 dots with the accent color.

Motion feeling: quiet, curious, analytical.

### Phase 2 — Hidden Pattern Appears
Connect nearby dots with thin lines.

- Lines should appear progressively using `Create` or `LaggedStart`.
- Use low stroke opacity.
- Gradually make one main path brighter, suggesting that a hidden structure was discovered.
- Avoid making the network look like a tech startup logo; it should feel social and human.

### Phase 3 — Lens / Analysis Sweep
Add a subtle circular scanning lens.

Lens behavior:

- A translucent circle or ring moves from left to right across the network.
- As it passes, messy lines fade out and the meaningful pattern remains.
- Use `ShowPassingFlash`, `Circumscribe`, or a custom ring sweep.
- Add a very subtle glow to the discovered path.

Do not overdo glow effects. It must stay elegant.

### Phase 4 — Pattern Becomes Brand Mark
Transform the remaining network into a clean emblem.

Emblem idea:

- A circular arrangement of dots and lines.
- It can suggest the Arabic letter **ن** abstractly, but do not force it if it becomes ugly.
- It can also look like a simplified social-pattern map.
- The emblem should be reusable as a small logo mark.

Use `Transform`, `ReplacementTransform`, or `FadeTransformPieces` to morph from network to emblem.

### Phase 5 — Brand Reveal
Reveal the brand name:

> **نمط - Namat**

Animation:

- Fade in from slight blur/scale if possible.
- Use `FadeIn(shift=UP * 0.15)` or `Write` if Arabic renders smoothly.
- Keep the name large and centered.
- Color: primary text, with the dash or `Namat` slightly muted if desired.

Then reveal the slogan:

> **كل ظاهرة لها نمط… وكل نمط له سبب**

Animation:

- Smaller than brand name.
- Fade in softly after 0.25s delay.
- Use accent color for the word **نمط** if feasible using `MarkupText`.

Then reveal CTA:

> **تابعنا لنفهم المجتمع ببساطة**

Animation:

- Small and calm.
- Fade in at the bottom.
- Opacity around 0.75.

Final hold: 0.8–1.2 seconds.

---

## Audio / Sound Design Notes
Do not generate audio, but leave comments in the code where sound effects can be added later.

Suggested sound style:

- soft digital pulse when dots appear,
- very subtle whoosh during lens sweep,
- calm final chime when logo appears.

Add comments like:

```python
# Optional SFX: soft pulse here
# Optional SFX: subtle lens sweep whoosh here
# Optional SFX: warm final logo chime here
```

---

## Technical Requirements
Generate a clean, production-ready Manim Community scene.

### Class Name
Use:

```python
class NamatClosingScene(Scene):
```

### Compatibility
- Target Manim Community v0.19+ or v0.20+.
- Do not use deprecated APIs.
- Avoid external images unless absolutely necessary.
- Build the animation from vector objects: `Dot`, `Line`, `Circle`, `VGroup`, `Text`, `MarkupText`, etc.
- Make the scene deterministic by setting a random seed.

### Arabic Text Handling
Use `Text` or `MarkupText` for Arabic. Do not use `Tex`/`MathTex` for Arabic phrases.

Implement helper functions if needed:

```python
def arabic_text(content, font_size=48, color=WHITE, weight=NORMAL):
    return Text(
        content,
        font="Cairo",
        font_size=font_size,
        color=color,
        weight=weight,
    )
```

If `Cairo` is unavailable, allow fallback:

```python
ARABIC_FONT = "Cairo"
# If Cairo is not installed, replace with "Noto Sans Arabic", "Tajawal", or default.
```

### Responsiveness
The scene should remain readable if later adapted to:

- 16:9 YouTube videos,
- 9:16 TikTok/Reels/Shorts,
- 1:1 square posts.

For now, implement 16:9. Add comments explaining which constants to change for vertical format.

---

## Implementation Details
Use clear constants:

```python
DOT_COUNT = 28
SCENE_DURATION_TARGET = 7.0
BRAND_NAME = "نمط - Namat"
SLOGAN = "كل ظاهرة لها نمط… وكل نمط له سبب"
CTA = "تابعنا لنفهم المجتمع ببساطة"
```

Use helper methods:

```python
def create_social_network(self):
    ...

def create_lens(self):
    ...

def create_final_emblem(self):
    ...

def create_brand_texts(self):
    ...
```

Make the code readable and modular.

---

## Motion Quality Requirements
Use smooth easing:

- `smooth`
- `there_and_back`
- `ease_in_out_sine` if imported from rate functions

Avoid sudden linear movement. Every element should feel intentional.

Use staggered animation with `LaggedStart` where appropriate.

Recommended animation primitives:

- `FadeIn`
- `FadeOut`
- `Create`
- `Transform`
- `ReplacementTransform`
- `FadeTransform`
- `LaggedStart`
- `ShowPassingFlash`
- `Circumscribe`
- `Indicate`

---

## Camera and Framing
Use default camera unless needed.

No camera shake.
No aggressive zoom.
A very subtle scale-in of the final emblem is acceptable.

Final frame should be stable, clean, and screenshot-worthy.

---

## Deliverable
Return only the final Python code for the Manim scene, plus short instructions for running it.

Expected command:

```bash
manim -pqh namat_closing_scene.py NamatClosingScene
```

Also mention how to render transparent-background version if possible, but keep the default with dark background.

---

## Quality Checklist
Before returning the code, verify:

- Arabic text is readable and not reversed incorrectly.
- Brand name is exactly: `نمط - Namat`.
- Slogan is exactly: `كل ظاهرة لها نمط… وكل نمط له سبب`.
- Scene duration is around 6–8 seconds.
- Final screen is not cluttered.
- Text is inside safe margins.
- No external assets are required.
- Code is modular and easy to edit.
- Animation feels premium, calm, analytical, and suitable for social-media education content.

---

## Optional Advanced Enhancement
If time allows, add a small animated cursor-like line under the word **نمط**, as if the page is “underlining the pattern.” It should be very subtle and appear only once before the final hold.

Do not make it look like a YouTube subscribe animation. Keep it elegant and brand-centered.
