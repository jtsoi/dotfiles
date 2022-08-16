#!/bin/sh -Cue


. ../../lib/dot.sh

# Install app
# wmctrl needed for custom shortcut to work
sudo add-apt-repository -y ppa:agornostal/ulauncher && sudo apt install -y ulauncher wmctrl
