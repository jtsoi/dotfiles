#!/bin/sh -Cue


. ../../lib/dot.sh

# See https://linrunner.de/tlp/installation/ubuntu.html

sudo add-apt-repository ppa:linrunner/tlp
sudo apt install -y tlp

# Tp14s Recommendations from 'tlp-stat'
sudo apt install acpi-call-dkms smartmontools

sudo cp -f "$DOT_MODULE_FILES_DIR/00-tlp-overrides.conf" "/etc/tlp.d/00-tlp-overrides.conf"

sudo systemctl enable tlp.service