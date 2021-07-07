#!/usr/bin/node
const { list } = require('./100-data');
const list2 = list.map((idx, num) => idx * num);
console.log(list);
console.log(list2);
