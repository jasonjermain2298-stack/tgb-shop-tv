#!/bin/bash
# Round 2, step A: build clips + review sheets (no upload). Run on the Mac.
W=/tmp/tgbr2; mkdir -p $W; cd $W
D="$HOME/Library/CloudStorage/GoogleDrive-jasonjermain2298@gmail.com/My Drive"
INBOX="$D/TGB_Shop_TV/Inbox"; mkdir -p "$INBOX"
enc(){ ffmpeg -nostdin -y -loglevel error -i "$1" -an -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=0x0A0A0A,setsar=1,fps=30" -c:v libx264 -preset medium -crf 24 -maxrate 1500k -bufsize 3M -pix_fmt yuv420p -movflags +faststart "$2"; }
sheet(){ d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$1"); ffmpeg -nostdin -y -loglevel error -i "$1" -vf "fps=8/$d,scale=-2:140,tile=8x1" -frames:v 1 "${1%.mp4}.jpg"; }
n=0
find "$D" -name "FULL-VOLUME-TOP9-*16x9.mp4" -size +100k 2>/dev/null | sort | while IFS= read -r f; do
  n=$((n+1)); o=$(printf "fv-%02d.mp4" $n); cat "$f" >/dev/null; enc "$f" $o && sheet $o; done
k=0
find "$INBOX" -type f \( -iname "*.mov" -o -iname "*.mp4" -o -iname "*.m4v" \) 2>/dev/null | sort | while IFS= read -r f; do
  k=$((k+1)); o=$(printf "40-inbox-%02d.mp4" $k); cat "$f" >/dev/null; enc "$f" $o && sheet $o; echo "$o <- $f" >> inbox-map.txt; done
ls -l $W/*.mp4; echo BUILD_DONE
