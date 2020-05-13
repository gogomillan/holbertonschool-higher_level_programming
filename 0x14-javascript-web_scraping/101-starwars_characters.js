#!/usr/bin/node
/*
  script that prints all characters of a Star Wars movie:
  - The first argument is the movie ID
  - It is used the Star wars API with the endpoint
    https://swapi-api.hbtn.io/api/films/:id
  - It is used the module request
 */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  }
  for (const each of JSON.parse(body).characters) {
    await request(each, function (err, resp, bd) {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(bd).name);
    });
  }
});
