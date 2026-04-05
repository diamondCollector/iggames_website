"""Resize/compress Forest Planting portfolio images → WebP."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ASSETS = Path(r"C:\Users\DELL\.cursor\projects\d-Cursor-projects-Project-1\assets")
OUT = Path(__file__).resolve().parent.parent / "images" / "forest-planting"

# (source filename, output stem, max width)
HERO_MAX = 1600
STILL_MAX = 1200

JOBS: list[tuple[str, str, int]] = [
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_6795-c2511c07-de10-43d7-b102-e7d3b9298d3a.png",
        "hero",
        HERO_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_6808-03bfadb3-fd40-4ba3-bc1b-bded1e1567c9.png",
        "still-01-aspen-sheet",
        STILL_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_6802-11554cbf-ccce-4616-82dc-fa03237a7531.png",
        "still-02-gameplay",
        STILL_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_4114-b9f42afc-f1ed-4967-ba1a-f01e96c1e927.png",
        "still-03-species-cards",
        STILL_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_4076-4458d354-f4d4-405c-98f1-882aa95c70e4.png",
        "still-04-outdoor-play",
        STILL_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_0-78e126a5-4927-4396-acbc-4bcb0fe85a11.png",
        "still-05-cover-leaves",
        STILL_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_4146-a712c6bd-c239-47d3-93ea-eb80e124219d.png",
        "still-06-tree-miniature",
        STILL_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_4130-e46ad977-8e90-4b17-b389-08dec8d3e99d.png",
        "still-07-board-grass-overhead",
        STILL_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_4119-e4bc1f54-5342-4773-8ebf-8657d8bb02f6.png",
        "still-08-pine-cards-leaves",
        STILL_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_4073-7c68575a-3473-481b-8362-e4193d3f03a2.png",
        "still-09-aspen-sheet-outdoor",
        STILL_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_4092-0f931dd3-3710-4660-9a20-c9efb50da92c.png",
        "still-10-beech-miniature-leaves",
        STILL_MAX,
    ),
    (
        "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_7ba5f8fdae910f0c7bc7ffe579bc2951_images_IMG_6812-9f76170b-738c-4a1e-965a-a0ff8a0be1ee.png",
        "still-11-dice-cubes-grid",
        STILL_MAX,
    ),
]


def resize_max_width(im: Image.Image, max_w: int) -> Image.Image:
    im = im.convert("RGB")
    w, h = im.size
    if w <= max_w:
        return im
    ratio = max_w / w
    new_h = max(1, int(h * ratio))
    return im.resize((max_w, new_h), Image.Resampling.LANCZOS)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for filename, stem, max_w in JOBS:
        src = ASSETS / filename
        if not src.is_file():
            raise SystemExit(f"Missing source: {src}")
        im = Image.open(src)
        im = resize_max_width(im, max_w)
        dest = OUT / f"{stem}.webp"
        im.save(dest, "WEBP", quality=82, method=6)
        print(f"Wrote {dest} ({dest.stat().st_size // 1024} KB)  size={im.size}")


if __name__ == "__main__":
    main()
