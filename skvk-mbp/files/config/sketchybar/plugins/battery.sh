#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
set -euo pipefail

# shellcheck source=SCRIPTDIR/../colors.sh
source "$HOME/.config/sketchybar/colors.sh"

batt=$(pmset -g batt)
pct=$(printf '%s' "$batt" | grep -oE '[0-9]+%' | head -1 | tr -d '%')

color="$FG"
# Line one reads `Now drawing from 'AC Power'` or `'Battery Power'`.
case "$batt" in
    *"'AC Power'"*) color="$OK" ;;
esac
if [ "$pct" -lt 10 ]; then
    color="$CRIT"
elif [ "$pct" -lt 20 ]; then
    color="$WARN"
fi

sketchybar --set "$NAME" label="${pct}%" label.color="$color"
