#!/bin/sh -Cue


. ../../lib/dot.sh

PREZTO_DIR="$HOME/.zprezto"

sudo apt-get install -y \
  zsh \
  fasd \
  fonts-powerline


if [ -d "$PREZTO_DIR" ]; then
    cd $PREZTO_DIR
    git pull
    git submodule sync --recursive
    git submodule update --init --recursive
else
    git clone --recursive https://github.com/sorin-ionescu/prezto.git "$PREZTO_DIR"
fi
