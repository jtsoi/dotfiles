#!/bin/sh -Cue


. ../../lib/dot.sh

sudo snap remove firefox || true

sudo add-apt-repository -y ppa:mozillateam/ppa

sudo apt remove -y firefox



if [ ! -f "/etc/apt/preferences.d/mozilla-firefox" ]
then
  echo '
Package: *
Pin: release o=LP-PPA-mozillateam
Pin-Priority: 1001
' | sudo tee /etc/apt/preferences.d/mozilla-firefox
fi

if [ ! -f "/etc/apt/apt.conf.d/51unattended-upgrades-firefox" ]
then
  echo 'Unattended-Upgrade::Allowed-Origins:: "LP-PPA-mozillateam:${distro_codename}";' | sudo tee /etc/apt/apt.conf.d/51unattended-upgrades-firefox
fi

sudo apt install -y firefox

echo ">>> FF installed"