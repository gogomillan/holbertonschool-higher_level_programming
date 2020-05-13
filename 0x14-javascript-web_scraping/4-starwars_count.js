#!/usr/bin/node
/*
  script that prints the number of movies where the character Wedge Antilles is
  present.
  - The first argument is the API URL of the Star wars API:
    https://swapi-api.hbtn.io/api/films/
  - Wedge Antilles is character ID 18
  - It is used the module request

 */
const request = require('request');
const url = process.argv[2];
let tot = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  for (const film of JSON.parse(body).results) {
    tot += film.characters.filter(each => each.search('/18/') > 0).length;
  }
  console.log(tot);
});
