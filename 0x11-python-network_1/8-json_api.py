#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    payload = {"q": q}

    r = requests.post(url, data=payload)
    if r.text == "{}\n":
        print("No result")
    else:
        r_dict = dict([e.split(":") for e in
                       r.text.strip("{}\n").replace('"', '').split(",")])
        print("[{id}] {name}".format(**r_dict))
