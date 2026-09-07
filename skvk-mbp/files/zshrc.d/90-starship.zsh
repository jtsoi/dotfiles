# 90- so the prompt initialises after the plugins but before syntax
# highlighting, which must stay last.
if command -v starship >/dev/null; then
  eval "$(starship init zsh)"
fi
