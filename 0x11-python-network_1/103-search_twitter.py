#!/usr/bin/python3
"""
Python script that takes in 3 strings and sends a search request to the Twitter
API.
"""
import requests
import base64
import sys


if __name__ == "__main__":
    """ Peparing parameters to get the bearer token
    """
    key = sys.argv[1]
    secret = sys.argv[2]
    url = "https://api.twitter.com/oauth2/token"
    payload = {'grant_type': 'client_credentials'}
    token = requests.post(url, auth=(key, secret), data=payload)

    """ Using the token preparing parameters to get the tweets
    """
    auth = {'Authorization': 'Bearer ' + token.json().get('access_token')}
    payload = {'q': sys.argv[3], 'result_type': 'recent', 'count': '6'}
    url = "https://api.twitter.com/1.1/search/tweets.json"
    token = requests.get(url, params=payload, headers=auth)

    """ Printing the tweets
    """
    for val in token.json().get("statuses"):
        print("[{id_str}] {text}".format(**val))
