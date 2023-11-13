#!/usr/bin/node

const myArgument = process.argv[2];

if (myArgument === undefined) {
  console.log('No argument');
} else {
  console.log(myArgument);
}
