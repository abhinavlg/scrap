#!/bin/bash

# Update package list
sudo apt-get update

# Install missing libraries
sudo apt-get install -y \
  libgstgl-1.0-0 \
  libgstcodecparsers-1.0-0 \
  libavif15 \
  libenchant2-2 \
  libsecret-1-0 \
  libmanette-0.2-0 \
  libgles2-mesa
