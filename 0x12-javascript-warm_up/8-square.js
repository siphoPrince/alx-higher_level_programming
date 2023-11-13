#!/usr/bin/node

const myArgs = process.argv[2];

const argConvert = parseInt(myArgs);

if (!isNaN(argConvert) && isFinite(argConvert) && argConvert > 0) {
  for (let i = 0; i < argConvert; i++) {
    let row = '';
    for (let j = 0; j < argConvert; j++) {
      row += 'X ';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
