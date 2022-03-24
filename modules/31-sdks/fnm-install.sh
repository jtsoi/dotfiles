#!/bin/sh -Cue


. ../../lib/dot.sh

export SKIP_SHELL=true
curl -fsSL https://fnm.vercel.app/install | bash


echo ">>> FNM installed"