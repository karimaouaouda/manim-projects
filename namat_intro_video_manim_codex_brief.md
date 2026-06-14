# NAMAT Intro Video — Codex/Manim Production Brief

**Project:** نمط - Namat  
**Video Type:** Hidden-brand reveal / social-analysis cinematic short  
**Primary Format:** 9:16 vertical Reels/TikTok/Shorts  
**Recommended Resolution:** 1080 × 1920  
**FPS:** 30 or 60 FPS. Prefer 60 FPS for smoother line animations if rendering time allows.  
**Estimated Duration:** 85–105 seconds  
**Language of Voice-over:** Algerian Arabic / DZ Arabic  
**Purpose:** Introduce the Namat project without making the viewer feel they are watching a presentation. The viewer should think this is a normal social-analysis video about Algerian life, keep searching for the hidden explanation, then discover that the missing concept is **نمط**.

---

## 1. Core Creative Strategy

Do **not** start by presenting the page or logo.

The video should begin like a serious, attractive social-analysis video about everyday Algerian patterns. The viewer should see different social phenomena and feel that something invisible connects them. The brand **NAMAT** should be revealed only after the viewer has emotionally and intellectually searched for the missing word.

### Emotional viewer journey

1. “This looks like a normal video about society.”
2. “Wait, all these problems feel connected.”
3. “What is the hidden thing behind them?”
4. “Ah… this is called نمط.”
5. “So Namat is the page that reveals these hidden patterns.”

### Main slogan

```text
افهم النمط… قبل ما يتحكم فيك.
```

### Central message

```text
المشكل ماشي دايماً في القرار… مرات المشكل في النمط اللي يسبق القرار.
```

---

## 2. Social Media Retention Logic

This video must be built for retention, not just beauty.

### Retention principles to implement

- Start with a **cold hook** in the first 1 second. No logo. No introduction.
- Use a **curiosity gap**: show repeated social situations, then delay the explanation.
- Use **visual progression**: every scene adds a piece to the hidden system.
- Use **pattern repetition**: circles, lines, loops, puppet strings, and connected points appear repeatedly.
- Use **micro-reveals** every 6–10 seconds so the viewer feels progress.
- Keep text readable and short: 3–7 words per on-screen line whenever possible.
- Do not overload the bottom area because TikTok/Instagram/Facebook UI covers lower screen areas.
- Use captions/subtitles throughout because many viewers watch with low or no sound.
- Use the brand reveal around **60–70%** of the video, not early.

---

## 3. Visual Identity

### Colors

Use a modern dark analytical identity.

```python
BG = "#071421"          # deep navy background
WHITE = "#F4F7FB"       # main text and line art
MUTED = "#8EA4B8"       # secondary labels
GOLD = "#F6C85F"        # insight / reveal / important word
RED = "#F25F5C"         # pressure / danger / panic
CYAN = "#3DDCFF"        # analysis lines / scanning / digital glow
GREEN = "#6EE7B7"       # awareness / clarity
```

### Typography

Use one strong Arabic font and one clean Latin font.

Recommended Arabic fonts:

- `Tajawal`
- `Cairo`
- `Noto Kufi Arabic`
- `Noto Naskh Arabic`

Recommended Latin font:

- `Inter`
- `Montserrat`
- `Poppins`

### Text rules

- Arabic text must be center-aligned for big statements.
- Use high contrast: white text on dark background.
- Use gold only for key words: `نمط`, `واش يقولوا الناس؟`, `الخوف`, `الضغط`, `وعي`.
- Avoid placing important text in the bottom 25–35% of the frame.

---

## 4. Required Assets

Create placeholders in the Manim code. Do not fail if assets are missing; show a clean placeholder rectangle with label instead.

```text
assets/
  logo/
    namat_logo.png                  # optional; reveal can be generated as text too
  mascot/
    namat_mascot.svg                # optional thinker mascot
  profiles/
    facebook_profile.png            # screenshot/image of the Namat Facebook profile
    instagram_profile.png           # screenshot/image of the Namat Instagram profile
    tiktok_profile.png              # screenshot/image of the Namat TikTok profile
  audio/
    voiceover.wav                   # final voice-over after recording
    ambient_dark_pulse.mp3          # optional background music
    reveal_hit.wav                  # optional NAMAT reveal hit
```

