#!/usr/bin/node
/*
  script that gets the contents of a webpage and stores it in a file.
  - The first argument is the URL to request
  - The second argument the file path to store the body response
  - The file is in UTF-8 encoded
  - It is used the module request
 */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url).pipe(fs.createWriteStream(file));
