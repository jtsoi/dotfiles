#!/bin/sh -Cue


. ../../lib/dot.sh

GIT_GLOBAL_IGNORE_FILE="$HOME/.gitignore"

set_git()
{
  git config --global "$1" "$2"
}

set_git "user.name" "$GIT_USER_NAME"
set_git "user.email" "$GIT_USER_EMAIL"


set_git "core.editor" "micro"
set_git "core.excludesFile" "$GIT_GLOBAL_IGNORE_FILE"

set_git "alias.co" "checkout"
set_git "alias.st" "status -sb"
set_git "alias.lg" "log --graph --pretty=format:'%C(yellow)%h%C(auto)%d%Creset %s %C(white)- %an, %ar%Creset'"


set_git "color.branch" "auto"
set_git "color.diff" "auto"
set_git "color.interactive" "auto"
set_git "color.status" "auto"
set_git "color.pager" "true"
set_git "color.ui" "true"

# Symlink gitignore
dot_symlink "$GIT_GLOBAL_IGNORE_FILE" "$DOT_MODULE_FILES_DIR/dot_gitignore" 

echo ">>> Git config:"
cat "$HOME/.gitconfig"
