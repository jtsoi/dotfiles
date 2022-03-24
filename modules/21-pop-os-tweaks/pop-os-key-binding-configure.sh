#!/bin/sh -Cue


. ../../lib/dot.sh

POP_OS_TILING_GROUP='org.gnome.mutter.keybindings'
POP_OS_SHELL_GROUP='org.gnome.shell.extensions.pop-shell'

GNOME_GROUP='org.gnome.desktop.wm.keybindings'

NOT_SET="[]"

set_gnome_key_binding()
{
    gsettings set $1 $2 $3
    echo "Key binding $2 to $3"
}

# Unbind conflicting PopOS Bindings
set_gnome_key_binding $POP_OS_TILING_GROUP toggle-tiled-right $NOT_SET
set_gnome_key_binding $POP_OS_TILING_GROUP toggle-tiled-left $NOT_SET
set_gnome_key_binding $POP_OS_SHELL_GROUP pop-monitor-down $NOT_SET

# Add Workpace left-right navigation
set_gnome_key_binding $GNOME_GROUP switch-to-workspace-right "['<Primary><Super>Right']"
set_gnome_key_binding $GNOME_GROUP switch-to-workspace-left "['<Primary><Super>Left']"

# Add move-to-workpace bindings
set_gnome_key_binding $GNOME_GROUP move-to-workspace-left "['<Primary><Shift><Super>Left']"
set_gnome_key_binding $GNOME_GROUP move-to-workspace-right "['<Primary><Shift><Super>Right']"
set_gnome_key_binding $GNOME_GROUP move-to-workspace-up "['<Primary><Shift><Super>Up']"
set_gnome_key_binding $GNOME_GROUP move-to-workspace-down "['<Primary><Shift><Super>Down']"
