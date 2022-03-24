#!/bin/sh -Cue

. ../../lib/dot.sh

OP_ITEM_NAME='dotfile-env'

eval "$(op signin my)"

op get item dotfiles-env --fields notesPlain | tee "$DOT_ENV_FILE"

echo ">>> '.env' file updated"
