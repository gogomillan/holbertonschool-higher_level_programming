#!/bin/bash
# Displays the message after catch
curl -s -H "Origin: HolbertonSchool" -d "user_id=98" -L -X PUT 0.0.0.0:5000/catch_me
