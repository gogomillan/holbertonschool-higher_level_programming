#!/usr/bin/node
/*
  script that display the status code of a GET request.
  - The first argument is the URL to request (GET)
  - The status code is printed like this: code: <status code>
  - It is used the module request

 */
const request = require('request');

request.get(process.argv[2]).on('response', function (response) {
  console.log('code:', response.statusCode);
});
