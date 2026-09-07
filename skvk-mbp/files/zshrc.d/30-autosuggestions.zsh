# $HOMEBREW_PREFIX rather than `brew --prefix`: avoids a subprocess on every
# shell start. The guard's login-shell sourcing has already exported it.
_plugin="${HOMEBREW_PREFIX-}/share/zsh-autosuggestions/zsh-autosuggestions.zsh"
if [[ -r $_plugin ]]; then
  source "$_plugin"
  ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=60'
fi
unset _plugin
