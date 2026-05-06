#!/usr/bin/env python3
"""Download free loop files and bundle into battle ZIP packs.

Usage:
  python assets/loop-packs/download_free_loops.py
"""
from pathlib import Path
from urllib.request import urlopen
import zipfile

ROOT = Path(__file__).parent
TMP = ROOT / "_downloads"
TMP.mkdir(parents=True, exist_ok=True)

# Curated free loop sources (royalty-free / public sample resources).
PACKS = {
    "soul_flip_42": [
        ("https://archive.org/download/musicloopsamples/90bpm-drum-loop.wav", "drum_loop.wav"),
        ("https://archive.org/download/musicloopsamples/90bpm-bass-loop.wav", "bass_loop.wav"),
        ("https://archive.org/download/musicloopsamples/90bpm-keys-loop.wav", "keys_loop.wav"),
    ],
    "drum_surgery_18": [
        ("https://archive.org/download/musicloopsamples/140bpm-drum-loop.wav", "drum_loop.wav"),
        ("https://archive.org/download/musicloopsamples/140bpm-perc-loop.wav", "perc_loop.wav"),
        ("https://archive.org/download/musicloopsamples/140bpm-bass-loop.wav", "bass_loop.wav"),
    ],
    "ambient_trap_09": [
        ("https://archive.org/download/musicloopsamples/75bpm-drum-loop.wav", "drum_loop.wav"),
        ("https://archive.org/download/musicloopsamples/75bpm-pad-loop.wav", "pad_loop.wav"),
        ("https://archive.org/download/musicloopsamples/75bpm-bass-loop.wav", "bass_loop.wav"),
    ],
}

for pack, files in PACKS.items():
    pack_dir = ROOT / pack
    pack_dir.mkdir(parents=True, exist_ok=True)
    readme = pack_dir / "README.txt"
    readme.write_text(
        f"{pack} free loop pack\n"
        "Source: archive.org free sample resources\n"
        "License: verify at source URLs before commercial release\n"
    )

    downloaded = []
    for url, filename in files:
        out = pack_dir / filename
        with urlopen(url) as r:
            out.write_bytes(r.read())
        downloaded.append(out)
        print(f"Downloaded {url} -> {out}")

    zip_path = ROOT / f"{pack}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(readme, arcname="README.txt")
        for f in downloaded:
            zf.write(f, arcname=f.name)
    print(f"Created {zip_path}")
