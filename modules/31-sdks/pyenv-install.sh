#!/bin/sh -Cue


. ../../lib/dot.sh

curl https://pyenv.run | bash

dot_symlink "$ZSHRC_D_DIR/31-pyenv-hook.zsh" "$DOT_MODULE_FILES_DIR/31-pyenv-hook.zsh"

echo ">>> PyEnv installed"