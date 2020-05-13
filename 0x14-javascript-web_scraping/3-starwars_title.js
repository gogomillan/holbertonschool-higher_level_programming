#!/usr/bin/node
/*
  script that prints the title of a Star Wars movie where the episode number
  matches a given integer.
  - The first argument is the movie ID
  - It is used the Star wars API with the endpoint
    https://swapi-api.hbtn.io/api/films/:id
  - It is used the module request
 */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
