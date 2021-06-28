#!/usr/bin/node
const request = require('request');
const Film = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api';
request(apiUrl + Film, (error, response, body) => {
  if (!error) {
    const persos = JSON.parse(body).persos;
    for (const perso of persos) {
      request(perso, (error, response, body) => {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
