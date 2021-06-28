#!/usr/bin/node
const request = require('request');
const Episode = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api';
request(apiUrl + `/films/${Episode}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
