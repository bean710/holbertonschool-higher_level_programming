#!/bin/bash
# This script prints out only the status code
curl -s -o /dev/null -s -w "%{http_code}\n" "$1"
