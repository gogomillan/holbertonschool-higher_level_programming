#!/usr/bin/node
/*
  script that computes the number of tasks completed by user id.
  - The first argument is the API URL:
    https://jsonplaceholder.typicode.com/todos
  - It is used the module request
 */
const request = require('request');
const url = process.argv[2];
const users = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const user of JSON.parse(body)) {
      if (!users[parseInt(user.userId, 10) - 1]) {
        users[parseInt(user.userId, 10) - 1] = 0;
      }
      users[parseInt(user.userId, 10) - 1] += 1;
    }
    console.log(users);
  }
});
