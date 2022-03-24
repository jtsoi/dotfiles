#!/bin/sh -Cue

# This module will setup ~/Code/* folders/workspaces
# Each workspace will have a custom git email configured

. ../../lib/dot.sh

GIT_CONFIG_FILE="$HOME/.gitconfig"

ensure_workspace()
{

  WORKSPACE_NAME="$1"
  
  WORKSPACE_DIR="$HOME/Code/$WORKSPACE_NAME"
  eval "WORKSPACE_GIT_USER_EMAIL=\$GIT_WORKSPACE_${WORKSPACE_NAME}_USER_EMAIL"

  mkdir -p $WORKSPACE_DIR

  if ! grep -q $WORKSPACE_DIR $GIT_CONFIG_FILE; then
    cat <<EOT | tee "$WORKSPACE_DIR/.gitconfig"
[user]
     email = $WORKSPACE_GIT_USER_EMAIL
EOT

    cat <<EOT >> $GIT_CONFIG_FILE
[includeIf "gitdir:$WORKSPACE_DIR/**"]
    path = $WORKSPACE_DIR/.gitconfig
EOT
  fi
}

for WS in $GIT_WORKSPACES; do
  echo "Ensuring workspace $WS"
  ensure_workspace $WS
done

echo ">>> Git config:"
cat "$HOME/.gitconfig"
