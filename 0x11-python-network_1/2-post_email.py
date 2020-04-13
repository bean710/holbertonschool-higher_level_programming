#!/usr/bin/python3
"""This module sends POST with an email"""
import urllib.parse as parse
import urllib.request as request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode("ascii")
    req = request.Request(url, data)
    with request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
