#!/usr/bin/env bash
# Managed by skvk-mbp/mise.toml ([dotfiles]).
#
# Interface type plus NetBird state. The Wi-Fi SSID is deliberately absent:
# reading it needs Location Services, which a bar script will not be granted --
# `networksetup -getairportnetwork en0` reports "not associated" here even with
# Wi-Fi on and the default route over en0.
#
# Never log this script's netbird output: it carries internal peer hostnames and
# WireGuard public keys.
set -euo pipefail

# shellcheck source=SCRIPTDIR/../colors.sh
source "$HOME/.config/sketchybar/colors.sh"

# NetBird.app owns this path and it is absent from the launchd agent's PATH,
# so `command -v netbird` fails inside every bar-plugin invocation even with
# NetBird installed and connected. An -x guard on the absolute path still
# hides the VPN half if NetBird is ever removed, which is the behaviour the
# design wants.
NETBIRD=/usr/local/bin/netbird

iface=$(route -n get default 2>/dev/null | awk '/interface:/ {print $2}')
case "$iface" in
    en0) net="wifi" ;;
    "")  net="offline" ;;
    *)   net="$iface" ;;
esac

label="$net"
color="$FG"

if [ -x "$NETBIRD" ]; then
    read -r daemon connected total <<<"$(
        "$NETBIRD" status --json 2>/dev/null \
            | /usr/bin/jq -r '"\(.daemonStatus) \(.peers.connected) \(.peers.total)"' 2>/dev/null \
            || printf 'Unknown 0 0'
    )"

    if [ "$daemon" = "Connected" ] && [ "$total" -gt 0 ] && [ "$connected" = "$total" ]; then
        label="$net · nb $connected/$total"
        color="$OK"
    elif [ "$daemon" = "Connected" ]; then
        label="$net · nb $connected/$total"
        color="$CRIT"
    else
        label="$net · nb down"
        color="$CRIT"
    fi
fi

sketchybar --set "$NAME" label="$label" label.color="$color"
