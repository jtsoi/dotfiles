#!/bin/sh -Cue


. ../../lib/dot.sh

curl -sfL https://direnv.net/install.sh | sudo bash

dot_symlink "$ZSHRC_D_DIR/15-direnv-hook.zsh" "$DOT_MODULE_FILES_DIR/15-direnv-hook.zsh"

echo ">>> Direnv installed"