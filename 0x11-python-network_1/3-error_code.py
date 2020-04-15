#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8), and manages urllib.error.HTTPError
exceptions.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    if url is not None:
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req) as response:
                the_page = response.read()
                print(the_page.decode('utf-8'))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
