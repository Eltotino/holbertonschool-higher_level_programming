#!/usr/bin/node
const arr = process.argv.slice(2);

const max = arr.sort((a, b) => b - a)[1];
console.log(max);

if (arr.length <= 2) {
  console.log(0);
}
