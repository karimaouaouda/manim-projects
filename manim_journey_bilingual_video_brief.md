# Manim Journey Video — Bilingual Visual Experiment Brief

## 1. Goal of the Video

Create a short, professional, cinematic Manim-based video that presents the creator's journey experimenting with **Manim** as a tool for turning abstract ideas into visual explanations.

The video must **not reveal any page name, brand name, final content niche, or exact project idea**. It should only show the experiment in an abstract, motivational way.

The core message:

> Code is not only for building apps.  
> Code can also explain ideas.

Arabic equivalent:

> الكود ليس فقط لبناء التطبيقات.  
> يمكنه أيضًا شرح الأفكار.

The final result should feel like a professional LinkedIn/TikTok/Instagram teaser about creative coding, visual learning, and engineering storytelling.

---

## 2. Video Style

### Visual Identity

Use a modern Manim style:

- Dark navy / deep blue background.
- White text as the main readable color.
- Accent colors: cyan, soft yellow/gold, light blue, and subtle green.
- Minimal shapes: circles, arrows, nodes, code panels, timeline lines, glowing dots.
- Smooth movement, not fast or chaotic.
- Professional, clean, and slightly cinematic.
- No cartoon mascot in this version.
- No logo or page name.
- No real project topic.

### Mood

The mood should be:

- Curious.
- Motivational.
- Intelligent.
- Engineering-oriented.
- Calm but inspiring.
- Like a “behind the experiment” video.

### Music

No voice-over.

Add motivational background music on top of the rendered video during editing/export.

Recommended music style:

- Soft cinematic tech music.
- Calm electronic / ambient motivation.
- No aggressive beat.
- Beat should support smooth transitions.
- Music volume should not overpower the visual rhythm.

If music is added programmatically or externally, keep it clean and license-safe.

---

## 3. Language Strategy

The video should include **both English and Arabic** for a wider audience.

Rules:

- English text appears first or slightly larger.
- Arabic text appears below it in a smaller but still readable size.
- Do not overload the screen with long paragraphs.
- Use short, powerful lines.
- Give each bilingual text enough time to be read.
- Arabic must be properly aligned and readable.
- If Arabic rendering in Manim is difficult, use a text image/SVG approach or a tested Arabic text rendering method.

Recommended layout:

```text
English main sentence
الجملة العربية المقابلة
```

Example:

```text
Can code explain ideas better than slides?
هل يمكن للكود أن يشرح الأفكار أفضل من الشرائح؟
```

---

## 4. Target Duration

Preferred duration: **35–45 seconds**.

Do not make the video too fast. Since there is no voice-over, the viewer needs enough time to read and understand each scene.

Approximate timing:

| Scene | Duration |
|---|---:|
| Scene 1 — Hook | 5s |
| Scene 2 — From Code to Motion | 7s |
| Scene 3 — Static vs Animated | 8s |
| Scene 4 — Learning Potential | 8s |
| Scene 5 — The Experiment Process | 8s |
| Scene 6 — Closing Question | 6s |
| Total | 42s |

---

## 5. Format and Export

Create the Manim script in a way that can be exported in multiple formats.

Primary format:

- **1080 × 1350** vertical-friendly LinkedIn/Instagram format, ratio 4:5.

Optional alternative:

- **1920 × 1080** landscape version, ratio 16:9.
- **1080 × 1920** vertical version, ratio 9:16.

For this first version, prioritize **4:5** because it works well on LinkedIn and social platforms.

Recommended render settings:

- 30 fps.
- High quality.
- MP4 output.
- Safe margins for mobile viewing.
- Text should never touch screen edges.

---

## 6. Global Design Rules

### Typography

Use clean sans-serif fonts.

Recommended:

- English: Inter, Poppins, Montserrat, or DejaVu Sans.
- Arabic: Cairo, Tajawal, Noto Kufi Arabic, or Noto Sans Arabic.

If a font is unavailable, use the closest readable fallback.

Text hierarchy:

- Main English line: large and bold.
- Arabic line: slightly smaller.
- Supporting labels: small, subtle opacity.

### Motion Rules

- Use easing for all movement.
- Avoid sudden jumps.
- Use fade, slide, morph, and line-draw animations.
- Let important text stay on screen for at least 2.5–3 seconds.
- Keep transitions elegant and meaningful.

### Color Rules

Suggested palette:

