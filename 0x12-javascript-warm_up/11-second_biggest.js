#!/usr/bin/node
const arr = process.argv.slice(2);

if (arr.length <= 2) {
  console.log(0);
} else {
  const max = arr.sort((a, b) => b - a)[1];
  console.log(max);
}
