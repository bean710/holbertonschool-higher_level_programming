#!/usr/bin/python3
"""This file requests form reddit's api"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subs for a subreddit"""

    res = requests.post("http://reddit.com/r/{}/about.json".format(subreddit),
                        headers={"User-Agent": "python:com.benkeener:0.0.1"})

    dat = res.json()

    subs = dat["data"]["subscribers"]

    return (subs)
