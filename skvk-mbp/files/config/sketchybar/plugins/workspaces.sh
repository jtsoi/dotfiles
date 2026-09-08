#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
#
# Highlights the focused workspace. Driven only by the aerospace_focus event, so
# it costs nothing while nothing changes. One sketchybar invocation for all
# twelve items rather than twelve.
set -euo pipefail

# shellcheck source=SCRIPTDIR/../colors.sh
source "$HOME/.config/sketchybar/colors.sh"

focused=$(aerospace list-workspaces --focused)

args=()
for ws in 1 2 3 4 5 6 7 8 9 M L S; do
    if [ "$ws" = "$focused" ]; then
        # A chip as well as a colour: the focused workspace is the one thing on
        # the bar you look for rather than notice.
        args+=(--set "space.$ws" label.color="$ACCENT" background.drawing=on)
    else
        args+=(--set "space.$ws" label.color="$DIM" background.drawing=off)
    fi
done

sketchybar "${args[@]}"