If the profile images are unavailable, generate mock profile cards using Manim shapes:

- Facebook card: blue accent, `f` icon placeholder, profile name `نمط - Namat`
- Instagram card: pink/orange/purple border gradient approximation using layered strokes, camera icon placeholder
- TikTok card: black card with cyan/red offset note icon placeholder

---

## 5. Manim Implementation Requirements

### Scene class

Use one main Manim scene:

```python
class NamatIntroVideo(Scene):
    pass
```

or, for better camera movements:

```python
class NamatIntroVideo(MovingCameraScene):
    pass
```

### Important helper functions to implement

```python
def make_arabic_text(text, size=48, color=WHITE, weight="MEDIUM"):
    # Return Text object with Arabic font and RTL-compatible rendering.
    pass


def safe_title(text, y=2.8, size=50):
    # Main text positioned in safe zone.
    pass


def make_social_character(label, icon_type, mood="neutral"):
    # Minimal 2D character + icon + label.
    pass


def pulse_line_between(p1, p2, color=CYAN, width=3):
    # Draw line then animate glowing pulse dot moving through it.
    pass


def make_phone_card(platform, image_path=None):
    # Phone mockup containing profile screenshot or fallback profile UI.
    pass


def morph_points_to_word(points_group, word_text):
    # Visually collapse network/circles/lines into the word نمط.
    pass
```

### Animation style

- Use `LaggedStart` heavily for modern staggered entrances.
- Use `Create`, `FadeIn`, `FadeOut`, `TransformMatchingShapes`, `ReplacementTransform`, `MoveAlongPath`, `Indicate`, `Flash`, and custom camera zooms.
- Use `rate_func=smooth`, `rate_func=there_and_back`, and `rate_func=ease_out_cubic` if available.
- Use `always_redraw` or updaters for subtle moving background particles.
- Use short camera pushes for emotional lines.
- Avoid static scenes longer than 3 seconds.

---

## 6. Global Animation Motif: The Hidden Pattern System

The video should use the same visual language from beginning to end:

1. **Dots** = people / moments / choices.
2. **Lines** = hidden social connections.
3. **Circles/loops** = repeated behavior.
4. **Puppet strings** = invisible pressure.
5. **Detective board** = analysis.
6. **Letters ن م ط** = hidden concept.
7. **Word نمط** = final reveal.

The viewer must subconsciously see the same shapes coming back. This makes the reveal feel natural.

---

# 7. Full Scene-by-Scene Production Plan

---

## Scene 0 — Pre-Hook Black Pulse

**Time:** 0:00–0:02  
**Goal:** Stop the scroll instantly with mystery, not branding.

### Visual

- Start with black/dark navy screen.
- A tiny white dot appears in the center.
- The dot pulses once like a heartbeat.
- Very quick glitch flash of many small dots around it.
- No logo.

### On-screen text

```text
كاين حاجة راهي تتعاود...
```

Text should appear for less than 1.5 seconds, centered slightly above the middle.

### Voice-over

```text
كاين حاجة راهي تتعاود...
```

### Animation

- Dot scales from 0 to 1.2 then returns to 1.
- Text appears with `FadeIn` from blur/opacity if possible.
- Add subtle screen vibration at the pulse.
- Cut immediately to Scene 1.

### Transition to next scene

The central dot splits into 5 dots that fly into different positions, each becoming a different social situation.

---

## Scene 1 — Social Montage: “Different stories?”

**Time:** 0:02–0:16  
**Goal:** Make the viewer feel this is a normal attractive DZ social video.

### Visual

Show 5 quick mini-scenes. Each mini-scene gets around 2.5 seconds.

#### Mini-scene A — Diploma waiting

- Character holding a diploma.
- Behind him: empty office chair labeled `وظيفة`.
- A clock rotates slowly above him.
- Character does not move; only the clock moves.

#### Mini-scene B — BAC/specialty panic

- Character relaxed on a couch.
- Result paper appears suddenly.
- Multiple specialty cards fly around him: `طب`, `إعلام آلي`, `حقوق`, `مدرسة عليا`, `بيولوجيا`.
- Character becomes smaller under the cards.

