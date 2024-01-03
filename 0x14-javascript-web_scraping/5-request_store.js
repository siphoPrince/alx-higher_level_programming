#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get({ url, encoding: 'utf-8' }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      } else {
        console.log(`Webpage content saved to: ${filePath}`);
        // Read and print the contents of the saved file
        fs.readFile(filePath, 'utf-8', (readError, fileContent) => {
          if (readError) {
            console.error(readError);
          } else {
            console.log(fileContent);
          }
        });
      }
    });
  }
});
