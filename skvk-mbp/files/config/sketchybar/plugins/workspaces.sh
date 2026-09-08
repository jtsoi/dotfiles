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
        # Filled white with a dark label: an inversion reads at a glance in a
        # way a lighter shade of grey does not, and the focused workspace is the
        # one thing on this bar you look for rather than merely notice.
        args+=(--set "space.$ws" \
               label.color="$ACTIVE_FG" \
               background.color="$ACTIVE_BG" \
               background.border_color="$ACTIVE_BG")
    else
        args+=(--set "space.$ws" \
               label.color="$DIM" \
               background.color="$CHIP_EMPTY" \
               background.border_color="$CHIP_BORDER")
    fi
done

sketchybar "${args[@]}"