#### Mini-scene C — Killed project idea

- Character holding a glowing paper labeled `فكرة`.
- Speech bubbles appear: `ما تصلحش هنا`, `شكون يشري؟`, `خليك مضمون`.
- The glow of the idea dims.

#### Mini-scene D — Social media comparison

- Big phone screen with fake success posts.
- Character beside the phone shrinks slowly.
- Likes/hearts float upward while the character looks down.

#### Mini-scene E — People’s opinion pressure

- Character in center.
- Around him: circular crowd icons.
- Speech bubbles repeat: `واش يقولوا الناس؟`

### Voice-over

```text
واحد يدي الديبلوم... ويستنى الخدمة تجيه.

واحد يكمل الباك...
وبعدها يفيق بلي لازم يختار حياتو في ليلة.

واحد عندو فكرة مشروع...
يدفنها قبل ما تبدأ.

واحد يشوف نجاح الناس في الهاتف...
وينسى الطريق تاعو.

واحد ما يختارش واش يحب...
يختار واش الناس ما يضحكوش عليه.
```

### Animation details

- Each mini-scene enters using `ReplacementTransform` from the previous one, not hard cuts.
- Use a fast `camera.frame.animate.scale(0.95)` push on every new example.
- Use red accents for pressure bubbles.
- Use gold only for the word `فكرة`.
- Add small background moving dots to maintain motion.

### Transition to next scene

All five mini-scenes shrink into five circular nodes arranged around the screen. A thin cyan line starts connecting them.

---

## Scene 2 — The Viewer Starts Searching

**Time:** 0:16–0:27  
**Goal:** Shift from examples to mystery. Make the viewer ask: “What connects these?”

### Visual

- Five circular nodes remain from Scene 1.
- Each node contains a simplified icon from the earlier examples.
- Lines begin connecting nodes slowly.
- The lines do not fully connect at first; they flicker like a weak signal.

### On-screen text

```text
تشوفهم قصص مختلفة؟
```

Then replace with:

```text
ركز مليح...
```

### Voice-over

```text
تشوفهم قصص مختلفة؟

بصح ركز مليح...

نفس الخوف.
نفس الضغط.
نفس المقارنة.
نفس الهروب.
نفس الجملة:
واش يقولوا الناس؟
```

### Animation details

- On every repeated phrase, add a label near one node:
  - `الخوف`
  - `الضغط`
  - `المقارنة`
  - `الهروب`
  - `واش يقولوا الناس؟`
- Draw each label with a quick typewriter effect.
- Use `Create(Line)` between labels.
- Add a small glowing dot moving across the lines using `MoveAlongPath`.
- Make the connected graph slowly rotate by 3–5 degrees, almost unnoticeable.

### Transition to next scene

The network lines stretch upward and become puppet strings.

---

## Scene 3 — Invisible Script / Puppet Pressure

**Time:** 0:27–0:40  
**Goal:** Make the concept deeper: people are not just choosing; repeated voices choose before them.

### Visual

- A single character appears in the middle.
- The earlier network lines transform into puppet strings attached to his hands, head, and back.
- Above the strings, labels appear:
  - `العائلة`
  - `المجتمع`
  - `المقارنة`
  - `الخوف`
  - `العادة`
  - `الاستسلام`
- The strings pull slightly in different directions.
- The character tries to move but is pulled back.

### Voice-over

```text
المشكل مرات ما يكونش في القرار.

المشكل في السكريبت اللي يتعاود داخل راسك...
وفي الصوت اللي يحكمك قبل ما تختار.

صوت يقولك:
استنى.
خاف.
ما تبداش.
دير كيما الناس.
ما تخاطرش.
ما تصلحش هنا.
```

### On-screen text

Main text should appear phrase-by-phrase:

```text
المشكل ماشي دايماً في القرار
```

Then:

```text
مرات في السكريبت اللي يسبق القرار
```

### Animation details

- Use `Transform` from lines to strings.
- Labels above strings should appear with slight jitter.
- Each command word appears like a stamp hitting the screen:
  - `استنى`
  - `خاف`
  - `ما تبداش`
  - `دير كيما الناس`
