# Must be sourced after every other plugin that defines widgets, hence 99-.
_plugin="${HOMEBREW_PREFIX-}/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"
if [[ -r $_plugin ]]; then
  source "$_plugin"
fi
unset _plugin
