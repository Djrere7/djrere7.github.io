#!/usr/bin/env bash
# First Spin branded overlays — intro lower-third + closing CTA on a landscape video.
# Usage: build/brand-overlay.sh input.mp4 output.mp4
set -e
IN="$1"; OUT="$2"
FD="fonts/Bangers.ttf"                                  # display (brand, OFL)
FB="/System/Library/Fonts/Supplemental/Arial Bold.ttf" # body (rendered to pixels only)
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
OS=$(awk "BEGIN{printf \"%.2f\", $DUR-5}")
ffmpeg -y -i "$IN" -vf "drawtext=fontfile='$FD':text='FIRST SPIN DJ BOOTCAMP':fontcolor=white:fontsize=h/14:x=60:y=h-h/4:box=1:boxcolor=0x12B3B8@0.9:boxborderw=18:enable='between(t,0.4,6)',drawtext=fontfile='$FB':text='Free Summer DJ Education for Ages 7+':fontcolor=white:fontsize=h/34:x=66:y=h-h/8:box=1:boxcolor=black@0.55:boxborderw=12:enable='between(t,0.4,6)',drawtext=fontfile='$FD':text='JOIN THE 2027 INTEREST LIST':fontcolor=white:fontsize=h/14:x=60:y=h-h/4:box=1:boxcolor=0xFF7900@0.92:boxborderw=18:enable='between(t,$OS,$DUR)',drawtext=fontfile='$FB':text='firstspindjbootcamp.org':fontcolor=white:fontsize=h/34:x=66:y=h-h/8:box=1:boxcolor=black@0.55:boxborderw=12:enable='between(t,$OS,$DUR)'" -c:v libx264 -crf 24 -preset veryfast -movflags +faststart -c:a copy "$OUT"
echo "Branded -> $OUT"
