#!/usr/bin/node
/*
  script that writes a string to a file.
  - The first argument is the file path
  - The second argument is the string to write
  - The content of the file is written in utf-8
  - If an error occurred during while writing, prints the error object
 */
const fs = require('fs');

fs.appendFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    console.log(err);
  }
});
