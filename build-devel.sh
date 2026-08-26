#!/bin/bash
# Process building blocks using the development (rolling) image build
BBP_IMAGE_TAG=develop exec "$(dirname "$0")/build.sh" "$@"