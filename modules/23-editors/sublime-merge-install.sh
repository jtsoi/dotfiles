#!/bin/sh -Cue


. ../../lib/dot.sh

# Copied from
# https://www.sublimemerge.com/docs/linux_repositories

sudo apt-get install -y apt-transport-https  ca-certificates
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

sudo apt-get update
sudo apt-get install -y sublime-merge