```python
BACKGROUND = "#07111F"
WHITE = "#F5F7FA"
MUTED = "#8EA4BD"
CYAN = "#38BDF8"
GOLD = "#FACC15"
GREEN = "#34D399"
BLUE = "#60A5FA"
RED_SOFT = "#FB7185"
```

Use glow effects subtly if possible.

---

## 7. Storyboard Overview

The story should move through this emotional path:

1. The creator did not want normal videos.
2. He started asking whether code can explain ideas.
3. He shows how code can create motion.
4. He compares static explanation with animated explanation.
5. He suggests educational value.
6. He ends with an open question that invites engagement.

Do not mention the specific future page, niche, or audience.

---

# 8. Detailed Scene-by-Scene Specification

---

## Scene 1 — The Hook

### Duration

5 seconds

### Purpose

Grab attention immediately. Make the viewer feel this is not another normal video project.

### Background

Dark navy background.

Start with a tiny glowing dot in the center. The dot expands into a small network of connected nodes, like an idea map forming.

### On-Screen Text

English:

```text
I didn’t want to make normal videos.
```

Arabic:

```text
لم أرد صنع فيديوهات عادية.
```

Then transform to:

English:

```text
I wanted to build explanations.
```

Arabic:

```text
أردت بناء شروحات تتحرك.
```

### Animation Direction

1. Start with black/dark background.
2. A small glowing dot appears in center.
3. Lines extend slowly from the dot to 4–5 smaller dots.
4. First bilingual text fades in above the network.
5. After 2 seconds, the first text dissolves into the second text.
6. The word **build** and the Arabic word **بناء** should briefly glow in cyan.

### Transition to Next Scene

The node network collapses into a thin horizontal line. That line becomes the top border of a code editor panel in Scene 2.

---

## Scene 2 — From Code to Motion

### Duration

7 seconds

### Purpose

Show that this experiment is based on code, not normal editing.

### Layout

Split-screen style:

- Left side: simplified Python/Manim code editor.
- Right side: animation preview area.

### On-Screen Text

Top-center:

English:

```text
What if ideas could move?
```

Arabic:

```text
ماذا لو استطاعت الأفكار أن تتحرك؟
```

Small label above left panel:

```text
Python + Manim
```

Small label above right panel:

```text
Visual Explanation
شرح بصري
```

### Code Snippet Visual

Show simplified pseudo-code, not real project code:

```python
idea = Circle()
question = Text("Why?")
self.play(Create(idea))
self.play(idea.animate.shift(RIGHT))
self.play(Transform(idea, explanation))
```

Important: The code does not need to fully compile visually. It is a visual metaphor.

### Animation Direction

1. Code panel slides in from the left.
2. Preview panel slides in from the right.
3. Lines of code type in quickly but elegantly.
4. Each important line triggers a visual action in the preview:
   - `Circle()` creates a circle.
   - `Text("Why?")` creates a small question mark.
   - `shift(RIGHT)` moves the circle.
   - `Transform` turns the circle into a connected diagram.
5. Add a subtle line connecting the code line to the visual output.

### Transition to Next Scene

The preview panel expands to full screen. The code panel fades away. The visual output freezes as a static diagram, preparing for the comparison in Scene 3.

---

## Scene 3 — Static vs Animated Explanation

### Duration

8 seconds

### Purpose

Show the value of animation compared to static explanation.

### Layout

Two-column comparison:

Left side:

```text
Static
ثابت
```

Right side:

```text
Animated
متحرك
```

### On-Screen Text

Center top:

English:

```text
Some concepts are hard to understand...
```

Arabic:

```text
بعض الأفكار يصعب فهمها...
```

Then:

English:

```text
until you see the process.
```

Arabic:

```text
إلى أن ترى العملية أمامك.
```

### Visual Design

Left side: static boxes and arrows, slightly dimmed.

Example:

```text
Idea → Step 1 → Step 2 → Result
```

Right side: same elements, but animated:

- Idea appears.
- Arrow is drawn.
- Step 1 appears.
- Arrow is drawn.
- Step 2 transforms.
- Result glows.

### Animation Direction

1. Show the left static diagram first. Keep it flat and slightly muted.
2. Draw a vertical divider line.
3. Show the right animated diagram.
4. Animate each step with smooth movement.
5. The right side should feel alive and clearer.
6. At the end, the right result node glows in gold.

### Transition to Next Scene

