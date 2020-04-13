#!/usr/bin/python3
"""This module gets the body of the holberton page"""
import urllib.request as req
import sys


if __name__ == "__main__":
    with req.urlopen(sys.argv[1]) as res:
        info = res.info()
        print(info.get("X-Request-Id"))
