#!/usr/bin/node

const list = require('./data.js').list;
console.log(list);
const newList = list.map((cur, idx) => cur * idx);
console.log(newList);
