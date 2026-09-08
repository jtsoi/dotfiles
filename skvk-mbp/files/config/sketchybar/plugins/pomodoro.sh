#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
#
# State is an absolute epoch end-time, not a countdown, which is what makes this
# wall-clock: a lid closed for ten minutes of a 25m block leaves fifteen, and a
# sketchybar restart picks the same block back up. Paused state stores remaining
# seconds instead, so a pause survives a restart too.
set -euo pipefail

# shellcheck source=SCRIPTDIR/../colors.sh
source "$HOME/.config/sketchybar/colors.sh"

WORK=$((25 * 60))
STATE_DIR="${XDG_STATE_HOME:-$HOME/.local/state}/sketchybar"
STATE="$STATE_DIR/pomodoro"

mkdir -p "$STATE_DIR"
[ -f "$STATE" ] || printf 'idle 0\n' > "$STATE"

read -r mode value < "$STATE"
now=$(date +%s)

write() { printf '%s %s\n' "$1" "$2" > "$STATE"; }

fmt() { printf '%d:%02d' $(($1 / 60)) $(($1 % 60)); }

case "${SENDER:-}" in
    mouse.clicked)
        case "${BUTTON:-left}" in
            right)
                write idle 0
                ;;
            *)
                case "$mode" in
                    running) write paused $((value - now)) ;;
                    paused)  write running $((now + value)) ;;
                    *)       write running $((now + WORK)) ;;
                esac
                ;;
        esac
        read -r mode value < "$STATE"
        ;;
esac

case "$mode" in
    running)
        remaining=$((value - now))
        if [ "$remaining" -le 0 ]; then
            write idle 0
            mode=idle
            remaining=$WORK
            /usr/bin/osascript -e 'display notification "Work block done" with title "Pomodoro" sound name "Glass"' >/dev/null 2>&1 || true
        fi
        ;;
    paused)  remaining=$value ;;
    *)       remaining=$WORK ;;
esac

case "$mode" in
    running)
        icon="▶"
        color="$FG"
        [ "$remaining" -le 60 ] && color="$WARN"
        freq=1
        ;;
    paused)
        icon="⏸"
        color="$DIM"
        # Nothing changes while paused, so stop waking every second.
        freq=0
        ;;
    *)
        icon="○"
        color="$DIM"
        freq=0
        ;;
esac

sketchybar --set "$NAME" \
    icon="$icon" \
    icon.color="$color" \
    label="$(fmt "$remaining")" \
    label.color="$color" \
    update_freq="$freq"
