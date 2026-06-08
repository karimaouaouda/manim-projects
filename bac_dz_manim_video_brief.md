# Manim Video Production Brief — BAC في الجزائر: كلمة صغيرة، ضغط كبير

## 1. Project Goal
Create a modern, emotional, and educational Manim video explaining the social overpressure around the Algerian BAC exam. The video must be written in Algerian Arabic / Dz language, with a balanced message:

> **BAC مهم، بصح ماشي حكم نهائي على قيمة الإنسان.**

The video should feel like a citizen awareness message, not a school lecture. The tone is calm, cinematic, respectful, and socially conscious.

---

## 2. Target Audience
- Algerian students preparing for BAC.
- Parents and families.
- Teachers and society in general.
- Social media viewers on TikTok, Instagram Reels, YouTube Shorts, or Facebook.

---

## 3. Recommended Video Duration
**Target duration: 70–80 seconds**

This duration is enough to build emotion, explain the problem, and deliver a solution without becoming boring.

Suggested format:
- Vertical version: `1080x1920`, best for TikTok/Reels/Shorts.
- Horizontal version: `1920x1080`, best for YouTube or presentations.

If only one version is produced, prefer **vertical 9:16** because the message is social-media oriented.

---

## 4. Visual Style
Use a **modern cinematic minimal style**:

- Dark background at the beginning.
- Strong typography.
- Few colors, used meaningfully.
- Smooth zooms, fades, transforms, and motion blur style if possible.
- Avoid overcrowding the screen.
- Keep the viewer's eye guided to one main element at a time.

### Suggested Color Palette
Use these values or close alternatives:

```text
Background dark: #0B0F19
Text white: #F8FAFC
Muted gray: #94A3B8
Warning red/orange: #F97316
Calm blue: #38BDF8
Success green: #22C55E
Soft yellow: #FACC15
```

Do not use too many colors in the same scene. Use orange/red for pressure, blue/green for the solution.

---

## 5. Arabic / Latin Text Rendering Instructions
The video contains Arabic/Darija and Latin text such as `BAC`, `Mention`, and `Relevé de notes`. The agent must make sure text renders correctly.

### Required Fonts
Use fonts that support Arabic and Latin clearly:

- Arabic/Darija: `Noto Kufi Arabic`, `Noto Naskh Arabic`, `Amiri`, or `Cairo`.
- Latin: `Montserrat`, `Inter`, `Poppins`, or default sans-serif.

### Important RTL Instruction
If Arabic letters appear disconnected or reversed, use:

```bash
pip install arabic-reshaper python-bidi
```

Then create a helper function in the Manim script:

```python
import arabic_reshaper
from bidi.algorithm import get_display

def ar(text: str) -> str:
    return get_display(arabic_reshaper.reshape(text))
```

Use this helper for every Arabic/Darija string:

```python
Text(ar("الباك مرحلة، ماشي نهاية الحياة"), font="Noto Kufi Arabic")
```

For mixed text like `BAC مرحلة`, either separate Latin and Arabic into different `Text` objects or test carefully. Recommended:

- Put `BAC` as a separate Latin `Text` object.
- Put Arabic/Darija as separate Arabic `Text` object.

---

## 6. Audio / Voiceover Instructions
The voiceover should be human and emotional. Prefer real recorded voice over TTS.

Voice style:
- Algerian Darija.
- Calm and serious.
- Not aggressive.
- Speak as a citizen.
- Slight pause after strong sentences.

Recommended background audio:
- Very low cinematic ambient pad.
- No loud music.
- Add subtle whoosh sounds for transitions if possible.

If using Manim Voiceover, structure scenes using `VoiceoverScene`. If not, create animation timings according to the durations below and sync manually later.

---

## 7. Main Video Message
The video should deliver this idea clearly:

1. BAC is important.
2. Society sometimes makes it heavier than it should be.
3. Notes are useful, but they do not define the whole person.
4. The solution is respect, support, and less comparison.
5. BAC is a step, not the end of life.

---

# 8. Full Scene-by-Scene Script

## Scene 0 — Technical Setup
**Duration:** not visible

### Manim Setup Notes
Create constants:

```python
BG = "#0B0F19"
WHITE = "#F8FAFC"
MUTED = "#94A3B8"
PRESSURE = "#F97316"
CALM = "#38BDF8"
SUCCESS = "#22C55E"
YELLOW = "#FACC15"
```

Use a dark background:

```python
self.camera.background_color = BG
```

