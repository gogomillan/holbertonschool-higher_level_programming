#!/usr/bin/node
/*
   script that prints x times C is fun
   - Where x is the first argument of the script
   - If the first argument cant be converted to an integer, print Missing number
     of occurrences
*/
if (!process.argv[2]) {
  console.log('Missing number of occurences');
} else if (process.argv[2] > 0) {
  for (let i = process.argv[2]; i; --i) {
    console.log('C is fun');
  }
}
