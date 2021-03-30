#!/usr/bin/node
const times = Number(process.argv[2]);
if (times) {
  for (let index = 0; index < times; index++) {
    const square = ('X'.repeat(times));
    console.log(square);
  }
} else {
  console.log('Missing size');
}
