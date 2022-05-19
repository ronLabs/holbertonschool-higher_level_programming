#!/usr/bin/node
const axios = require('axios');
const url = process.argv[2];

axios(url, { json: true }, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const resOut = {};
  for (const rs of body) {
    if (rs.completed) {
      if (resOut[rs.userId] === undefined) {
        resOut[rs.userId] = 0;
      }
      resOut[rs.userId] += 1;
    }
  }
  console.log(resOut);
});
