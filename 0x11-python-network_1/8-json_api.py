#!/usr/bin/python3
"""This script makes a POST request to an API"""
import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    res = requests.post("http://0.0.0.0:5000/search_user", data={"q":letter})

    try:
        jres = res.json()
        if jres != {}:
            print("[{}] {}".format(jres.get("id"), jres.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
