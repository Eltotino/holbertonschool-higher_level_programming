#!/usr/bin/node
const times = Number(process.argv[2]);
if (times) {
  for (let index = 0; index < times; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
