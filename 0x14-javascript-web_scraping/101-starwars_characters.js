#!/usr/bin/node
const request = require('request');
const Film = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
request(apiUrl + Film, (error, response, body) => {
  if(!error) {
    const persos = JSON.parse(body).characters;
    console.log(persos)
  }
});