- Use red for command words.
- Character should be simple: circular head, dot eyes, capsule body, thin limbs.
- Add subtle body squash/stretch when strings pull.

### Transition to next scene

The puppet strings snap. The snapped string endpoints become pins on a detective board.

---

## Scene 4 — Detective Board: The Hidden Social Map

**Time:** 0:40–0:53  
**Goal:** Turn emotion into analysis. The viewer now sees that Namat is not complaining; it is investigating.

### Visual

- Screen becomes a dark detective-board layout.
- Pins/nodes show social phenomena:
  - `ديبلوم`
  - `خدمة`
  - `باك`
  - `تخصص`
  - `مشروع`
  - `سوشيال ميديا`
  - `عائلة`
  - `زواج`
  - `واش يقولوا الناس؟`
- Animated lines connect them.
- Some lines are straight, some curved, some dashed.
- A magnifying glass scans over the board.

### Voice-over

```text
علاش واحد يستنى الخدمة وما يبحثش على طريقو؟

علاش واحد يختار تخصص ما يفهموش غير خاطر قالولو مليح؟

علاش مشروع يموت قبل ما يتجرب؟

علاش كلمة من الناس تقدر توقف مستقبل كامل؟

علاش نعاودو نفس الغلطة...
ونسميوها ظروف؟
```

### Animation details

- Use `Dot` objects as pins.
- Use `DashedLine`, `Line`, and `CubicBezier` curves for connections.
- Animate lines with `Create` using staggered timing.
- Add a small light sweep across the board using translucent rectangle or gradient-like group.
- Every time the voice says “علاش”, briefly zoom into one node then back out.

### Required between-points line animation

Implement a function for connecting concepts:

```python
def connect_concepts(start_mob, end_mob, label=None, color=CYAN):
    line = Line(start_mob.get_center(), end_mob.get_center(), color=color, stroke_width=3)
    pulse = Dot(color=GOLD).scale(0.55)
    # Create line, then move pulse from start to end.
    return VGroup(line, pulse)
```

Use at least 10 animated connections:

1. `ديبلوم` → `خدمة`
2. `باك` → `تخصص`
3. `تخصص` → `العائلة`
4. `مشروع` → `الخوف`
5. `سوشيال ميديا` → `المقارنة`
6. `المقارنة` → `الإحباط`
7. `عائلة` → `واش يقولوا الناس؟`
8. `زواج` → `ضغط`
9. `ضغط` → `هروب`
10. `هروب` → `نفس الغلطة`

### Transition to next scene

The detective board zooms out. The lines become a maze from above.

---

## Scene 5 — Maze of Repeated Choices

**Time:** 0:53–1:03  
**Goal:** Show that repeated behavior becomes a trap.

### Visual

- The connection lines morph into a maze.
- A small character walks inside the maze.
- Each dead end contains one word:
  - `نستنى`
  - `نقارن`
  - `نخاف`
  - `نلوم`
  - `نقلد`
- The character reaches a dead end, turns, repeats.
- Above the maze, a faint missing word outline appears but remains unreadable.

### Voice-over

```text
كي نفس السلوك يرجع...
ونفس الخوف يرجع...
ونفس الطريقة في التفكير ترجع...

هنا ما بقيناش نحكيو على موقف.

كاين كلمة ناقصة.
```

### Animation details

- Build maze using `VMobject` or groups of `Line` objects.
- Character moves with `MoveAlongPath`.
- Camera follows character for 2 seconds then zooms out to show the whole maze.
- Make dead-end words appear only when the character reaches them.
- The missing word outline should flicker in gold but remain incomplete.

### Transition to next scene

Maze lines begin collapsing inward. Dead-end words fly toward the center and dissolve into three separate letters: `ن`, `م`, `ط`.

---

## Scene 6 — The Missing Letters

**Time:** 1:03–1:10  
**Goal:** Build suspense just before reveal.

### Visual

- Empty dark background.
- Three large letters appear separately but not aligned:
  - `ن` appears from the diploma node.
  - `م` appears from the project/social media node.
  - `ط` appears from the people-pressure node.
- The letters float, rotate gently, and do not yet form a word.
- Around them: tiny nodes orbit like a system.

