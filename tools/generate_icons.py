#!/usr/bin/env python3
"""Generate the PWA app icons under assets/icons/ from a simple drawn
coffee-cup glyph, matching the brand accent color used across index.html
(--accent: #7d1d2f) and its brand-mark SVG. Run manually after changing the
brand color; output is checked into git like any other static asset.

Usage: python3 tools/generate_icons.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

ACCENT = (125, 29, 47, 255)  # #7d1d2f
WHITE = (255, 255, 255, 255)
OUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "icons"


def draw_cup(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color) -> None:
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    body = (x0 + w * 0.08, y0 + h * 0.12, x0 + w * 0.68, y0 + h * 0.62)
    draw.rounded_rectangle(body, radius=w * 0.08, outline=color, width=max(2, int(w * 0.055)))
    cx1, cy1, cx2, cy2 = body[2], y0 + h * 0.2, x0 + w * 0.86, y0 + h * 0.46
    draw.arc([cx1 - w * 0.02, cy1, cx2, cy2], start=300, end=120, fill=color, width=max(2, int(w * 0.055)))
    saucer_y = body[3] + h * 0.05
    draw.line([x0 + w * 0.02, saucer_y, x0 + w * 0.74, saucer_y], fill=color, width=max(2, int(w * 0.05)))
    steam_w = max(2, int(w * 0.04))
    for sx in (0.22, 0.38, 0.54):
        sx0 = x0 + w * sx
        draw.line(
            [(sx0, y0 + h * 0.06), (sx0 - w * 0.03, y0 - h * 0.0), (sx0, y0 - h * 0.04)],
            fill=color,
            width=steam_w,
            joint="curve",
        )


def make_icon(size: int, maskable: bool) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    if maskable:
        draw.rectangle([0, 0, size, size], fill=ACCENT)
        safe_margin = size * 0.18
    else:
        radius = size * 0.22
        draw.rounded_rectangle([0, 0, size, size], radius=radius, fill=ACCENT)
        safe_margin = size * 0.14
    draw_cup(draw, (safe_margin, safe_margin, size - safe_margin, size - safe_margin), WHITE)
    return img


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    make_icon(192, maskable=False).save(OUT_DIR / "icon-192.png")
    make_icon(512, maskable=False).save(OUT_DIR / "icon-512.png")
    make_icon(512, maskable=True).save(OUT_DIR / "icon-maskable-512.png")
    make_icon(180, maskable=False).save(OUT_DIR / "apple-touch-icon.png")
    print(f"Wrote icons to {OUT_DIR}")


if __name__ == "__main__":
    main()
