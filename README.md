# Manim Project Notes

## Manim Journey Teaser

Scene file:

```text
projects/manim_journey_teaser.py
```

Scene class:

```text
ManimJourneyTeaser
```

Render the primary 4:5 LinkedIn/social version from the project root:

```powershell
manim -pqh projects/manim_journey_teaser.py ManimJourneyTeaser
```

Or use the root wrapper:

```powershell
manim -pqh main.py ManimJourneyTeaser
```

Expected output is an MP4 under `media/videos/...`. The scene sets a
1080 x 1350 canvas at 30 fps.

Background music is intentionally not embedded in the Manim scene. Add a
license-safe motivational ambient/tech track in your editor, or mux it after
rendering with ffmpeg:

```powershell
ffmpeg -i rendered_video.mp4 -i music.mp3 -shortest -c:v copy -c:a aac final_with_music.mp4
```

Arabic text uses the shared helpers in `common/manim_helpers.py` by default.
If Arabic shaping appears disconnected on your machine, install the Python
Arabic helpers used there:

```powershell
pip install arabic-reshaper python-bidi
```

The scene also has an opt-in LuaLaTeX/Cairo path through
`common/arabic_text_helper.py` and `safe_ar_text`. Use it only on a UTF-8
friendly console with LuaLaTeX available:

```powershell
$env:MANIM_JOURNEY_USE_TEX_ARABIC="1"
manim -pqh projects/manim_journey_teaser.py ManimJourneyTeaser
```
