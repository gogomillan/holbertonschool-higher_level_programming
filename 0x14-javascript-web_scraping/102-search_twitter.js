#!/usr/bin/node
/*
  Javascript script that takes in 3 strings and sends a search request to the
  Twitter API
 */
const request = require('request');
const user = process.argv[2];
const pass = process.argv[3];
const sear = process.argv[4];

/*
request.post({url:'https://api.twitter.com/oauth2/token',
auth: 'iYG0zVmVWMjsX3YnQCjA6aJsY:EySmIgS9gujl4ZI6zDoTa0RVZ8vdWAsSrxTcEETBcJR926e0F9',
form: {grant_type:'client_credentials'}},
function (err, response, body) {
  console.log(response.statusCode);
  console.log(body);
});
*/
request.post({url:'https://api.twitter.com/oauth2/token',
headers: {'iYG0zVmVWMjsX3YnQCjA6aJsY':'EySmIgS9gujl4ZI6zDoTa0RVZ8vdWAsSrxTcEETBcJR926e0F9'},
form: {grant_type:'client_credentials'}},
function (err, response, body) {
  console.log(response.statusCode);
  console.log(body);
});
