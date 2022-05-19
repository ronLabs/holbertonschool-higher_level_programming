#!/usr/bin/node

const argv = require('process').argv;
const file = require('fs');

const filepath = argv[2];
const data = argv[3];
file.writeFile(filepath, data, 'utf8', function (err, data) {
  if (err) { console.log(err); }
});