The animated diagram nodes float upward and rearrange into icons representing learning fields.

---

## Scene 4 — Learning and Teaching Potential

### Duration

8 seconds

### Purpose

Suggest educational use without sounding like a direct pitch.

### On-Screen Text

English:

```text
This could help people learn what static slides can’t show.
```

Arabic:

```text
قد يساعد الناس على فهم ما لا توضحه الشرائح الثابتة.
```

Then smaller text appears:

```text
Programming • Math • AI • Physics • Systems
البرمجة • الرياضيات • الذكاء الاصطناعي • الفيزياء • الأنظمة
```

### Visual Design

Create five minimal icons arranged in a circular orbit around a central glowing word:

Center word:

```text
Learning
التعلّم
```

Icons:

1. Programming: angle brackets `< />`.
2. Math: `∑` or graph curve.
3. AI: small neural network.
4. Physics: atom/orbit.
5. Systems: connected gears/nodes.

### Animation Direction

1. The nodes from Scene 3 become the five field icons.
2. Icons orbit slowly around the central word.
3. Each icon appears one by one with a small pulse.
4. Keep the movement slow and readable.
5. Do not make it look childish; keep it professional.

### Transition to Next Scene

The five icons collapse into a clean workflow timeline.

---

## Scene 5 — The Experiment Process

### Duration

8 seconds

### Purpose

Show the creator’s workflow abstractly: idea → scene → code → motion → learning.

### On-Screen Text

English:

```text
The hard part is not writing code.
```

Arabic:

```text
الصعب ليس كتابة الكود فقط.
```

Then:

English:

```text
The hard part is translating thought into motion.
```

Arabic:

```text
الصعب هو تحويل الفكرة إلى حركة.
```

### Workflow Timeline

Show this horizontal or vertical process:

```text
Idea → Scene → Code → Motion → Understanding
فكرة → مشهد → كود → حركة → فهم
```

### Animation Direction

1. Create five cards/nodes in a timeline.
2. Each card appears with a soft pop/fade.
3. Connect the cards with animated arrows.
4. The arrow between `Code` and `Motion` should glow because this is the core of Manim.
5. The final card `Understanding / فهم` should become slightly larger and brighter.
6. Add subtle background particles moving slowly.

### Transition to Next Scene

The final `Understanding / فهم` card zooms in and becomes the center of the closing scene.

---

## Scene 6 — Closing Question

### Duration

6 seconds

### Purpose

End with curiosity and engagement. Invite comments without revealing the final project.

### On-Screen Text

Main closing line:

English:

```text
Still experimenting.
```

Arabic:

```text
ما زلت أجرّب.
```

Second line:

English:

```text
But I think visual coding has a future in education.
```

Arabic:

```text
لكنني أؤمن أن للكود البصري مستقبلًا في التعليم.
```

Final engagement question:

English:

```text
Where do you think this can help most?
```

Arabic:

```text
أين تعتقد أن هذا الأسلوب يمكن أن يساعد أكثر؟
```

### Visual Design

- Centered text.
- Subtle glowing circular outline behind the text.
- Small animated particles move outward slowly.
- End with a clean fade to dark.

### Final Frame

Hold final question for at least 2 seconds.

Do not show logo.
Do not show page name.
Do not show social handle.

---

# 9. Suggested Manim Implementation Structure

Create a Python file named:

```text
manim_journey_teaser.py
```

Main class:

```python
class ManimJourneyTeaser(Scene):
    def construct(self):
        self.setup_style()
        self.scene_1_hook()
        self.scene_2_code_to_motion()
        self.scene_3_static_vs_animated()
        self.scene_4_learning_potential()
        self.scene_5_experiment_process()
        self.scene_6_closing_question()
```

Recommended helper functions:

```python
def bilingual_text(en, ar, en_size=42, ar_size=34, gap=0.25):
    """Return a VGroup with English text above Arabic text."""


def create_code_panel(lines):
    """Create a stylized code editor panel."""


def create_glow_dot(position, color):
    """Create a small glowing dot using circles with opacity."""


def create_icon(kind):
    """Return simple Manim icon for programming, math, AI, physics, systems."""


def smooth_replace(old, new):
    """Reusable replacement animation helper."""
```

---

# 10. Arabic Text Rendering Notes

Arabic text may not render correctly in default Manim text objects depending on system configuration.

Preferred options:

1. Use `Text` with a font that supports Arabic, such as `Cairo`, `Tajawal`, or `Noto Sans Arabic`.
2. If shaping is broken, use `MarkupText` carefully.
3. If Arabic still appears disconnected or reversed, generate Arabic text as SVG or PNG images and import them into Manim.
4. Keep Arabic phrases short to reduce rendering problems.

Arabic text must be visually correct before final export.

---

# 11. Detailed Animation Requirements

## Text Animations

Use:

- `FadeIn`
- `FadeOut`
- `Write`
- `TransformMatchingShapes`
- `ReplacementTransform`
- `LaggedStart`
- `AnimationGroup`

Avoid:

- Overusing `Write` for long text.
- Very fast text changes.
- Too many effects at once.

## Object Animations

Use:

- `Create` for lines, arrows, circles.
- `GrowFromCenter` for nodes.
- `Transform` for concept evolution.
- `MoveAlongPath` for orbit effects.
- `Indicate` or soft pulse for emphasis.

## Transitions

Use cinematic transitions:

1. Dot expands into network.
2. Network collapses into code panel border.
3. Preview panel expands to full screen.
4. Static diagram morphs into animated diagram.
5. Nodes rearrange into learning icons.
6. Icons collapse into workflow timeline.
7. Final understanding node zooms into closing question.

---

# 12. Timing and Readability Rules

Because there is no voice-over, readability is critical.

Rules:

- Main bilingual text should stay visible for at least 2.5 seconds.
- Do not show more than two bilingual lines at once unless they are labels.
- Leave enough empty space.
- Use slow camera movement only when it improves focus.
- Avoid fast cuts.
- Use music rhythm to support transitions, not control every frame.

---

# 13. Music Sync Suggestions

Since there is no voice-over, the animation should feel synchronized with music.

Use these music-inspired visual beats:

- Beat 1: first dot appears.
- Beat 2: network expands.
- Beat 3: code panel appears.
- Beat 4: visual preview reacts.
- Beat 5: static vs animated comparison appears.
- Beat 6: learning icons orbit.
- Beat 7: workflow timeline appears.
- Final beat: closing question appears and holds.

Do not make the movement too beat-heavy. Keep it professional.

---

# 14. Optional Opening Micro-Hook Variant

If a stronger first second is needed, start with this text for 1.5 seconds:

English:

```text
Can code teach?
```

Arabic:

```text
هل يمكن للكود أن يعلّم؟
```

Then transition into:

```text
I didn’t want to make normal videos.
لم أرد صنع فيديوهات عادية.
```

This version is more direct and may work better for social media.

---

# 15. Final Caption Compatibility

The video should be compatible with a LinkedIn post about:

- Learning in public.
- Creative coding.
- Manim experimentation.
- Visual teaching.
- Turning abstract ideas into motion.

Do not include any text in the video that conflicts with this positioning.

---

# 16. Things to Avoid

Do not include:

- Page name.
- Brand name.
- Logo.
- Social handle.
- Specific social analysis topic.
- Any political/social subject.
- Any religious/social message.
- Any final project reveal.
- Any voice-over.
- Any exaggerated hype like “revolutionary” or “the future is here.”
- Too much code on screen.
- Long paragraphs.
- Fast text transitions.

---

# 17. Expected Final Output

Codex should produce:

1. A clean Manim Python script.
2. A modular scene structure.
3. Bilingual English/Arabic on-screen text.
4. Smooth transitions.
5. Professional motion design.
6. Render-ready configuration for 4:5 format.
7. No voice-over.
8. A final MP4 video ready for motivational background music.

---

# 18. Suggested File Structure

```text
manim_journey_video/
│
├── manim_journey_teaser.py
├── assets/
│   ├── fonts/
│   ├── music/
│   └── optional_text_svgs/
│
├── renders/
│   └── final/
│
└── README.md
```

---

# 19. Final Creative Direction Summary

Build the video as a professional visual story about an experiment:

> A developer discovers that code can do more than execute logic.  
> It can organize thought, animate meaning, and help people understand complex ideas.

Arabic essence:

> مطوّر يكتشف أن الكود لا ينفّذ المنطق فقط،  
> بل يمكنه تنظيم الفكرة، وتحريك المعنى، ومساعدة الناس على الفهم.

Keep the result elegant, abstract, and mysterious.

The viewer should finish the video thinking:

> “This is interesting. What is he building next?”

