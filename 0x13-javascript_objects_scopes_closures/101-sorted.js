#!/usr/bin/node
const dict = require('./101-data').dict;

const ndict = {};
for (const key of Object.keys(dict)) {
  if (!(dict[key] in ndict)) {
    ndict[dict[key]] = [key];
  } else {
    ndict[dict[key]].push(key);
  }
}

console.log(ndict);
