#!/usr/bin/node
/*
   function that executes x times a function.
   - The function is visible from outside
   - Prototype: function (x, theFunction)
 */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
