#!/usr/bin/node
const request = require('request');
const Url = process.argv[2];
request.get(Url)
  .on('response', response => {
    console.log('code: $(response.statusCode}');
  });
