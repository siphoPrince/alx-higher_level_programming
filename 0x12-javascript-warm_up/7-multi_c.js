#!/usr/bin/node

const x = process.argv[2];

const stringConvet = parseInt(x);

if (!isNaN(stringConvet)) {
  for (let i = 0; i < stringConvet; i++) {
    console.log('c is fun');
  }
}
