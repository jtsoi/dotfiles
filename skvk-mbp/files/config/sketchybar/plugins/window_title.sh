#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
#
# Nothing else on screen names the focused window: AeroSpace draws no titles and
# Alacritty runs decorations = "None".
set -euo pipefail

title=$(aerospace list-windows --focused --format '%{window-title}' 2>/dev/null || true)

sketchybar --set "$NAME" label="${title:-}"
