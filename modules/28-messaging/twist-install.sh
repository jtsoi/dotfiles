#!/bin/sh -Cue


. ../../lib/dot.sh

mkdir -p $HOME/Applications

dot_curl_download \
  "https://twist.com/linux_app/appimage" \
  "$HOME/Applications/Twist.AppImage"

chmod +x "$HOME/Applications/Twist.AppImage"

echo ">>> Twist installed"

exec $HOME/Applications/Twist.AppImage
