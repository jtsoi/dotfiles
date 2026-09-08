#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
#
# 1-minute load average, not a percentage: a true CPU% needs sampling across an
# interval (`top -l 2` costs about a second) which a 5-second item cannot
# afford. Load only means anything against core count, so that is the threshold.
set -euo pipefail

# shellcheck source=SCRIPTDIR/../colors.sh
source "$HOME/.config/sketchybar/colors.sh"

# sysctl prints `{ 4.32 3.17 3.06 }`, so the 1-minute figure is field 2.
load1=$(sysctl -n vm.loadavg | awk '{print $2}')
ncpu=$(sysctl -n hw.ncpu)

color="$FG"
if awk -v l="$load1" -v n="$ncpu" 'BEGIN { exit !(l > n) }'; then
    color="$WARN"
fi

sketchybar --set "$NAME" label="load $load1" label.color="$color"
