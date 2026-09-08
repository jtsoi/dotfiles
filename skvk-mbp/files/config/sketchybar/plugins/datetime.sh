#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
#
# One script for all three time items rather than inline `date` calls in
# sketchybarrc: inline would put sketchybar's own % escaping inside a shell
# string that shellcheck also has to accept, and the quoting that satisfies both
# is fragile.
set -euo pipefail

case "${1:-}" in
    local)   label=$(date '+%H:%M') ;;
    utc)     label=$(TZ=UTC date '+%H:%MZ') ;;
    # %a has no lowercase form in BSD date, hence tr. Character classes
    # rather than ranges: shellcheck rejects A-Z at info level (SC2019).
    isoweek) label=$(date '+w%V/%a' | tr '[:upper:]' '[:lower:]') ;;
    *)       printf 'usage: %s local|utc|isoweek\n' "${0##*/}" >&2; exit 64 ;;
esac

sketchybar --set "$NAME" label="$label"
