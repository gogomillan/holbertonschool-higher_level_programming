#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        print("Body response:")
        print("    - type: {}".format(type(response.msg)))
        print("    - content: {}".format(response.msg))
