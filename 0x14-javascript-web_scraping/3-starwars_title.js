#!/usr/bin/node
const request = require('request');

const [id] = process.argv.slice(2);

request(`https://swapi-api.hbtn.io/api/films/${id}`, (err, res, body) => {
  if (err) console.error(err);

  console.log(JSON.parse(body).title);
});
