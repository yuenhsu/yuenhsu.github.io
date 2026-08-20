#!/usr/bin/env bash
# Compress raster images in place (lossy, visually near-identical) to cut page weight.
# Requires: pngquant, jpegoptim, gifsicle (brew install pngquant jpegoptim gifsicle)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

EXCLUDE_DIRS=(-path ./.git -o -path ./_site -o -path ./.quarto -o -path ./.venv -o -path ./node_modules)

echo "== PNG (pngquant, quality 65-85) =="
find . \( "${EXCLUDE_DIRS[@]}" \) -prune -o -iname "*.png" -print | while read -r f; do
  before=$(stat -f%z "$f")
  pngquant --quality=65-85 --speed 1 --strip --force --output "$f" "$f" || true
  after=$(stat -f%z "$f")
  echo "$f: $before -> $after bytes"
done

echo "== JPEG (jpegoptim, max quality 82) =="
find . \( "${EXCLUDE_DIRS[@]}" \) -prune -o \( -iname "*.jpg" -o -iname "*.jpeg" \) -print | while read -r f; do
  jpegoptim --max=82 --strip-all --all-progressive "$f"
done

echo "== GIF (gifsicle -O3 --lossy) =="
find . \( "${EXCLUDE_DIRS[@]}" \) -prune -o -iname "*.gif" -print | while read -r f; do
  before=$(stat -f%z "$f")
  gifsicle -O3 --lossy=80 --colors 128 "$f" -o "$f"
  after=$(stat -f%z "$f")
  echo "$f: $before -> $after bytes"
done

echo "Done."
