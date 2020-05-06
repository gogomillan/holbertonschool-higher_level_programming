#!/usr/bin/node
/*
   script that prints a square
   - The first argument is the size of the square
   - If the first argument cant be converted to an integer, print Missing size
   - Uses the character X to print the square
*/
const size = process.argv[2];

if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else if (size > 0) {
  for (let i = 0; i < size; ++i) {
    console.log('X'.repeat(size));
  }
}
