#!/bin/sh -Cue


. ../../lib/dot.sh

dot_curl_download \
  "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" \
  "/tmp/google-chrome-stable_current_amd64.deb"
  
sudo dpkg -i "/tmp/google-chrome-stable_current_amd64.deb"


echo ">>> Chrome installed"