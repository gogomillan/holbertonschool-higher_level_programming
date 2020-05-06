#!/usr/bin/node
/*
   script that searches the second biggest integer in the list of arguments.
   - All arguments can be converted to integer
   - If no argument passed, print 0
   - If the number of arguments is 1, print 0
 */
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  const array = process.argv.slice(2).sort((a, b) => a - b);
  const len = array.length;

  console.log(array[len - 2]);
}
