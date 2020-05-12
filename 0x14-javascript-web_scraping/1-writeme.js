#!/usr/bin/node
const fs = require('fs');
const util = require('util');

const writeFile = util.promisify(fs.writeFile);

const [file, input] = process.argv.slice(2);

async function main () {
  try {
    await writeFile(file, input);
  } catch (e) {
    console.error(`Error writing to the file: ${e}`);
  }
}

main();
