#!/bin/sh -Cue

. ../../lib/dot.sh

KEY_FILE="$HOME/.ssh/id_ed25519"


ssh-keygen -t ed25519 -C "jtsoi" -f "$KEY_FILE"

echo ">>> Run 'eval \"$(ssh-agent -s)\"' to add key to ssh-agent"