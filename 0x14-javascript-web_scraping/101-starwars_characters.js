#!/usr/bin/node
/*
  script that prints all characters of a Star Wars movie:
  - The first argument is the movie ID
  - It is used the Star wars API with the endpoint
    https://swapi-api.hbtn.io/api/films/:id
  - Display one character name by line in the same order of the list characters
    in the /films/ response
  - It is used the module request
 */
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getCharacter (theUrl) {
  return new Promise((resolve, reject) => {
    request(theUrl, function (error, resp, body) {
      if (error) {
        reject(error);
      }
      resolve(body);
    });
  });
}

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  }
  for (const each of JSON.parse(body).characters) {
    try {
      const character = await getCharacter(each);
      console.log(JSON.parse(character).name);
    } catch (error) {
      console.error(error);
    }
  }
});
