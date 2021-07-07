#!/usr/bin/node
const fs = require('fs');
const File = process.argv[2];
const stream = fs.createReadStream(File, 'utf-8');
stream.on('error', error => {
  console.log(error);
})
  .on('data', data => {
    console.log(data);
  });
