#!/usr/bin/node
/*
  class Rectangle that defines a rectangle:
  - It is used the class notation for defining your class
  - The constructor take 2 arguments w and h
  - Initialize the instance attribute width with the value of w
  - Initialize the instance attribute height with the value of h
  - If w or h is equal to 0 or not a positive integer, create an empty object
  - The print() method prints the rectangle using the character X
  - Instance method rotate() that exchanges the width and the height of the
    rectangle
  - Instance method called double() that multiples the width and the height
    of the rectangle by 2
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
