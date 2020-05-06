#!/usr/bin/node
/*
   script that prints 3 lines: (like 1-multi_languages.js) but by using an array
   of string and a loop.
   - The first line: C is fun
   - The second line: Python is cool
   - The third line: Javascript is amazing
*/
const array = ['C is fun', 'Python is cool', 'Javascript is amazing'];

for (let i = 0; array[i]; ++i) {
  console.log(array[i]);
}
