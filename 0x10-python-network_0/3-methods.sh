#!/usr/bin/env bash
# This script gets the accepted methods from an HTTP server

curl -si -X OPTIONS "$1" | grep 'Allow:' | cut -f 1 -d " " --complement
