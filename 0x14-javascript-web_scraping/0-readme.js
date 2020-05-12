#!/usr/bin/node
const fs = require('fs');
const util = require('util');

const readFile = util.promisify(fs.readFile);

const file1 = process.argv.slice(2)[0];

async function main () {
  try {
    out = await util.promisify(fs.readFile)(file1);
    process.stdout.write(out.toString());
  } catch (e) {
    console.error(`Error reading the file: ${e}`);
  }
}

main();
