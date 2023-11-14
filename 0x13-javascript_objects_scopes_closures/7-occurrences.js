#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ocr = 0;
  for (const i of list) {
    if (i === searchElement) ocr++;
  }
  return ocr;
};
