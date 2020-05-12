#!/usr/bin/node
const request = require('request');
const util = require('util');

const req = util.promisify(request);
const [url] = process.argv.slice(2);

async function main () {
  try {
    const res = await req(url);
    console.log(`code: ${res.statusCode}`);
  } catch (e) {
    console.error(`Problem with the request: ${e}`);
  }
}

main();
