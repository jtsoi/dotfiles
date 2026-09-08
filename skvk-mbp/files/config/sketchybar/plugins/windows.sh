#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
#
# Paints the focused workspace's windows as chips in the centre of the bar.
#
# `probe` prints one window's glyph and label without touching the bar. It is
# the seam the verify harness asserts the rules through: without it the harness
# would have to restate the case block below, and a restated rule drifts from
# the one that runs.
set -euo pipefail

# The cap counts characters, but ${#s} and ${s:0:n} count bytes unless a UTF-8
# locale is set. Apple's /bin/bash 3.2 slices "Åland — naïve" mid-character
# without this; Homebrew's bash 5 happens not to, which is a difference no
# reader should have to know about. The pattern strips below need no pin --
# they match literal bytes.
export LC_ALL=en_US.UTF-8

CAP=12

# One entry per app: its icon ligature, and the one fragment of its title worth
# showing in a chip this narrow. Keyed on bundle id rather than app name --
# stable across renames and localisation, and it is what list-windows returns.
#
# Alacritty takes the generic :terminal: rather than its own logo, so the chip
# reads "a terminal, in this directory" and stays right if the emulator changes.
#
# Sets the globals `glyph` and `label`.
chip_for() {
    local bid="$1" app="$2" title="$3" t
    case "$bid" in
        com.microsoft.VSCode)      glyph=':code:'          ; label="${title##* — }" ;;
        org.alacritty)             glyph=':terminal:'      ; label="${title##*: }" ;;
        com.sublimemerge)          glyph=':sublime_merge:' ; label="${title##*/}" ;;
        com.linear)                glyph=':linear:'        ; label="${title%% *}" ;;
        com.tinyspeck.slackmacgap) glyph=':slack:'         ; label="${title%% - *}" ;;
        com.google.Chrome)         glyph=':google_chrome:' ; t="${title% - Google Chrome}"
                                                             label="${t%% | *}" ;;
        # No entry: a generic window mark and the app's own name. Not a bare
        # initial -- two unknown apps would then look identical, and the glyph
        # already says "this app has no icon".
        *)                         glyph=':default:'       ; label="$app" ;;
    esac

    # A VS Code window with no folder open reports its project as
    # "Untitled (Workspace)". The filename is the only thing that distinguishes
    # one such window from another.
    if [ "$label" = 'Untitled (Workspace)' ]; then
        label="${title%% — *}"
    fi

    if [ "${#label}" -gt "$CAP" ]; then
        label="${label:0:$((CAP - 1))}…"
    fi
}

if [ "${1:-}" = probe ]; then
    chip_for "${2:-}" "${3:-}" "${4:-}"
    printf '%s|%s\n' "$glyph" "$label"
    exit 0
fi

# Below the probe branch on purpose. This path is a symlink into the repo, so it
# only resolves on a machine where the module has been applied -- and the verify
# harness calls `probe` on machines where it may not have been. Sourcing above
# the branch would fail eight probe checks for a reason that has nothing to do
# with the probe.
# shellcheck source=SCRIPTDIR/../colors.sh
source "$HOME/.config/sketchybar/colors.sh"

SLOTS=5

# Exits 2 with "No window is focused" on an empty workspace, which set -e would
# turn into a dead plugin and a centre group still showing the last workspace's
# windows -- stale, drawn, and clickable. Four of the twelve workspaces are
# empty, so this is the common path.
focused=$(aerospace list-windows --focused --format '%{window-id}' 2>/dev/null || true)

# Deliberately unguarded: this one exits 0 with empty output on an empty
# workspace, so a non-zero status here is a real failure and should be loud
# rather than rendering as "no windows".
windows=$(aerospace list-windows --workspace focused \
    --format '%{window-id}|%{app-bundle-id}|%{app-name}|%{window-title}')

# Whatever order list-windows returns, which groups by app. AeroSpace exposes no
# tiling index -- `focus --dfs-index` exists but there is no matching --format
# placeholder -- so this is the only order available.
#
# What matters is that it is stable, and it is: unchanged across four focus
# changes in a five-window workspace. Chips therefore stay put when focus moves,
# which is the point. The cost is that a window moved within the layout does not
# move its chip.
args=()
slot=0
while IFS='|' read -r id bid app title; do
    if [ -z "$id" ] || [ "$slot" -ge "$SLOTS" ]; then
        continue
    fi
    slot=$((slot + 1))
    chip_for "$bid" "$app" "$title"

    if [ "$id" = "$focused" ]; then
        # Filled, by the same inversion the focused workspace uses.
        args+=(--set "win.$slot"
               icon.color="$ACTIVE_FG"
               label.color="$ACTIVE_FG"
               background.color="$ACTIVE_BG"
               background.border_color="$ACTIVE_BG")
    else
        args+=(--set "win.$slot"
               icon.color="$DIM"
               label.color="$DIM"
               background.color="$CHIP_EMPTY"
               background.border_color="$CHIP_BORDER")
    fi

    # One command: focus --window-id switches workspace on its own.
    args+=(--set "win.$slot"
           drawing=on
           icon="$glyph"
           label="$label"
           click_script="aerospace focus --window-id $id")
done <<< "$windows"

# Unconditional: a slot past the window count still holds the previous
# repaint's chip. This is also the whole empty-workspace branch -- slot is 0
# there, so all five are switched off.
while [ "$slot" -lt "$SLOTS" ]; do
    slot=$((slot + 1))
    args+=(--set "win.$slot" drawing=off)
done

sketchybar "${args[@]}"