### On-screen text

```text
كاين كلمة ناقصة...
```

### Voice-over

```text
كاين كلمة ناقصة.
```

Pause 0.5–0.8 seconds.

### Animation details

- Use silence or low ambient pulse.
- Use slow-motion movement here; this is the breathing space before reveal.
- Background particles stop moving for a moment.
- The three letters glow lightly in gold.

### Transition to next scene

The letters snap into alignment with a clean sound hit.

---

## Scene 7 — Main Reveal: NAMAT

**Time:** 1:10–1:20  
**Goal:** Reveal the project name as the answer, not as an ad.

### Visual

- Letters combine into:

```text
نمط
```

- Under it, smaller Latin text appears:

```text
NAMAT
```

- All previous nodes/circles/lines appear behind the word as a subtle constellation.
- The word should be large, centered, gold/white combination.

### Voice-over

```text
هذا اسمو...

نمط.

النمط هو الشي اللي يتعاود فينا...
حتى نوليو نحسبوه طبيعة.
```

### Animation details

- `نمط` should be created by morphing the lines, not simply fading in.
- Use `TransformMatchingShapes` where possible.
- Add a circular ripple from the center when the word appears.
- Use a short camera push-in during the word `نمط`.
- Add one soft reveal sound hit.

### Text styling

- `نمط` in gold.
- `NAMAT` in muted white/cyan.
- Background constellation in low opacity.

### Transition to next scene

The word `نمط` moves upward and becomes a header. Below it, the project meaning appears through animated visual examples.

---

## Scene 8 — What Namat Actually Does

**Time:** 1:20–1:34  
**Goal:** Introduce the project clearly, but still in cinematic style.

### Visual

- Namat word remains at top.
- Optional mascot appears from the side as a thinker/analyzer, not a childish narrator.
- A magnifying glass/light beam scans three layers:
  1. `قدامك` — society
  2. `فيك` — internal fear/thoughts
  3. `حولك` — family/media/work pressure
- Each layer appears as a transparent plane, stacked in perspective.

### Voice-over

```text
ونمط...
ما جاش باش يحكم عليك.

جاء باش يوريك واش راه يتعاود قدامك...
وفيك...
وفي المجتمع اللي عايش فيه.

باش كي تشوف الخوف، ما تتبعوش.
وكي تشوف الضغط، ما تذوبش فيه.
وكي تشوف الطريق، تختارو بوعي.
```

### On-screen text

Use three short statements:

```text
ماشي حكم
```

```text
فهم
```

```text
وعي
```

### Animation details

- `ماشي حكم` appears then gets crossed softly, not aggressively.
- `فهم` appears with a magnifying lens.
- `وعي` appears with a small light expansion.
- Make the mascot point to the layers with simple arm movement if SVG parts allow it.

### Transition to next scene

The three words `فهم`, `وعي`, `اختيار` become three glowing dots that move into a compass shape.

---

## Scene 9 — Religious/Moral Depth Without Preaching

**Time:** 1:34–1:45  
**Goal:** Anchor the project in values without turning the video into direct preaching.

### Visual

- A minimal compass in the center.
- Left side: simple brain icon labeled `عقل`.
- Right side: simple heart icon labeled `قلب`.
- Above: light ray labeled `قيم`.
- The compass needle aligns gently toward `وعي`.

### Voice-over

```text
لأن الوعي ماشي ضد الدين.

ربي عطانا عقل باش نتدبرو،
وقلب باش نرحمو،
وقيم باش ما نضيعوش وسط الزحام.

والمؤمن ما يعيش غير مقلد...
يعيش فاهم، مسؤول، وواعي.
```

### Animation details

- Keep this scene calm and elegant.
- No heavy religious symbols.
- Use light, compass, heart, brain, and balance only.
- Use gold for `وعي` and `قيم`.
- Add a slow breathing glow to the compass.

### Transition to next scene

The compass needle draws a line that becomes a path leading to three phone/profile cards.

---

## Scene 10 — Social Profiles Reveal: Facebook / Instagram / TikTok

**Time:** 1:45–1:57  
**Goal:** Reveal where the viewer can find Namat, but keep it part of the story. This is the only scene that can feel like a soft call-to-action.

