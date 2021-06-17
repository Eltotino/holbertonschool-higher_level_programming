#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (const obj of list) {
    if (obj === searchElement) {
      occur++;
    }
  }
  return occur;
};
