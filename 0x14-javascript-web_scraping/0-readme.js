#!/usr/bin/node

const argv = require('process').argv;
const file = require('fs');

const filepath = argv[2];
file.readFile(filepath, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