### Visual

Three vertical phone/profile cards slide into view:

1. **Facebook profile** on the left.
2. **Instagram profile** in the center.
3. **TikTok profile** on the right.

The Instagram card should be slightly larger/in front if Instagram is the main visual platform. TikTok can pulse more if short-form discovery is priority.

### Required profile images

Use these image paths if available:

```text
assets/profiles/facebook_profile.png
assets/profiles/instagram_profile.png
assets/profiles/tiktok_profile.png
```

### Fallback design if images are missing

Each phone card should contain:

- circular profile avatar placeholder with the Namat logo/word
- name: `نمط - Namat`
- username placeholder: `@namat.dz` or `@namat`
- button placeholder: `Follow / متابعة`
- 2–3 mini post thumbnails with abstract Manim-style patterns

### Animation details

- A glowing line from the compass path reaches the center Instagram card first.
- Then the line splits to Facebook and TikTok.
- Use `DrawBorderThenFill` for phone frames.
- Use `FadeIn(profile_image, shift=UP*0.3)`.
- Add a small cyan pulse around each platform card when it appears.
- Create a “connected ecosystem” feel: three cards connected by thin animated lines.
- Under the cards, write:

```text
وين ما كنت... شوف النمط.
```

### Voice-over

```text
من هنا يبدأ نمط.

في كل فيديو...
نحاولو نشوفو الشي اللي كان قدامنا...
وما كناش نشوفوه.
```

### Platform labels

Use short labels below cards:

```text
Facebook
Instagram
TikTok
```

Do not overdo platform colors. Keep brand identity dominant.

### Transition to final scene

The three profile cards slide backward and become three small glowing nodes orbiting the final logo.

---

## Scene 11 — Final Brand Lockup

**Time:** 1:57–2:05  
**Goal:** End with a memorable slogan and clear identity.

### Visual

- Final centered logo/text:

```text
نمط - NAMAT
```

- Under it:

```text
افهم النمط… قبل ما يتحكم فيك.
```

- Behind it: subtle animated constellation of social nodes.
- Nodes slowly stop moving, forming a stable pattern.

### Voice-over

```text
نمط...
باش نشوفو الشي اللي كان قدامنا...
وما كناش نشوفوه.

افهم النمط...
قبل ما يتحكم فيك.
```

### Animation details

- Final text appears with `Write` or `FadeIn` + slight upward motion.
- Background lines slowly fade to 20% opacity.
- End with the central dot pulse from Scene 0, closing the loop.
- Leave 0.5 seconds of clean final frame for readability.

---

# 8. Full Voice-over Script

Use this exact script as the first version. Timing can be adjusted during editing.

```text
كاين حاجة راهي تتعاود...

واحد يدي الديبلوم... ويستنى الخدمة تجيه.

واحد يكمل الباك...
وبعدها يفيق بلي لازم يختار حياتو في ليلة.

واحد عندو فكرة مشروع...
يدفنها قبل ما تبدأ.

واحد يشوف نجاح الناس في الهاتف...
وينسى الطريق تاعو.

واحد ما يختارش واش يحب...
يختار واش الناس ما يضحكوش عليه.

تشوفهم قصص مختلفة؟

بصح ركز مليح...

نفس الخوف.
نفس الضغط.
نفس المقارنة.
نفس الهروب.
نفس الجملة:
واش يقولوا الناس؟

المشكل مرات ما يكونش في القرار.

المشكل في السكريبت اللي يتعاود داخل راسك...
وفي الصوت اللي يحكمك قبل ما تختار.

صوت يقولك:
استنى.
خاف.
ما تبداش.
دير كيما الناس.
ما تخاطرش.
ما تصلحش هنا.

علاش واحد يستنى الخدمة وما يبحثش على طريقو؟

علاش واحد يختار تخصص ما يفهموش غير خاطر قالولو مليح؟

علاش مشروع يموت قبل ما يتجرب؟

علاش كلمة من الناس تقدر توقف مستقبل كامل؟

علاش نعاودو نفس الغلطة...
ونسميوها ظروف؟

كي نفس السلوك يرجع...
ونفس الخوف يرجع...
ونفس الطريقة في التفكير ترجع...

هنا ما بقيناش نحكيو على موقف.

كاين كلمة ناقصة.

هذا اسمو...

نمط.

النمط هو الشي اللي يتعاود فينا...
حتى نوليو نحسبوه طبيعة.

ونمط...
ما جاش باش يحكم عليك.

جاء باش يوريك واش راه يتعاود قدامك...
وفيك...
وفي المجتمع اللي عايش فيه.

باش كي تشوف الخوف، ما تتبعوش.
وكي تشوف الضغط، ما تذوبش فيه.
وكي تشوف الطريق، تختارو بوعي.

لأن الوعي ماشي ضد الدين.

ربي عطانا عقل باش نتدبرو،
وقلب باش نرحمو،
وقيم باش ما نضيعوش وسط الزحام.

والمؤمن ما يعيش غير مقلد...
يعيش فاهم، مسؤول، وواعي.

من هنا يبدأ نمط.

في كل فيديو...
نحاولو نشوفو الشي اللي كان قدامنا...
وما كناش نشوفوه.

نمط...
باش نشوفو الشي اللي كان قدامنا...
وما كناش نشوفوه.

افهم النمط...
قبل ما يتحكم فيك.
```

