#!/bin/sh -Cue

# Make sure you are logged in to "my.1password.eu" before running this script.

. ../../lib/dot.sh

OP_ITEM_NAME='dotfiles-env'

eval "$(op signin --account my)"

op item get $OP_ITEM_NAME --fields notesPlain --format json | jq '.value' -r | tee "$DOT_ENV_FILE"

echo ">>> '.env' file updated"
