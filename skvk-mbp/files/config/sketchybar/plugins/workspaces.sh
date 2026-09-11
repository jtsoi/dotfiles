#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
#
# Highlights the focused workspace. Driven only by the aerospace_focus event, so
# it costs nothing while nothing changes. One sketchybar invocation for all
# twelve items rather than twelve.
set -euo pipefail

# True only for a badge that counts something addressed to you. A Dock badge
# carries either a count or a bare dot and lsappinfo returns whichever verbatim
# -- Linear is the app on this Mac that shows a dot -- while Slack reserves the
# count for highlights: DMs, mentions, keywords and replies in followed threads.
# So the leading character is the whole distinction, and a dot, an empty label
# and a literal 0 all mean nothing is waiting.
#
# A leading digit rather than a numeric test on the whole label, so a capped
# form like "99+" still counts. That is the case where a dark chip would be
# worst.
#
# It cannot narrow further to DMs alone. The badge merges them with mentions and
# offers no breakdown, and the only source that does is the Slack Web API, which
# wants a user token with im:read and a request per DM conversation.
unread_badge() {
    case "$1" in
        [1-9]*) return 0 ;;
        *)      return 1 ;;
    esac
}

# Sets the global `state` to one of focused, unread or idle.
#
# Focus wins over unread deliberately: you are looking at the workspace, so the
# badge is moot, and a white border on a white fill says nothing.
chip_state() {
    local ws="$1" focused="$2" badge="$3"

    if [ "$ws" = "$focused" ]; then
        state=focused
    elif [ "$ws" = 'S' ] && unread_badge "$badge"; then
        state=unread
    else
        state=idle
    fi
}

# `probe` prints one chip's state without touching the bar or reading Slack. It
# is the seam the verify harness asserts the rule through, so the rule is never
# restated anywhere it can drift from the one that runs.
if [ "${1:-}" = probe ]; then
    chip_state "${2:-}" "${3:-}" "${4:-}"
    printf '%s\n' "$state"
    exit 0
fi

# Below the probe branch for the reason windows.sh orders these the same way:
# this path is a symlink into the repo, so it resolves only where the module has
# been applied, and the harness probes on machines where it may not have been.
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
# information at all.
slack_badge=$(/usr/bin/lsappinfo info -only StatusLabel "${SLACK_APP:-Slack}" 2>/dev/null |
    sed -n 's/.*"label"="\([^"]*\)".*/\1/p')

args=()
for ws in 1 2 3 4 5 6 7 8 9 L M S; do
    chip_state "$ws" "$focused" "$slack_badge"
    case "$state" in
        # Filled white with a dark label: an inversion reads at a glance in a
        # way a lighter shade of grey does not, and the focused workspace is the
        # one thing on this bar you look for rather than merely notice.
        focused) args+=(--set "space.$ws" \
                        label.color="$ACTIVE_FG" \
                        background.color="$ACTIVE_BG" \
                        background.border_color="$ACTIVE_BG") ;;
        unread)  args+=(--set "space.$ws" \
                        label.color="$DIM" \
                        background.color="$CHIP_EMPTY" \
                        background.border_color="$UNREAD") ;;
        idle)    args+=(--set "space.$ws" \
                        label.color="$DIM" \
                        background.color="$CHIP_EMPTY" \
                        background.border_color="$CHIP_BORDER") ;;
    esac
done

sketchybar "${args[@]}"
