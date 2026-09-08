#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
#
# Roles, not per-item colours: a re-theme touches only this file. Dark is the
# fixed requirement; the hues carry item state.
export BAR_BG=0xff000000        # pure black, so every label sits at full contrast
export FG=0xffeaeaea            # primary label
export DIM=0xff9a9a9a           # secondary labels and inactive workspaces
export SEP=0xffffffff           # drawn rules between widgets
export CHIP_EMPTY=0x00000000    # inactive workspace: outline only, no fill
export CHIP_BORDER=0xff6e6e6e   # that outline
export ACTIVE_BG=0xffffffff     # focused workspace: filled white
export ACTIVE_FG=0xff000000     # its label, dark against that fill
export OK=0xff9ece6a            # netbird connected, battery charging
export WARN=0xffe0af68          # battery under 20%, load above core count
export CRIT=0xfff7768e          # netbird down, battery under 10%
