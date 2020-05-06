#!/usr/bin/node
/*
   script that prints two arguments passed to it, in the following format: is
*/
if (!process.argv[2]) {
  console.log('undefined is undefined');
} else {
  console.log(process.argv[2].concat(' is ', process.argv[3]));
}
