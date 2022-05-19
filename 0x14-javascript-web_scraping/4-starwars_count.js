#!/usr/bin/node
const axios = require('axios');
const url = process.argv[2];

axios(url, { json: true }, function (error, res, body) {
  if (error) {
    return console.log(error);
  }
  const results = body.results;
  let count = 0;
  for (const rs of results) {
    for (const chr of rs.characters) {
      if (chr.indexOf('18') > 0) {
        count += 1;
      }
    }
  }
  console.log(count);
});
