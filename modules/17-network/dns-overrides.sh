#!/bin/sh -Cue
. ../../lib/dot.sh

# Enable 'skovik.dev'
sudo cp "$DOT_MODULE_FILES_DIR/skovik-domains.conf" /etc/NetworkManager/dnsmasq.d/skovik-domains.conf

# Enable dnsmasq shipped with NetworkManager
sudo cp "$DOT_MODULE_FILES_DIR/00-enable-dnsmasq.conf" /etc/NetworkManager/conf.d/00-enable-dnsmasq.conf
sudo systemctl restart NetworkManager

# Ensure /etc/systemd/resolved.conf.d/ dir exists
sudo mkdir -p /etc/systemd/resolved.conf.d/
sudo cp "$DOT_MODULE_FILES_DIR/00-resolve-dnsmasq.conf" /etc/systemd/resolved.conf.d/00-resolve-dnsmasq.conf

# Restart for effect
sudo systemctl restart systemd-resolved

echo ">>> DNS overrides installed"
