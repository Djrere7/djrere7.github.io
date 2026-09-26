#!/usr/bin/env bash
# First Spin caption burner — burns styled, on-brand captions into a video.
# Usage:
#   build/caption.sh input.mp4 captions.srt output.mp4
#
# Where captions.srt is a standard SubRip file, e.g.:
#   1
#   00:00:00,000 --> 00:00:02,500
#   First Spin gave me my first shot at DJing.
#
# Get an .srt fast (no coding): CapCut "Auto captions" → Export SRT, or
# veed.io, or YouTube Studio → Subtitles → Download. Then run this to burn
# clean captions in First Spin style (bold white text on a dark bar, lower third).
set -e
IN="$1"; SRT="$2"; OUT="$3"
if [ -z "$IN" ] || [ -z "$SRT" ] || [ -z "$OUT" ]; then
  echo "Usage: build/caption.sh input.mp4 captions.srt output.mp4"; exit 1
fi
# Font: Montserrat if installed, else a safe system font. Colours are ASS &HAABBGGRR.
ffmpeg -y -i "$IN" -vf "subtitles=${SRT}:force_style='FontName=Montserrat,FontSize=24,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=3,BackColour=&HB3000000,Outline=1,Shadow=0,MarginV=48,Alignment=2'" \
  -c:v libx264 -crf 24 -preset veryfast -movflags +faststart -c:a copy "$OUT"
echo "Captioned → $OUT"
