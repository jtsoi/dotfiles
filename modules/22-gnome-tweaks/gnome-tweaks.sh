#!/bin/sh -Cue


. ../../lib/dot.sh


# Notes
#   - use 'xev' to find key codes
#   - 'dconf reset -f /org/gnome/' to reset all settings

# Set "Correct" scroll directon
gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll false

# Enable static workspaces (12)
gsettings set org.gnome.mutter dynamic-workspaces false
gsettings set org.gnome.desktop.wm.preferences num-workspaces 12

# Name static workspaces
gsettings set org.gnome.desktop.wm.preferences workspace-names "['1t','2c','3w','4t','5c','6w','7t','8c','9w','10g','11p','12m']"

# Isolate worspaces and monitors
gsettings set org.gnome.shell.app-switcher current-workspace-only true
gsettings set org.gnome.shell.extensions.dash-to-dock isolate-monitors true

# Enable workspaces on all displays
gsettings set org.gnome.mutter workspaces-only-on-primary false

# Rebind navigate workspace keys (Super+#)
## Unset Super+# keys 
gsettings set org.gnome.shell.keybindings switch-to-application-1 "[]"
gsettings set org.gnome.shell.keybindings switch-to-application-2 "[]"
gsettings set org.gnome.shell.keybindings switch-to-application-3 "[]"
gsettings set org.gnome.shell.keybindings switch-to-application-4 "[]"
gsettings set org.gnome.shell.keybindings switch-to-application-5 "[]"
gsettings set org.gnome.shell.keybindings switch-to-application-6 "[]"
gsettings set org.gnome.shell.keybindings switch-to-application-7 "[]"
gsettings set org.gnome.shell.keybindings switch-to-application-8 "[]"
gsettings set org.gnome.shell.keybindings switch-to-application-9 "[]"
## Set Super+# keys to switch workspaces
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-1  "['<Super>1']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-2  "['<Super>2']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-3  "['<Super>3']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-4  "['<Super>4']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-5  "['<Super>5']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-6  "['<Super>6']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-7  "['<Super>7']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-8  "['<Super>8']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-9  "['<Super>9']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-10 "['<Super>0']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-11 "['<Super>Minus']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-12 "['<Super>Equal']"
## Set Super+Shift+# keys to switch workspaces
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-1  "['<Super><Shift>1']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-2  "['<Super><Shift>2']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-3  "['<Super><Shift>3']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-4  "['<Super><Shift>4']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-5  "['<Super><Shift>5']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-6  "['<Super><Shift>6']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-7  "['<Super><Shift>7']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-8  "['<Super><Shift>8']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-9  "['<Super><Shift>9']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-10 "['<Super><Shift>0']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-11 "['<Super><Shift>Minus']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-12 "['<Super><Shift>Equal']"

## Rebind navigate workspace keys (Super+Ctrl+Left/Right)
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-left  "['<Super><Ctrl>Left']"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-right "['<Super><Ctrl>Right']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-left  "['<Super><Ctrl><Shift>Left']"
gsettings set org.gnome.desktop.wm.keybindings move-to-workspace-right "['<Super><Ctrl><Shift>Right']"

# Rebind Super+Tab to toggle between workspaces
gsettings set org.gnome.desktop.wm.keybindings switch-applications-backward "[]"
gsettings set org.gnome.desktop.wm.keybindings switch-applications "[]"
gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-last "[]"
# TODO: Maybe use this to switch between workspaces instead.

# Super Enter to start terminal
gsettings set org.gnome.settings-daemon.plugins.media-keys terminal "['<Super>Return']"

# Super+Q to close window
gsettings set org.gnome.desktop.wm.keybindings close "['<Super>q']"

# Suspend on Super+Shift+s
gsettings set org.gnome.settings-daemon.plugins.media-keys suspend "['<Super><Shift>s']"

# Custom key bindings
gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings "[\
  '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/'\
]"

## 0 - ULauncher 
### Unset Super+Space combo
gsettings set org.freedesktop.ibus.general.hotkey triggers "[]"
gsettings set org.gnome.desktop.wm.keybindings switch-input-source "['XF86Keyboard']"
gsettings set org.gnome.desktop.wm.keybindings switch-input-source-backward "['<Shift>XF86Keyboard']"
### Create custom shortcut for ULauncher
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name "'ulauncher'"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command "'/usr/bin/ulauncher-toggle'"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding "'<Super>space'"
