#!/usr/bin/node
/*
  class Square that defines a square and inherits from Square of 5-square.js:
  - It is used the class notation for defining the class and extends
  - Instansce method called charPrint(c) that prints the rectangle using the
    character c:
    - If c is undefined, use the character X

 */
const s = require('./5-square');

module.exports = class Square extends s {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
