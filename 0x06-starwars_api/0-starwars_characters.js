#!/usr/bin/node

const request = require('request');

function getMovieCharacters (movieId) {
  const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
  const movieUrl = `${baseUrl}${movieId}/`;

  request.get(movieUrl, (error, response, movieData) => {
    if (error || response.statusCode !== 200) {
      return;
    }

    const charactersUrlList = JSON.parse(movieData).characters;

    charactersUrlList.forEach(characterUrl => {
      request.get(characterUrl, (error, response, characterData) => {
        if (error || response.statusCode !== 200) {
          return;
        }

        console.log(JSON.parse(characterData).name);
      });
    });
  });
}

const args = process.argv.slice(2);

const movieId = args[0];
getMovieCharacters(movieId);
