#!/bin/bash
# Displays the contento for parameter X-HolbertonSchool-User-Id
curl -s -X GET -H "X-HolbertonSchool-User-Id:98" "$1"
