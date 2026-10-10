#!/bin/bash
# Round 2, step B: upload approved clips with retries, then back them up.
W=/tmp/tgbr2; cd $W; GH=$HOME/.local/bin/gh; R=jasonjermain2298-stack/tgb-shop-tv
for pass in 1 2 3 4 5 6; do miss=0
  have=$($GH api repos/$R/releases/tags/media-v1 --jq '.assets[]|select(.state=="uploaded")|.name')
  for f in fv-*.mp4 40-inbox-*.mp4; do [ -f "$f" ] || continue; [ -f "$f.skip" ] && continue
    echo "$have" | grep -qx "$f" && continue; miss=1; $GH release upload media-v1 "$f" -R $R --clobber && echo "ok $f"; done
  [ $miss = 0 ] && break; sleep 20; done
L="$HOME/Documents/TGB_Shop_TV/Videos"; G="$HOME/Library/CloudStorage/GoogleDrive-jasonjermain2298@gmail.com/My Drive/TGB_Shop_TV/Videos"
mkdir -p "$L" "$G"; for f in fv-*.mp4 40-inbox-*.mp4; do [ -f "$f" ] && [ ! -f "$f.skip" ] && cp -f "$f" "$L/" && cp -f "$f" "$G/"; done
echo UPLOAD_DONE
