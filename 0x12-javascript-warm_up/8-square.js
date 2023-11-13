#!/usr/bin/node

const sizeArg = process.argv[2];

const size = parseInt(sizeArg);

if (!isNaN(size) && isFinite(size) && size > 0) {
    for (let i = 0; i < size; i++) {
        let row = '';
        for (let j = 0; j < size; j++) {
            row += 'X';
        }
        console.log(row);
    }
} else {
    console.log('Missing size');
}