Use helper functions:

- `make_ar_text(content, size=...)`
- `make_latin_text(content, size=...)`
- `focus_on(mobject)` using subtle scale or spotlight effect.

---

## Scene 1 — Cold Hook: One Word
**Duration:** 0:00–0:06  
**Goal:** Capture attention immediately.

### Visual
Start with a black/dark screen. Nothing appears for 0.3 seconds.

Then one word appears in the center:

```text
BAC
```

The word should be very large, bold, and white. Use a Latin font like Montserrat ExtraBold.

Animation sequence:
1. `FadeIn(BAC, scale=0.8)`
2. Very slow zoom-in.
3. A thin glowing circle or pulse appears behind the word.
4. Hold silence for half a second.

### Voiceover
```text
BAC...
```

Pause 0.5 seconds.

```text
كلمة صغيرة... بصح ضغط كبير.
```

### On-screen Text
Only show:

```text
BAC
```

Then, under it, small Arabic subtitle appears:

```text
كلمة صغيرة... ضغط كبير
```

### Focus Direction
Viewer must focus only on the word `BAC`. Do not add other elements yet.

### Transition to Next Scene
The word `BAC` remains in the center. Around it, pressure words will start appearing.

---

## Scene 2 — The Pressure Around One Word
**Duration:** 0:06–0:16  
**Goal:** Show how society surrounds BAC with fear and expectations.

### Visual
Keep `BAC` in the center.

Around it, short pressure phrases appear one by one, like social voices coming from different directions:

```text
واش جبت؟
دخلت طب؟
جبت Mention؟
وش قالو الناس؟
ما تخيبناش
مستقبلك هنا
```

Each phrase appears quickly, then moves slightly toward the center, as if pressure is closing in.

Use different sizes but keep them readable. Do not let them overlap too much.

Suggested layout:
- Top left: `واش جبت؟`
- Top right: `دخلت طب؟`
- Left: `جبت Mention؟`
- Right: `وش قالو الناس؟`
- Bottom left: `ما تخيبناش`
- Bottom right: `مستقبلك هنا`

Animate with:
- `FadeIn`
- `LaggedStart`
- slight shake or vibration
- orange/red color for pressure words

### Voiceover
```text
في الجزائر، كي تسمع BAC، ساعات الدار كامل تبدّل جوّها.
العائلة، الجيران، المدرسة، والسوشيال ميديا... كامل يزيدو في الضغط.
```

### On-screen Text
Pressure phrases only. Do not add long subtitles.

### Focus Direction
The central `BAC` must remain the anchor. The pressure phrases should orbit or surround it, not distract randomly.

### Transition to Next Scene
Pressure words compress into a circular ring around `BAC`. Then the ring transforms into a heavy exam paper.

---

## Scene 3 — BAC Becomes Too Heavy
**Duration:** 0:16–0:27  
**Goal:** Show the exaggeration: an important exam becomes a life judgment.

### Visual
The pressure ring morphs into a large paper icon labeled:

```text
Relevé de notes
```

Then a simple student icon appears under it. The paper slowly becomes larger and starts covering the student.

Use simple shapes:
- Student: circle head + body line, or simple SVG-style icon built with Manim shapes.
- Paper: rounded rectangle with small horizontal lines.

The paper displays marks:

```text
10/20
14/20
17/20
```

These numbers flash one after another.

### Voiceover
```text
المشكل ماشي في الامتحان بحد ذاتو.
المشكل كي نكبّروه حتى يولي حكم على الإنسان.
نولّيو نسقسو: شحال جاب؟ واش دخل؟ جاب Mention؟
وننساو نسقسو: هل راه مليح؟ هل راه بخير؟
```

### On-screen Text
After the paper covers the student, show one strong sentence:

```text
النقطة ما تلخّصش الإنسان
```

Keep this sentence centered and large.

### Focus Direction
During this scene, the viewer should first focus on the student, then the paper, then the sentence. Use dimming: when the sentence appears, fade the background elements to 35% opacity.

### Transition to Next Scene
The sentence `النقطة ما تلخّصش الإنسان` stays on screen. Then split it into two sides: reality vs exaggeration.

---

## Scene 4 — Balanced Reality Check
**Duration:** 0:27–0:43  
**Goal:** Be fair: BAC matters, but it does not define everything.

### Visual
Create a clean split-screen layout.

Left panel title:

```text
BAC يقدر يحدد:
```

Left items:

```text
الدخول للجامعة
بعض الاختيارات
أول طريق أكاديمي
```

