#!/usr/bin/node
/*
   script that prints the addition of 2 integers
   - The first argument is the first integer
   - The second argument is the second integer
*/
function add (a, b) {
  return a + b;
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
