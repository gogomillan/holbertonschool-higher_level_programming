#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password) and
uses the Github API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]

    url = "https://api.github.com/repos/" + user + "/" + repo + \
          "/commits?page=1&per_page=10"
    repos = requests.get(url)

    for element in repos.json():
        print("{}: {}".format(element.get("sha"),
                              element.get("commit").get("author").get("name")))
