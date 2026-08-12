# restrained-hand-drawn-illustration

Create small, playful hand-drawn illustrations from a photo, image, or written prompt. The skill turns a large or realistic scene into a quiet visual vignette: tactile variable-width charcoal-like lines, intentional open contours, generous pale negative space, and only a trace of muted color.

## What it does

- Reinterprets photos and visual references without copying their exact composition, text, or characters.
- Generates compact, humorous scenes from prompts, rather than full-scale editorial or cinematic illustrations.
- Uses relaxed, pressure-sensitive black crayon/graphite linework with soft starts and lifted endings.
- Keeps shapes selectively open instead of sealing every contour into a clean icon.
- Delivers RGB JPG stills at the requested or source aspect ratio.
- Creates 6-second looping GIFs at 10 fps with linked character-and-scene motion, exported with a maximum 400 px longest edge.

## Visual principles

- Warm white or pale-cream ground with 55–80% negative space.
- A compact vignette, normally occupying 20–45% of the frame.
- One or two simplified subjects and one clear visual joke.
- Deep charcoal contours with visible, natural 2–3:1 line-weight variation.
- One muted accent color by default; no saturated color, gradients, realistic shading, or dense scenery.
- Deliberate contour gaps at overlaps and turns; avoid mechanical, closed, vector-like outlines.

## Installation

Copy the `restrained-hand-drawn-illustration` folder into your Codex skills directory:

```text
<CODEX_HOME>/skills/restrained-hand-drawn-illustration/
```

If you downloaded the release archive, unzip it first and copy the extracted folder into that location. Restart or refresh Codex so the skill is discovered.

## Example prompts

```text
Use $restrained-hand-drawn-illustration to create a 1:1 JPG of a woman pulling a suitcase to the right.
```

```text
Use $restrained-hand-drawn-illustration to reinterpret this photo as a small open-contour illustration, preserving the main action and the original aspect ratio.
```

```text
Use $restrained-hand-drawn-illustration to make a 3-second looping GIF: the climber reaches slightly upward, pauses, then settles back.
```

## Included files

```text
restrained-hand-drawn-illustration/
├── SKILL.md                    # Main workflow and quality gate
├── agents/openai.yaml          # Codex skill metadata
├── references/
│   ├── style-system.md          # Fixed visual rules and palette recipes
│   ├── line-profiles.md        # Crayon, gesture, and silhouette profiles
│   ├── prompt-compiler.md      # Prompt-building guidance
│   └── motion-system.md        # Small-loop animation guidance
└── scripts/export_raster.py    # JPG and validated looping-GIF export helper
```

## GitHub description

> Create playful, restrained hand-drawn illustrations from photos or prompts, featuring natural open contours, tactile variable-width lines, pale backgrounds, sparse muted color, JPG delivery, and optional GIF motion.
