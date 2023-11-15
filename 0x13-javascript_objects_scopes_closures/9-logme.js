#!/usr/bin/node

let loged = 0;
exports.logMe = function (item) {
  console.log(`${loged}: ${item}`);
  loged++;
};
