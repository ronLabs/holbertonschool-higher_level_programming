#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    let char = 'X';
    if (c !== undefined) {
      char = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.height));
    }
  }
};
