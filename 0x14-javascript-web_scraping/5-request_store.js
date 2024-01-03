#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

axios.get(url)
  .then(response => {
    const content = response.data;
    fs.writeFile(filePath, content, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      } else {
        console.log(`Webpage content saved to: ${filePath}`);
      }
    });
  })
  .catch(error => {
    console.error(error.message);
  });
