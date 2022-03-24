#!/bin/sh -Cue

# Download a file using curl.
dot_curl_download()
{
  echo ">>> Downloading file to $2"
  curl \
    --location "$1" \
    --output "$2"
}


# Symlink FROM TO
dot_symlink()
{
  ln -sf "$2" "$1"
  echo ">>> Created symlink $1 --> $2"
}