#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const result = {};
    for (const all of todos) {
      if (all.completed) {
        if (!result[all.userId]) {
          result[all.userId] = 1;
        } else {
          result[all.userId]++;
        }
      }
    }
    console.log(result);
  }
});
