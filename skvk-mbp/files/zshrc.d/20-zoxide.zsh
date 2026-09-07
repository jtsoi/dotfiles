# `z` — frecency-ranked directory jumping. Guarded so a missing brew package
# degrades to a plain shell instead of erroring on every prompt.
if command -v zoxide >/dev/null; then
  eval "$(zoxide init zsh)"
fi
