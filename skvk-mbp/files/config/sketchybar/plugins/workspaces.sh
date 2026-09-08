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

# Slack's Dock badge is the unread signal. lsappinfo reports the very label
# Slack puts on its own icon, which costs no permission, no database and no API
# token -- the alternatives are the Notification Centre store, which needs Full
# Disk Access and exposes notification content, or a Slack token to keep.
#
# Empty covers three cases that all mean "nothing waiting": no unread, badges
# switched off for Slack in System Settings, and Slack not running. The middle
# one is worth knowing about, since it reads as all-clear while being no
# information at all. The label is treated as an opaque string because Slack
# shows a dot rather than a count in some configurations.
slack_badge=$(/usr/bin/lsappinfo info -only StatusLabel "${SLACK_APP:-Slack}" 2>/dev/null |
    sed -n 's/.*"label"="\([^"]*\)".*/\1/p')

args=()
for ws in 1 2 3 4 5 6 7 8 9 L M S; do
    if [ "$ws" = "$focused" ]; then
        # Filled white with a dark label: an inversion reads at a glance in a
        # way a lighter shade of grey does not, and the focused workspace is the
        # one thing on this bar you look for rather than merely notice.
        #
        # Focus wins over unread deliberately: you are looking at the workspace,
        # so the badge is moot, and a white border on a white fill says nothing.
        args+=(--set "space.$ws" \
               label.color="$ACTIVE_FG" \
               background.color="$ACTIVE_BG" \
               background.border_color="$ACTIVE_BG")
    elif [ "$ws" = "S" ] && [ -n "$slack_badge" ]; then
        args+=(--set "space.$ws" \
               label.color="$DIM" \
               background.color="$CHIP_EMPTY" \
               background.border_color="$UNREAD")
    else
        args+=(--set "space.$ws" \
               label.color="$DIM" \
               background.color="$CHIP_EMPTY" \
               background.border_color="$CHIP_BORDER")
    fi
done

sketchybar "${args[@]}"
