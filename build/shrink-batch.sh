#!/usr/bin/env bash
# Batch-shrink EVERY video in a folder to safely under 10 MB each,
# so they can be pulled through the Google Drive connector.
#
# Usage:
#   build/shrink-batch.sh "/path/to/folder-of-videos"
#   (tip: type the command, then DRAG the folder from Finder into Terminal
#    to paste its path, then press Return)
#
# Output: a "web-shrunk" subfolder inside that folder, each clip an .mp4
#         under ~9 MB (720p, faststart). Originals are left untouched.
set -e

SRC="${1:-.}"
TARGET_MB=9          # aim just under the 10 MB cap (leaves headroom)
AUDIO_K=96           # audio bitrate, kbps
MAXH=720             # cap height at 720p

cd "$SRC"
mkdir -p "web-shrunk"
shopt -s nullglob nocaseglob

count=0
for f in *.mov *.mp4 *.m4v; do
  [ -f "$f" ] || continue
  base="${f%.*}"
  out="web-shrunk/${base}-web.mp4"
  if [ -f "$out" ]; then echo "• skip (already done): $out"; continue; fi

  dur=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$f" 2>/dev/null)
  if [ -z "$dur" ] || [ "$dur" = "N/A" ]; then echo "• skip (no duration): $f"; continue; fi

  # video kbps = (target size in kbits / seconds) - audio ; floor at 200k
  vbit=$(awk "BEGIN{tb=$TARGET_MB*8192; v=tb/$dur - $AUDIO_K; if(v<200)v=200; printf \"%d\", v}")
  echo "==> $f  (${dur%.*}s  ->  video ${vbit}k)"

  # two-pass = accurate size targeting regardless of clip length
  ffmpeg -y -v error -i "$f" -vf "scale=-2:'min($MAXH,ih)'" \
    -c:v libx264 -b:v "${vbit}k" -pass 1 -an -f mp4 /dev/null
  ffmpeg -y -v error -i "$f" -vf "scale=-2:'min($MAXH,ih)'" \
    -c:v libx264 -b:v "${vbit}k" -pass 2 -c:a aac -b:a "${AUDIO_K}k" \
    -movflags +faststart "$out"

  sz=$(du -h "$out" | cut -f1)
  echo "    ✓ $out  ($sz)"
  count=$((count+1))
done

rm -f ffmpeg2pass-*.log ffmpeg2pass-*.log.mbtree 2>/dev/null || true
echo ""
echo "Done. Shrank $count video(s) into: $SRC/web-shrunk"
echo "Now drag the web-shrunk files into your Google Drive folder 03."
