#!/bin/bash
# Displays the size of the body of the response from a HTTP header
curl -s -X GET -i "$1" | grep -o -P "(?<=Content\-Length: )(\d+)"
