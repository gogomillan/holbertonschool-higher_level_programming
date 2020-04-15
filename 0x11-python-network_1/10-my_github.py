#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password) and
uses the Github API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]

    r = requests.get('https://api.github.com/user', auth=(user, token))

    if r.status_code >= 400:
        print("None")
    else:
        """ It is used ||| as token because of dates has : inside
        """
        r_dict = dict([e.split("|||") for e in r.text.strip("{}\n").
                       replace('":"', '"|||"').replace('":', '"|||').
                       replace('"','').split(",")])
        print("{id}".format(**r_dict))
