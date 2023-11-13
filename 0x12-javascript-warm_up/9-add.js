#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (!isNaN(arg1) && isFinite(arg1) && !isNaN(arg2) && isFinite(arg2)) {
  console.log(add(arg1, arg2));
} else {
  console.log('Invalid input. Please provide two integers.');
}
