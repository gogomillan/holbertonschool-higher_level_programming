#!/usr/bin/node
/*
   function that increments and calls a function.
   - The function is visible from outside
   - Prototype: function (number, theFunction)
 */
exports.addMeMaybe = function (x, theFunction) {
  theFunction(x + 1);
};
