#!/usr/bin/env python3
"""Export approved raster artwork as RGB JPEG or a validated looping GIF."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from PIL import Image


def load_rgb(path: Path) -> Image.Image:
    with Image.open(path) as image:
        if image.mode in ("RGBA", "LA") or (image.mode == "P" and "transparency" in image.info):
            ground = Image.new("RGB", image.size, "#F7F2E9")
            alpha = image.convert("RGBA")
            ground.paste(alpha, mask=alpha.getchannel("A"))
            return ground
        return image.convert("RGB")


def jpg(source: Path, destination: Path, quality: int) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    load_rgb(source).save(destination, "JPEG", quality=quality, subsampling=0, optimize=True)


def gif(sources: Sequence[Path], destination: Path, delay_ms: int, loop: int) -> None:
    if len(sources) < 2:
        raise ValueError("GIF export needs at least two frames.")
    frames = [load_rgb(path) for path in sources]
    first_size = frames[0].size
    wrong = [str(path) for path, frame in zip(sources, frames) if frame.size != first_size]
    if wrong:
        raise ValueError(f"All GIF frames must be {first_size}; mismatched: {', '.join(wrong)}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        destination,
        "GIF",
        save_all=True,
        append_images=frames[1:],
        duration=delay_ms,
        loop=loop,
        disposal=2,
        optimize=False,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    jpg_parser = sub.add_parser("jpg", help="Flatten and export one image as RGB JPEG")
    jpg_parser.add_argument("source", type=Path)
    jpg_parser.add_argument("destination", type=Path)
    jpg_parser.add_argument("--quality", type=int, default=94, choices=range(1, 96))
    gif_parser = sub.add_parser("gif", help="Compile equally sized frames into a looping GIF")
    gif_parser.add_argument("frames", type=Path, nargs="+")
    gif_parser.add_argument("destination", type=Path)
    gif_parser.add_argument("--delay-ms", type=int, default=100)
    gif_parser.add_argument("--loop", type=int, default=0, help="0 means loop forever")
    args = parser.parse_args()
    if args.command == "jpg":
        jpg(args.source, args.destination, args.quality)
    else:
        gif(args.frames, args.destination, args.delay_ms, args.loop)


if __name__ == "__main__":
    main()
