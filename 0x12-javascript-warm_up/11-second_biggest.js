#!/usr/bin/node

if (process.argv.length < 3) {
  console.log(0);
} else {
  const nump = process.argv.slice(2);
  const num = nump.map(Number);

  let max = num[0];
  for (let i = 0; i < num.length; i++) {
    max = (max > num[i]) ? max : num[i];
  }
  let smax = 0;
  for (let j = 0; j < num.length; j++) {
    smax = (num[j] > smax && num[j] < max) ? num[j] : smax;
  }
  console.log(smax);
}
