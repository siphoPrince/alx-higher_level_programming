#!/usr/bin/node

const myArguments = process.argv.length - 2;

if (myArguments === 0) {
  console.log('No argument');
} else if (myArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
