#!/usr/bin/node

const x = process.argv[2];

const stringConvert = parseInt(x);

if (!isNaN(stringConvert) && isFinite(stringConvert)) {
  for (let i = 0; i < stringConvert; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
