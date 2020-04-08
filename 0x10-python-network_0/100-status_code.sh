#!/bin/bash
# This script prints out only the status code
curl -s -L -o /dev/null -s -w "%{http_code}" "$1"