Right panel title:

```text
بصح ما يحددش:
```

Right items:

```text
قيمتك
ذكاءك كامل
إبداعك
مستقبلك كامل
```

Use two rounded rectangles:
- Left panel: calm blue border.
- Right panel: soft green border.

Animate items one by one with check icons or small dots.

### Voiceover
```text
نعم، BAC مهم.
يفتح باب الجامعة، ويوجّه أول خطوة أكاديمية.
بصح ما يحددش قيمتك، ما يقيسش ذكاءك كامل، وما يكتبش مستقبلك كامل.
```

### On-screen Text
Keep the split-screen content readable. Do not add extra subtitles.

### Focus Direction
Guide the viewer item by item. While one item appears, slightly brighten that item and keep others muted.

### Transition to Next Scene
The right panel phrase `ما يكتبش مستقبلك كامل` transforms into a road/path line.

---

## Scene 5 — The Real Problem: Comparison Culture
**Duration:** 0:43–0:57  
**Goal:** Identify the social problem clearly: comparison, shame, and fear.

### Visual
A horizontal path appears from left to right. A student walks or moves along the path.

Above the path, comparison bubbles appear:

```text
ولد فلان جاب 18
بنت خالتك دخلت طب
راك غير 12؟
عاودت؟
```

Each bubble appears, then turns into a small weight attached to the student.

The student slows down visually.

Then a large label appears:

```text
المقارنة تقتل الثقة
```

### Voiceover
```text
لي يوجع أكثر من الامتحان، هو المقارنة.
ولد فلان، بنت فلان، شكون جاب أكثر، وشكون دخل تخصص أحسن.
هنا الضغط يتحوّل من تحفيز... لخوف وشعور بالنقص.
```

### On-screen Text
Main sentence only:

```text
المقارنة تقتل الثقة
```

### Focus Direction
Use the student as the emotional center. The comparison bubbles should appear one at a time, then fade slightly after becoming weights.

### Transition to Next Scene
The weights fall down and disappear. The student stands straight again. The background becomes calmer.

---

## Scene 6 — The Solution: Respect Without Pressure
**Duration:** 0:57–1:12  
**Goal:** Give a constructive solution.

### Visual
Show three clean cards appearing one by one:

Card 1:
```text
نحضّرو بجدية
```

Card 2:
```text
ما نقارنوش
```

Card 3:
```text
نساندو لي ما وفقش
```

Then a fourth final card appears larger:

```text
نفرحو بالناجح... وما نكسروش لي تعثر
```

Visual style:
- Calm blue/green tones.
- Cards slide up smoothly.
- Use check icons or simple line icons.

### Voiceover
```text
الحل ماشي أننا ننقصو من قيمة BAC.
الحل أننا نحطّوه في بلاصتو الصحيحة.
نحضّرو بجدية، بصح بلا رعب.
نفرحو بالناجح، ونوقفو مع لي ما وفقش.
```

### On-screen Text
Show the cards. Do not overload with full voiceover text.

### Focus Direction
Each card should appear in sync with the voiceover. Keep previous cards visible but slightly dimmed when a new card appears.

### Transition to Next Scene
Cards move together and form a protective circle around the student.

---

## Scene 7 — Citizen Message / Emotional Conclusion
**Duration:** 1:12–1:20  
**Goal:** End with a memorable citizen statement.

### Visual
The word `BAC` returns, but now normal-sized, placed beside the student, not above him.

Layout:
- Student icon center-left.
- BAC paper center-right.
- Both are equal height or the student slightly taller.

This symbolizes: the student is not under the exam; the exam is only one part of life.

Final sentence appears in the center:

```text
BAC مرحلة... ماشي نهاية الحياة
```

Under it, smaller:

```text
رسالة مواطن
```

### Voiceover
```text
كمواطن، رسالتي بسيطة:
BAC مرحلة... ماشي نهاية الحياة.
النقطة مهمة، بصح الإنسان أكبر من ورقة نقاط.
```

### On-screen Text
Main final text:

```text
BAC مرحلة... ماشي نهاية الحياة
```

Small text:

```text
الإنسان أكبر من ورقة نقاط
```

### Focus Direction
End cleanly. No extra objects. The final sentence must be the strongest visual memory.

### Transition / Outro
Fade out slowly to dark background.

---

# 9. Complete Voiceover Script in Algerian Darija

Use this as the final narration. It should be recorded naturally, with pauses.

