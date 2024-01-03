#!/usr/bin/node

// Import necessary modules
const fs = require('fs');
const request = require('request');

// Get command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if both URL and file path are provided
if (!url || !filePath) {
  console.error('Usage: node 5-request_store.js <URL> <file-path>');
  process.exit(1);
}

// Make a request to the specified URL
request(url, (error, response, body) => {
  // Check for errors during the request
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Check if the request was successful (status code 200)
  if (response.statusCode === 200) {
    // Write the body content to the specified file with UTF-8 encoding
    fs.writeFileSync(filePath, body, 'utf-8');
    console.log(`Contents from ${url} saved to ${filePath}`);
  } else {
    console.error(`Error: Unable to fetch content from ${url}. Status Code: ${response.statusCode}`);
    process.exit(1);
  }
});

