#!/usr/bin/node
/*
   function that returns the reversed version of a list:
 */
exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length, j = 0; i > 0; i--, j++) {
    newList[j] = list[i - 1];
  }
  return newList;
};
