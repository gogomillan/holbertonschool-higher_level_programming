#!/usr/bin/node
/*
   script that reads and prints the content of a file.
   - The first argument is the file path
   - The content of the file is readed in utf-8
   - If an error occurred during the reading, it is printed the error object
 */
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
}); 
