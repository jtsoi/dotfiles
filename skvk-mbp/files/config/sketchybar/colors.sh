#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
#
# The Skovik palette, from arbor/packages/client/app/styles/shared/colors.css,
# on a ground desaturated well below --color-brand-primary. Everything else is
# that file's brand hue, 135, at lightnesses this ground can carry: its own
# dark-mode values assume a near-black canvas at 14% and would be mud here.
#
# The muted ground is what lets OK be the brand green again. Against
# --color-brand-primary itself the success signature is invisible, since they are
# the same colour. OK, WARN and CRIT have no consumer while the right group is
# empty; they are kept because the plugins that use them are kept.
#
# Roles, not per-item colours: a re-theme touches only this file.
export BAR_BG=0xff46554a       # RGB 70 85 74, a desaturated brand hue
export FG=0xfff1f4f1           # hsl(135 12% 95%) labels
export DIM=0xffb8c7bb          # hsl(135 12% 75%) secondary labels
export CHIP_EMPTY=0x00000000   # inactive workspace: outline only, no fill
export CHIP_BORDER=0xff76937d  # hsl(135 12% 52%) that outline
export ACTIVE_BG=0xfff9fafa    # hsl(135 10% 98%) focused workspace: filled
export ACTIVE_FG=0xff304034    # hsl(135 14% 22%) its label, the ground darkened to read on that fill
export OK=0xff72ca88           # hsl(135 45% 62%) --color-success-signature, lifted: the ground is muted enough that the brand green reads again
export WARN=0xfff0ac4c         # hsl(35 85% 62%) --color-warning-signature, lifted
export CRIT=0xffed5a5a         # hsl(0 80% 64%) --color-danger-signature, lifted
