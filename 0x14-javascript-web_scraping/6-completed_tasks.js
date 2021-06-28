#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (!error) {
    const all = JSON.parse(body);
    const result = {};
    for (const alls of all) {
      if (alls.completed) {
        if (!result[alls.UserId]) {
          result[alls.userId] = 1;
        } else {
          result[alls.userId]++;
        }
      }
    }
    console.log(result);
  }
});
