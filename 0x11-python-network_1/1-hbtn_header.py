#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    if url is not None:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_header = response.info()
            print(the_header['X-Request-Id'])