```text
BAC...
كلمة صغيرة... بصح ضغط كبير.

في الجزائر، كي تسمع BAC، ساعات الدار كامل تبدّل جوّها.
العائلة، الجيران، المدرسة، والسوشيال ميديا... كامل يزيدو في الضغط.

المشكل ماشي في الامتحان بحد ذاتو.
المشكل كي نكبّروه حتى يولي حكم على الإنسان.
نولّيو نسقسو: شحال جاب؟ واش دخل؟ جاب Mention؟
وننساو نسقسو: هل راه مليح؟ هل راه بخير؟

نعم، BAC مهم.
يفتح باب الجامعة، ويوجّه أول خطوة أكاديمية.
بصح ما يحددش قيمتك، ما يقيسش ذكاءك كامل، وما يكتبش مستقبلك كامل.

لي يوجع أكثر من الامتحان، هو المقارنة.
ولد فلان، بنت فلان، شكون جاب أكثر، وشكون دخل تخصص أحسن.
هنا الضغط يتحوّل من تحفيز... لخوف وشعور بالنقص.

الحل ماشي أننا ننقصو من قيمة BAC.
الحل أننا نحطّوه في بلاصتو الصحيحة.
نحضّرو بجدية، بصح بلا رعب.
نفرحو بالناجح، ونوقفو مع لي ما وفقش.

كمواطن، رسالتي بسيطة:
BAC مرحلة... ماشي نهاية الحياة.
النقطة مهمة، بصح الإنسان أكبر من ورقة نقاط.
```

---

# 10. Shorter Voiceover Version for 45–55 Seconds

If the generated video feels too long, use this shorter script:

```text
BAC...
كلمة صغيرة... بصح ضغط كبير.

في الجزائر، BAC ماشي غير امتحان.
ساعات يولي خوف، مقارنة، وحكم على الإنسان.

نسقسو: شحال جاب؟ دخل طب؟ جاب Mention؟
وننساو نسقسو: هل راه بخير؟

نعم، BAC مهم.
يفتح باب الجامعة، ويوجّه أول طريق أكاديمي.
بصح ما يحددش قيمتك، ما يقيسش ذكاءك كامل، وما يكتبش مستقبلك كامل.

المشكل ماشي في الامتحان.
المشكل في الضغط والمقارنة.

الحل؟
نحضّرو بجدية، بلا رعب.
نفرحو بالناجح، ونساندو لي ما وفقش.

BAC مرحلة... ماشي نهاية الحياة.
والإنسان أكبر من ورقة نقاط.
```

---

# 11. Scene Timing Table

| Scene | Time | Duration | Main Idea | Visual Focus |
|---|---:|---:|---|---|
| 1 | 0:00–0:06 | 6s | Hook | One word: BAC |
| 2 | 0:06–0:16 | 10s | Pressure | Social phrases around BAC |
| 3 | 0:16–0:27 | 11s | Overrating | Student covered by grades |
| 4 | 0:27–0:43 | 16s | Reality check | BAC decides vs does not decide |
| 5 | 0:43–0:57 | 14s | Comparison culture | Student carrying comparison weights |
| 6 | 0:57–1:12 | 15s | Solution | Supportive cards |
| 7 | 1:12–1:20 | 8s | Final message | BAC beside student |

Total: **~80 seconds**

---

# 12. Manim Animation Details

## Text Animation Style
Use kinetic typography but not too much.

Recommended animations:

```python
FadeIn(text, shift=UP * 0.2)
Write(text)
TransformMatchingShapes(old_text, new_text)
LaggedStart(*animations, lag_ratio=0.15)
```

Avoid excessive rotations or chaotic movement.

## Camera / Focus Effects
Use subtle camera movement:

- Slow zoom on `BAC` in Scene 1.
- Slight zoom out in Scene 2 when pressure words appear.
- Spotlight/dimming in Scene 3 when final sentence appears.
- Static clean layout in Scene 4.
- Calm fade and centered composition in final scene.

If using `MovingCameraScene`, keep movements slow and meaningful.

## Shape Language
Use simple symbolic elements:

- BAC: large typography.
- Student: circle + line body, simple icon.
- Pressure: arrows, bubbles, labels.
- Notes: paper rectangle with numbers.
- Solution: rounded cards.

No complex characters are required.

---

# 13. Suggested Manim Object Design

## BAC Text
```python
bac = Text("BAC", font="Montserrat", weight=BOLD, font_size=110, color=WHITE)
```

