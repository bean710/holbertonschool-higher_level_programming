#!/usr/bin/python3
"""This module gets the body of the holberton page"""
import urllib.request as req


if __name__ == "__main__":
    with req.urlopen("https://intranet.hbtn.io/status") as res:
        body = res.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t\
- utf8 content: {}".format(type(body), body, body.decode("utf-8")))
