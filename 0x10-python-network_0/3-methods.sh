#!/bin/bash
# Displays supported methos from an HTTP server
curl -s -X OPTIONS -i "$1" | grep -o -P "(?<=Allow: ).*(?=[\r|\n|$])"
