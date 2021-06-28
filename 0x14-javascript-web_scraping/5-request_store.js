#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const apiUrl = process.argv[2];
const Path = process.argv[3];
request
  .get(apiUrl)
  .on('error', error => console.log(error))
  .pipe(fs.createWriteStream(Path));
