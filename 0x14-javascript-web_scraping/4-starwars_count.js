#!/usr/bin/node
const request = require('request');

const [url] = process.argv.slice(2);

request(url, (err, res, body) => {
  if (err) return;

  const results = JSON.parse(body).results;

  let total = 0;
  const waurl = 'https://swapi-api.hbtn.io/api/people/18/';
  for (let i = 0; i < results.length; i++) {
    if (results[i].characters.includes(waurl)) {
      total++;
    }
  }

  console.log(total);
});
