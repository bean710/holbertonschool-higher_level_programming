#!/bin/bash
# This script sends a POST request with form data
curl -s "$1" --data "email=hr@holbertonschool.com&subject=I will always be here for PLD"
