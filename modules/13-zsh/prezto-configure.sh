#!/bin/sh -Cue


. ../../lib/dot.sh

PREZTO_DIR="$HOME/.zprezto"

PREZTO_RUNCOMS="zlogin zlogout zprofile zshenv"

for CONF_FILE in $PREZTO_RUNCOMS; do
    echo "$CONF_FILE"
    dot_symlink "$HOME/.$CONF_FILE" "$PREZTO_DIR/runcoms/$CONF_FILE"
done

dot_symlink "$HOME/.zpreztorc" "$DOT_MODULE_FILES_DIR/dot_zpreztorc"
dot_symlink "$HOME/.zshrc" "$DOT_MODULE_FILES_DIR/dot_zshrc"

# Create zshrc.d directory
mkdir -p $ZSHRC_D_DIR

dot_symlink "$ZSHRC_D_DIR/13-zsh-aliases.zsh" "$DOT_MODULE_FILES_DIR/13-zsh-aliases.zsh"

# Make zsh deafult shell
chsh -s /bin/zsh

echo ">>> ZSH is now the default shell"
