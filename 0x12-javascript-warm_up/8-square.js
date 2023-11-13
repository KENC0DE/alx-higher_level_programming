#!/usr/bin/node

const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let s = 0; s < num; s++) {
    let line = '';
    for (let r = 0; r < num; r++) line += 'X';
    console.log(line);
  }
}
