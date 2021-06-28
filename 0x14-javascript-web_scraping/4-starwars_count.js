#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (!error) {
    const result = JSON.parse(body).result;
    let count = 0;
    for (const movie of result) {
      if (movie.characters.find(value => value.endsWith('18/'))) {
        count++;
      }
    }
    console.log(count);
  }
});
