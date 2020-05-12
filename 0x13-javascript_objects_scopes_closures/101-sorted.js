#!/usr/bin/node
/*
   script that imports an array and order into a new array.
 */
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
