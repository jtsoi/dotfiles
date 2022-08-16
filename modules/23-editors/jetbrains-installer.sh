#!/bin/sh -Cue


. ../../lib/dot.sh

curl -fsSL https://raw.githubusercontent.com/nagygergo/jetbrains-toolbox-install/master/jetbrains-toolbox.sh | sudo bash

jetbrains-toolbox