---

# 9. On-Screen Caption Plan

Do not show the full voice-over as subtitles in large chunks. Use short kinetic captions.

## Caption rhythm

- One strong caption every 2–4 seconds.
- Keep captions at center or upper-middle.
- Use bottom captions only if they are inside safe zone above platform UI.

## Key captions

```text
كاين حاجة راهي تتعاود...
```

```text
تشوفهم قصص مختلفة؟
```

```text
نفس الخوف
```

```text
نفس الضغط
```

```text
نفس المقارنة
```

```text
واش يقولوا الناس؟
```

```text
المشكل ماشي دايماً في القرار
```

```text
كاين كلمة ناقصة
```

```text
هذا اسمو... نمط
```

```text
ماشي حكم
```

```text
فهم
```

```text
وعي
```

```text
افهم النمط… قبل ما يتحكم فيك
```

---

# 10. Advanced Transition Map

## Transition A — Dot split

Scene 0 → Scene 1

- Central dot splits into 5 dots.
- Each dot becomes a social example.

## Transition B — Examples to network

Scene 1 → Scene 2

- Each social example shrinks into a circular node.
- Nodes arrange into a graph.
- Lines start drawing between nodes.

## Transition C — Network to puppet strings

Scene 2 → Scene 3

- Graph lines stretch upward.
- Lines attach to the character as puppet strings.
- Labels appear above strings.

## Transition D — Puppet strings to detective board

Scene 3 → Scene 4

- Strings snap.
- Snapped ends become board pins.
- Pins spread across screen.
- Lines reconnect with analytical style.

## Transition E — Detective board to maze

Scene 4 → Scene 5

- Board rotates downward as if viewed from above.
- Connections become maze walls.
- A small character enters the maze.

## Transition F — Maze to letters

Scene 5 → Scene 6

- Maze walls collapse inward.
- Dead-end words dissolve.
- Three letters appear: `ن`, `م`, `ط`.

## Transition G — Letters to logo

Scene 6 → Scene 7

- Letters magnetically align.
- Lines and particles wrap around them.
- `نمط` is revealed.

## Transition H — Logo to social profiles

Scene 9 → Scene 10

- Compass needle draws a path.
- Path becomes a connecting line toward phone cards.
- Three profile cards reveal as nodes on the same network.

## Transition I — Profiles to final lockup

Scene 10 → Scene 11

- Phone cards shrink into glowing nodes.
- Nodes orbit final logo.
- Logo locks in place.

---

# 11. Sound Design Direction

The video can work without music, but sound will increase retention.

### Background music

- Dark cinematic ambient pulse.
- Low percussion heartbeat at beginning.
- Slight rise before NAMAT reveal.
- Calm warm texture after reveal.

### Sound effects

- Dot pulse: soft bass hit.
- Lines connecting: digital spark / whoosh.
- Puppet string pull: subtle tension sound.
- String snap: short snap.
- Reveal: soft cinematic hit, not too aggressive.
- Profile cards: light pop/whoosh.

