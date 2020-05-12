#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const [url, file] = process.argv.slice(2);

request(url).pipe(fs.createWriteStream(file));
