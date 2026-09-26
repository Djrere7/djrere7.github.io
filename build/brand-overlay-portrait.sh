#!/usr/bin/env bash
# First Spin branded overlays for PORTRAIT clips (interviews/testimonials).
# Usage: build/brand-overlay-portrait.sh input.mp4 output.mp4 "Subtitle line"
set -e
IN="$1"; OUT="$2"; SUB="${3:-A First Spin Testimonial}"
FD="fonts/Bangers.ttf"
FB="/System/Library/Fonts/Supplemental/Arial Bold.ttf"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
OS=$(awk "BEGIN{printf \"%.2f\", $DUR-4}")
ffmpeg -y -i "$IN" -vf "drawtext=fontfile='$FD':text='FIRST SPIN DJ BOOTCAMP':fontcolor=white:fontsize=w/12:x=40:y=h*0.62:box=1:boxcolor=0x12B3B8@0.9:boxborderw=14:enable='between(t,0.4,5.5)',drawtext=fontfile='$FB':text='$SUB':fontcolor=white:fontsize=w/26:x=46:y=h*0.62+w/8:box=1:boxcolor=black@0.55:boxborderw=10:enable='between(t,0.4,5.5)',drawtext=fontfile='$FD':text='JOIN THE 2027 LIST':fontcolor=white:fontsize=w/12:x=40:y=h*0.62:box=1:boxcolor=0xFF7900@0.92:boxborderw=14:enable='between(t,$OS,$DUR)',drawtext=fontfile='$FB':text='firstspindjbootcamp.org':fontcolor=white:fontsize=w/26:x=46:y=h*0.62+w/8:box=1:boxcolor=black@0.55:boxborderw=10:enable='between(t,$OS,$DUR)'" -c:v libx264 -crf 24 -preset veryfast -movflags +faststart -c:a copy "$OUT"
echo "Branded(portrait) -> $OUT"
