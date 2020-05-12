#!/usr/bin/node
/*
  class Square that defines a square and inherits from Rectangle of
  4-rectangle.js
  - It is used the class notation for defining the class and extends
  - The constructor take 1 argument: size
  - The constructor of Rectangle must be called (by using super())
 */
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
