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

function listOrderedCharacters (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const charDict = {};
      const charList = JSON.parse(body).characters;
      for (let i = 0; i < charList.length; i++) {
        request(charList[i], function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            charDict[i] = JSON.parse(body).name;
          }
          if (charList.length === Object.keys(charDict).length) {
            for (let k = 0; k < Object.keys(charDict).length; k++) {
              console.log(charDict[k]);
            }
          }
        });
      }
    }
  });
}
listOrderedCharacters(url);
