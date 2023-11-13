#!/usr/bin/node

const MyNumber = process.argv[2];

const numValue = parseInt(MyNumber);

if (!isNaN(MyNumber)) {
  console.log('My number: ' + numValue);
} else {
  console.log('Not a number');
}
