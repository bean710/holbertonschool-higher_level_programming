#!/usr/bin/node
const request = require('request');

const [url] = process.argv.slice(2);

request(url, (err, res, body) => {
  if (err) console.error(err);

  const results = JSON.parse(body);

  const ret = {};
  for (let i = 0; i < results.length; i++) {
    const userid = results[i].userId;
    if (results[i].completed) {
      ret[userid] = (userid in ret ? ret[userid] + 1 : 1);
    }
  }

  console.log(ret);
});
