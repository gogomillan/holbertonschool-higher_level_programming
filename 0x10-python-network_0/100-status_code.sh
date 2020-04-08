#!/bin/bash
# Displays only the status code
curl -s -L -w "%{http_code}" -I "$1" -o /dev/null
