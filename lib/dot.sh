#!/bin/sh -Cue

echo ">>> Dot lib included"

# Get the directory of the runnings script
PWD_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# Split the path on 'dotfiles', assuming the project name is dotfiles.
# C/P from https://stackoverflow.com/questions/41996121/split-string-after-matching-the-word-in-shell
DOT_DIR="$(echo "$PWD_DIR" | sed -n -e 's/\(^.*\)\(\(dotfiles\).*\)/\1/p')/dotfiles"

# Module specific
DOT_MODULE_DIR="$PWD_DIR"
DOT_MODULE_FILES_DIR="$DOT_MODULE_DIR/files"

# Dotfiles shared dirs
DOT_LIB_DIR="$DOT_DIR/lib"
DOT_MODULES_DIR="$DOT_DIR/modules"
DOT_ENV_FILE="$DOT_DIR/.env"

# Common folders
ZSHRC_D_DIR="$HOME/.zshrc.d"

# Load .env file if it exists
if [ -f "$DOT_ENV_FILE" ]; then
    eval "$(cat $DOT_ENV_FILE)"
    echo ">>> '.env' file loaded"
fi

# Load sub libraries
. "$DOT_LIB_DIR/files.sh"
