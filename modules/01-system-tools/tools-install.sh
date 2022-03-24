#!/bin/sh -Cue

. ../../lib/dot.sh

sudo apt-get update

sudo apt-get install -y \
  micro \
  apt-transport-https \
  ca-certificates \
  curl \
  build-essential \
  libreadline-dev \
  libssl-dev \
  libbz2-dev \
  libsqlite3-dev \
  jq \
  htop \
  moreutils
  
