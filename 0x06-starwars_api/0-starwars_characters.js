#!/usr/bin/node

const request = require('request');

function getMovieCharacters (movieId) {
  const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
  const movieUrl = `${baseUrl}${movieId}/`;

  return new Promise((resolve, reject) => {
    request.get(movieUrl, (error, response, movieData) => {
      if (error) {
        reject(error);
        return;
      }

      const charactersUrlList = JSON.parse(movieData).characters;
      const characterNames = [];

      function fetchCharacter (index) {
        if (index >= charactersUrlList.length) {
          resolve(characterNames);
          return;
        }

        const characterUrl = charactersUrlList[index];
        request.get(characterUrl, (error, response, characterData) => {
          if (error) {
            reject(error);
            return;
          }

          characterNames.push(JSON.parse(characterData).name);
          fetchCharacter(index + 1);
        });
      }
      fetchCharacter(0);
    });
  });
}

const args = process.argv.slice(2);

const movieId = args[0];

getMovieCharacters(movieId)
  .then(characterNames => {
    characterNames.forEach((characterName, index) => {
      console.log(`${characterName}`);
    });
  })
  .catch(error => console.error(error));