### Important

Voice-over must remain clear. Music should stay under voice.

---

# 12. Recommended Code Architecture

Codex should generate clean, maintainable Manim code.

```text
namat_intro/
  main.py
  assets/
    profiles/
    logo/
    mascot/
    audio/
  utils/
    colors.py
    typography.py
    shapes.py
    animations.py
```

If Codex generates a single file, still organize code with sections:

1. Constants
2. Helper Functions
3. Character Components
4. Social Node Components
5. Phone/Profile Card Components
6. Main Scene
7. Scene Methods

Recommended main scene methods:

```python
class NamatIntroVideo(MovingCameraScene):
    def construct(self):
        self.setup_background()
        self.scene_00_pre_hook()
        self.scene_01_social_montage()
        self.scene_02_pattern_network()
        self.scene_03_invisible_script()
        self.scene_04_detective_board()
        self.scene_05_maze()
        self.scene_06_missing_letters()
        self.scene_07_namat_reveal()
        self.scene_08_project_meaning()
        self.scene_09_moral_depth()
        self.scene_10_profiles_reveal()
        self.scene_11_final_lockup()
```

---

# 13. Technical Notes for Arabic in Manim

Use `Text` with a font that supports Arabic.

Example:

```python
Text("افهم النمط", font="Tajawal", color=WHITE)
```

If Arabic appears disconnected or reversed depending on the environment, use Arabic shaping utilities before passing text to Manim:

```python
import arabic_reshaper
from bidi.algorithm import get_display

reshaped = arabic_reshaper.reshape(text)
rtl_text = get_display(reshaped)
```

Then pass `rtl_text` to `Text`.

Codex should implement a safe helper:

```python
def ar(text: str) -> str:
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        return get_display(arabic_reshaper.reshape(text))
    except Exception:
        return text
```

---

# 14. Safe Zone Guide for Vertical Video

For 1080×1920 vertical output:

- Keep main text between y positions roughly `-2.5` and `+3.2` in Manim coordinate logic.
- Avoid important text in the bottom 25–35% of the screen.
- Avoid key logos at extreme right side where TikTok buttons may cover content.
- Final logo should be center or upper-center.
- Captions should not collide with platform UI.

---

# 15. Final Deliverable Requirements for Codex

Codex should output:

1. A full Manim Python script.
2. Clean helper functions.
3. Asset placeholders that do not crash if missing.
4. A vertical 9:16 scene configuration.
5. A complete animated sequence matching the scene plan.
6. Profile reveal scene with Facebook/Instagram/TikTok image placeholders.
7. Animated connecting lines between social phenomena.
8. Hidden reveal of `نمط` after suspense.
9. Final slogan screen.

---

# 16. Quality Checklist

Before final render, verify:

- [ ] No Namat logo appears before the reveal scene.
- [ ] First 3 seconds create curiosity.
- [ ] Social examples feel Algerian and relatable.
- [ ] Motion is continuous; no long static blocks.
- [ ] Lines/circles/loops appear repeatedly as hidden motif.
- [ ] The word `نمط` feels like the answer to the video.
- [ ] Profile cards appear only after the concept is understood.
- [ ] Captions are readable on phone.
- [ ] Important text avoids the bottom UI area.
- [ ] Arabic text renders correctly.
- [ ] Final slogan remains visible long enough.

---

# 17. Optional Shorter Variant

If the video must be shorter than 60 seconds, merge scenes like this:

- Scene 0 + 1: 0:00–0:12
- Scene 2 + 3: 0:12–0:25
- Scene 4 + 5: 0:25–0:38
- Scene 6 + 7: 0:38–0:46
- Scene 8 + 10 + 11: 0:46–0:60

But the recommended version is 85–105 seconds because the brand reveal needs emotional build-up.

---

# 18. Final Instruction to Codex

Generate a professional Manim video based on this brief. The video must feel like a cinematic social-analysis short first, and only later reveal that the hidden concept is **نمط - NAMAT**. Prioritize retention, mystery, modern motion design, and clean Arabic typography. Use animated points, connecting lines, loops, detective-board links, puppet strings, and final letter morphing to make the brand reveal feel inevitable.
