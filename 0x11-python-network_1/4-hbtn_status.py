#!/usr/bin/python3
"""This module gets the body of the holberton page"""
import requests


if __name__ == "__main__":
    res = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(res.text), res.text))