## Arabic Text
```python
txt = Text(ar("كلمة صغيرة... ضغط كبير"), font="Noto Kufi Arabic", font_size=42, color=WHITE)
```

## Student Icon
Build using simple shapes:

```python
head = Circle(radius=0.25, color=WHITE)
body = Line(ORIGIN, DOWN * 0.7, color=WHITE)
arms = Line(LEFT * 0.35, RIGHT * 0.35, color=WHITE)
legs = VGroup(
    Line(DOWN * 0.7, DOWN * 1.1 + LEFT * 0.25, color=WHITE),
    Line(DOWN * 0.7, DOWN * 1.1 + RIGHT * 0.25, color=WHITE),
)
student = VGroup(head, body, arms, legs)
```

## Paper / Relevé de notes
```python
paper = RoundedRectangle(width=3.4, height=4.2, corner_radius=0.15, color=WHITE)
label = Text("Relevé de notes", font="Montserrat", font_size=26, color=WHITE)
```

## Pressure Words
Use Arabic text objects with orange/red color and place around `BAC`:

```python
phrases = [
    ar("واش جبت؟"),
    ar("دخلت طب؟"),
    ar("جبت Mention؟"),
    ar("وش قالو الناس؟"),
    ar("ما تخيبناش"),
    ar("مستقبلك هنا"),
]
```

Because `Mention` is Latin inside Arabic, test carefully. If it renders badly, use two objects side by side:

```text
جبت
Mention
؟
```

---

# 14. Image Placeholder Policy
Avoid real images if possible. This video can be made fully with typography, icons, and shapes.

Only use image placeholders if the agent decides to add realism.

Optional placeholders:

```text
[IMAGE_PLACEHOLDER_1]
Description: A simple, generic silhouette of an Algerian student sitting at a desk, stressed before an exam. Use only if vector-style image is available. Do not use real copyrighted photos.
```

```text
[IMAGE_PLACEHOLDER_2]
Description: A generic exam paper / answer sheet icon. Prefer creating it directly with Manim shapes instead of importing an image.
```

Recommended: **do not use external images**. Build everything with Manim shapes and text.

---

# 15. Important Layout Rules

1. Never display too much Arabic text at once.
2. Keep each scene focused on one main idea.
3. Use big text for emotional sentences.
4. Use smaller text only for supporting words.
5. Keep enough margin around the screen, especially in vertical format.
6. Avoid placing Arabic text too close to edges because reshaped text can appear wider than expected.
7. Test render at low quality first:

```bash
manim -pql bac_video.py BACVideo
```

Then final render:

```bash
manim -pqh bac_video.py BACVideo
```

For vertical format, configure pixel dimensions in Manim config or use command options depending on the installed version.

---

# 16. Suggested Class Structure for Codex

Create a single Python file:

```text
bac_dz_manim.py
```

Main class:

```python
class BACDzAwarenessVideo(MovingCameraScene):
    def construct(self):
        self.setup_scene()
        self.scene_1_hook()
        self.scene_2_pressure()
        self.scene_3_grade_overload()
        self.scene_4_reality_check()
        self.scene_5_comparison()
        self.scene_6_solution()
        self.scene_7_final_message()
```

Helper methods:

```python
def make_ar_text(self, text, font_size=40, color=WHITE):
    ...

def make_latin_text(self, text, font_size=60, color=WHITE):
    ...

def create_student_icon(self):
    ...

def create_paper(self):
    ...

def create_card(self, text, color):
    ...
```

This structure will make the code easier to edit later.

---

# 17. Quality Checklist Before Final Render

The agent must verify:

- Arabic letters are connected correctly.
- Arabic text is not reversed.
- Latin `BAC`, `Mention`, and `Relevé de notes` are readable.
- No scene contains too many objects.
- Voiceover timing matches animation timing.
- The final message appears long enough to be read.
- The video does not attack students, parents, or teachers; it criticizes pressure and comparison.
- The message remains balanced: BAC is important, but not life itself.

---

# 18. Final Closing Frame

The final frame must stay visible for at least **2 seconds**.

Final text:

```text
BAC مرحلة... ماشي نهاية الحياة
```

Second line:

```text
الإنسان أكبر من ورقة نقاط
```

Small signature:

```text
رسالة مواطن
```

Fade out slowly.

---

# 19. Emotional Direction for the Whole Video
The viewer should feel this progression:

```text
Attention → Pressure → Realization → Balance → Hope
```

Do not end with sadness. End with clarity and support.

