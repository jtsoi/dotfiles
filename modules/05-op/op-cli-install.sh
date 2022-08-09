#!/bin/sh -Cue

. ../../lib/dot.sh

OP_CLI_VERSION='2.6.0'
OP_CLI_PATH="/usr/local/bin/op"

dot_curl_download \
  "https://cache.agilebits.com/dist/1P/op2/pkg/v$OP_CLI_VERSION/op_linux_amd64_v$OP_CLI_VERSION.zip" \
  "/tmp/op_cli.zip"

unzip -o "/tmp/op_cli.zip" -d "/tmp/"

sudo mv -f /tmp/op "$OP_CLI_PATH"

sudo chmod +x "$OP_CLI_PATH"

op update

echo ">>> To login run:"
echo ">>>   op signin -h"
