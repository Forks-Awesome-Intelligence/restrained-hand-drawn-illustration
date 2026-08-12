# Motion system

Animate the meaning, not the whole drawing. Preserve the still composition, palette, and line character. Make loops with a clear rest pose and a nearly identical first/last frame.

| Scene cue | Preferred loop | Notes |
| --- | --- | --- |
| Delivery, travel, urgency | small horizontal glide, wheel turn, trailing motion marks | loop across a short path; keep subject scale stable |
| Discovery, idea, surprise | pop, reveal, tiny star blink, object rise | use one staggered accent, then settle |
| Conversation, collaboration | nod, hand offer/receive, speech mark pulse | alternate only the communicating parts |
| Calm care, reading, waiting | breathing bob, steam curl, blink, gentle sway | 2–4 px-scale movement; avoid busy motion |
| Confusion, choice, search | head tilt, sign flip, orbiting mark | make the resolution return to the starting pose |
| Nature/animal | tail flick, ear twitch, drifting leaf, fish glide | retain a stable body silhouette |

## Animation process

1. Describe the action as one sentence: “the envelope rises slightly, pauses, then settles.”
2. Make 12–36 same-size frames using controlled layer movement or consistent image-editing passes. Keep the pale ground fixed and color count unchanged.
3. Use ease-in/ease-out; duplicate a brief rest at the turning point if needed. Avoid full-frame camera shake, morphing limbs, flicker, or unrelated random movement.
4. Inspect at actual GIF size, then compile: `export_raster.py gif frames/frame-*.png final.gif --delay-ms 100 --loop 0`.

Default delivery is a 3-second loop at 10 fps. Use 4–5 seconds only when the action needs a readable pause.
