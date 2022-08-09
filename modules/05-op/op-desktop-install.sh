#!/bin/sh -Cue

# Copied from:
#   https://support.1password.com/install-linux/#debian-or-ubuntu


 curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
   sudo gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg

 echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/amd64 stable main' | \
   sudo tee /etc/apt/sources.list.d/1password.list

 sudo mkdir -p /etc/debsig/policies/AC2D62742012EA22/
 sudo mkdir -p /usr/share/debsig/keyrings/AC2D62742012EA22

 curl -sS https://downloads.1password.com/linux/debian/debsig/1password.pol | \
   sudo tee /etc/debsig/policies/AC2D62742012EA22/1password.pol

 curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
   sudo gpg --dearmor --output /usr/share/debsig/keyrings/AC2D62742012EA22/debsig.gpg

sudo apt update && \
  sudo apt install -y 1password