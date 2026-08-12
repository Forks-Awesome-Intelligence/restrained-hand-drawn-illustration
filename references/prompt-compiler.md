# Prompt compiler

Build prompts in this order. Keep the positive description specific and the exclusions short.

## Static prompt template

```text
Create an original small, playful pencil-line vignette of [ONE TINY VISUAL JOKE].
Subject and action: [1–2 simple subjects], [one unexpected but readable action], [0–2 tiny supporting marks].
Composition: [tiny ground-line/floating encounter/small object joke/off-balance stack], drawing occupies only [20–45%] of the frame, [placement], 55–80% pale [ground color] negative space, [required aspect ratio].
Line profile: [soft-crayon-outline/fine-gesture/ink-silhouette].
Drawing treatment: a broad tactile deep-charcoal outer contour with visibly variable width and softly grainy edges. Give every stroke an organic pressure path: light or tapered touch-down, fuller middle, then a gentle lifted/tapered or softly rounded release; avoid uniform stamped ends. Use open-contour grammar: leave 1–3 intentional gaps on each main subject, especially at overlap, turns, or low-information edges; do not close every silhouette into a neat shape. Use thin marks only for small expressive details, and optionally one small solid black patch. Curves should sweep, overlap, and land imperfectly rather than meet at hard geometric corners. Use simplified, deliberately uneven silhouettes and asymmetric spacing; flat fills only, [one muted accent recipe] under 12% of the image; [optional short handwritten text and placement].
Avoid: grand scene, poster-scale subject, cityscape, skyline, realistic landscape, elaborate background, technical construction, repeated detail, exact symmetry, mechanically equal spokes, thin outlines used everywhere, scratchy sketch lines, blunt cut-off marks, identical round endpoints, fully closed cartoon outlines, hard polygonal joins, polished vector art, uniform heavy outlines, photorealism, gradients, 3D, glossy lighting, saturated or neon colors, dense pattern, legible filler text, logos, watermarks, copied reference composition or characters.
```

## Photo/image transform addition

```text
Use the supplied image as the edit target. Preserve [identity/product/pose/clothing/other agreed cues] and its [ratio]; extract only one playful action or object relationship, then redraw it as a compact original pencil-line vignette. Do not retain incidental background, photographic scale, scenery, original typography, logos, or photographic rendering unless explicitly requested.
```

## Lettering addition

```text
Add only this exact short handwritten phrase: "[TEXT]". Treat it as irregular drawn lettering, place it at [location], and keep it subordinate to the illustration. If exact legibility is essential, leave a clear lettering zone for verified post-processing.
```

## Prompt review

Confirm that it contains one tiny joke, no more than two subjects, a stated ratio, a 20–45% subject footprint, a pale ground, a 12% color limit, and explicit exclusions for scene scale. Remove adjectives that create visual noise (cinematic, monumental, elaborate, highly detailed, vibrant, dynamic lighting) unless the user expressly overrides the house style.
