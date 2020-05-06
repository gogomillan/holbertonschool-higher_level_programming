#!/usr/bin/node
/*
   script that prints the first argument passed to it:
   - If no arguments are passed to the script, print No argument
   - You must use console.log(...) to print all output
*/
if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
