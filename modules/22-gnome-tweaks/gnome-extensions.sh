#!/bin/sh -Cue


. ../../lib/dot.sh

# Install tweaks app
sudo apt update
sudo apt install -y gnome-tweaks gnome-shell-extensions

# Install installer
wget -O /tmp/gnome-shell-extension-installer "https://github.com/brunelli/gnome-shell-extension-installer/raw/master/gnome-shell-extension-installer"
chmod +x /tmp/gnome-shell-extension-installer
sudo mv /tmp/gnome-shell-extension-installer /usr/local/bin/

# Disable version validation
gsettings set org.gnome.shell disable-extension-version-validation true

# Dash to panel https://extensions.gnome.org/extension/1160/dash-to-panel/
gnome-shell-extension-installer 1160

# Workspace indicator https://extensions.gnome.org/extension/3968/improved-workspace-indicator/
# gnome-shell-extension-installer 3968

# Space-bar (named workspaces) https://extensions.gnome.org/extension/5090/space-bar/
gnome-shell-extension-installer 5090

# Clock format https://extensions.gnome.org/extension/3465/panel-date-format/
gnome-shell-extension-installer 3465

# top bar organizer https://extensions.gnome.org/extension/4356/top-bar-organizer/
# gnome-shell-extension-installer 4356

# Clipboard indicator https://extensions.gnome.org/extension/779/clipboard-indicator/
gnome-shell-extension-installer 779

# Just Perfection extension https://extensions.gnome.org/extension/3843/just-perfection/
# not needed - dash-to-panel is better
# gnome-shell-extension-installer 3843

# Custom clock format https://extensions.gnome.org/extension/4655/date-menu-formatter/
gnome-shell-extension-installer 4655

# Multiple timezones https://extensions.gnome.org/extension/2657/timezones-extension/
# not great for this use case
# gnome-shell-extension-installer 2657