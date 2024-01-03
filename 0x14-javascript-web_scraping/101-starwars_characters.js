#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;

      // Function to retrieve character names and print them
      const getCharacterName = (characterUrl) => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      };

      // Display characters one by line in the same order as the list in /films/ response
      charactersUrls.forEach(getCharacterName);
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError}`);
    }
  }
});
