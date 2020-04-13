#!/usr/bin/python3
"""This script lists commit info for a given repo"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]

    res = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        user, repo))

    jres = res.json()
    for commit in jres[:10]:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
