#!/usr/bin/node
/*
  script that display the status code of a GET request.
  - The first argument is the URL to request (GET)
  - The status code is printed like this: code: <status code>
  - It is used the module request

 */
const request = require('request');

request(process.argv[2], function (error, response, body) {
  console.log('code:', response && response.statusCode);
});
