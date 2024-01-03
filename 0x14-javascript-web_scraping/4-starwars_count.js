#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const wedgeAntillesId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const filmsData = JSON.parse(body).results;

      // Filter films where Wedge Antilles is present
      const filmsWithWedgeAntilles = filmsData.filter((film) =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)
      );

      console.log(`${filmsWithWedgeAntilles.length}`);
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError}`);
    }
  }
});
