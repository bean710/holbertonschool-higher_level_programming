#!/usr/bin/env bash
# This script gets the number of bytes from an HTTP response
curl -s -I $1 | grep "Content-Length: " | awk '{print $2}'
