#!/bin/bash
# Displays the answer from a POST json
curl -s -d "@${2}" -H "Content-Type: application/json" -X POST "$1"
