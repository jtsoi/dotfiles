#!/bin/sh -Cue

. ../../lib/dot.sh

sudo add-apt-repository ppa:appimagelauncher-team/stable

sudo apt update

sudo apt install -y \
  appimagelauncher
