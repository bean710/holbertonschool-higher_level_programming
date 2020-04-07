#!/bin/bash
# This script gets a response from a super secret page
curl -Ls -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0:5000/catch_me
