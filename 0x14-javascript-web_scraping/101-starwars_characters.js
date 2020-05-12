#!/usr/bin/node
const util = require('util');
const request = require('request');

const [id] = process.argv.slice(2);

const req = util.promisify(request);

async function main () {
  const movieRes = await req(`https://swapi-api.hbtn.io/api/films/${id}`);
  const movie = JSON.parse(movieRes.body);
  const characters = movie.characters;

  const reqs = [];

  // reqs = [req(character) for character in characters];
  for (let i = 0; i < characters.length; i++) {
    reqs.push(req(characters[i]));
  }

  const [...fchars] = await Promise.all(reqs);

  for (let i = 0; i < fchars.length; i++) {
    console.log(JSON.parse(fchars[i].body).name);
  }
}

main();
