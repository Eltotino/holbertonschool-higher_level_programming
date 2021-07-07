#!/usr/bin/node
const fs = require('fs');
const File = process.argv[2];
const Str = process.argv[3];
const content = fs.createWriteStream(File, 'utf-8');
content.write(Str);
content.on('error', error => {
  console.log(error);
});
