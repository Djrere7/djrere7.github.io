#!/usr/bin/env bash
# ============================================================
#  Shrink Videos for Web  —  double-click me
#  Pops up a folder picker, then shrinks EVERY video in that
#  folder to safely under 10 MB (720p .mp4) into a "web-shrunk"
#  subfolder. Originals are never touched.
# ============================================================

# Make sure ffmpeg/ffprobe are found even on a bare double-click.
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"

TARGET_MB=9      # aim just under the 10 MB cap
AUDIO_K=96       # audio bitrate, kbps
MAXH=720         # cap height at 720p

# --- pick the folder with a normal Mac dialog ---
SRC=$(osascript -e 'POSIX path of (choose folder with prompt "Pick the folder of videos to shrink:")' 2>/dev/null)
if [ -z "$SRC" ]; then
  echo "No folder chosen. You can close this window."
  exit 0
fi

if ! command -v ffmpeg >/dev/null 2>&1; then
  osascript -e 'display alert "ffmpeg not found" message "Could not locate ffmpeg. Tell Claude and it will fix the path."' >/dev/null 2>&1
  echo "ffmpeg not found on PATH."; exit 1
fi

cd "$SRC" || { echo "Cannot open $SRC"; exit 1; }
mkdir -p "web-shrunk"
shopt -s nullglob nocaseglob

echo "Shrinking videos in: $SRC"
echo "-----------------------------------------------"
count=0
for f in *.mov *.mp4 *.m4v; do
  [ -f "$f" ] || continue
  base="${f%.*}"
  out="web-shrunk/${base}-web.mp4"
  if [ -f "$out" ]; then echo "• skip (already done): ${base}-web.mp4"; continue; fi

  dur=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$f" 2>/dev/null)
  if [ -z "$dur" ] || [ "$dur" = "N/A" ]; then echo "• skip (unreadable): $f"; continue; fi

  vbit=$(awk "BEGIN{tb=$TARGET_MB*8192; v=tb/$dur - $AUDIO_K; if(v<200)v=200; printf \"%d\", v}")
  echo "==> $f  (${dur%.*}s)"

  ffmpeg -y -v error -i "$f" -vf "scale=-2:'min($MAXH,ih)'" \
    -c:v libx264 -b:v "${vbit}k" -pass 1 -an -f mp4 /dev/null
  ffmpeg -y -v error -i "$f" -vf "scale=-2:'min($MAXH,ih)'" \
    -c:v libx264 -b:v "${vbit}k" -pass 2 -c:a aac -b:a "${AUDIO_K}k" \
    -movflags +faststart "$out"

  sz=$(du -h "$out" | cut -f1)
  echo "    done -> ${base}-web.mp4  ($sz)"
  count=$((count+1))
done

rm -f ffmpeg2pass-*.log ffmpeg2pass-*.log.mbtree 2>/dev/null || true
echo "-----------------------------------------------"
echo "Finished. Shrank $count video(s)."

# Open the results folder and show a friendly popup.
open "$SRC/web-shrunk" 2>/dev/null || true
osascript -e "display notification \"Shrank $count videos into web-shrunk\" with title \"Videos ready for Drive\"" >/dev/null 2>&1
echo ""
echo "The shrunk files are in the 'web-shrunk' folder that just opened."
echo "Drag them into Google Drive folder 03. You can close this window."
