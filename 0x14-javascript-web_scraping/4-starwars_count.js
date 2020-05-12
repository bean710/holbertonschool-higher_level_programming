#!/usr/bin/node
const request = require('request');

const [url] = process.argv.slice(2);

request(url, (err, res, body) => {
  if (err) console.error(err);

  const results = JSON.parse(body).results;

  let total = 0;
  for (let i = 0; i < results.length; i++) {
    if (results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      total++;
    }
  }

  console.log(total);
});
