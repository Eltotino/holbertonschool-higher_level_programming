#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const Film = process.argv[2];
request(apiUrl + Film, (error, response, body) => {
  if (!error) {
    const persos = JSON.parse(body).characters;
    console.log(peros)
  }
});
