#!/usr/bin/python3
"""This module uses GitHub's auth api"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]

    res = requests.get("https://api.github.com/users/{}".format(user),
                       auth=HTTPBasicAuth(user, token))

    print(res.json().get("id"))
