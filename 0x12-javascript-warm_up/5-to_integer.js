#!/usr/bin/node
/*
   script that prints My number: <first argument converted in integer> if the
   first argument can be converted to an integer. If the argument cant be
   converted to an integer, prints Not a number.
*/
if (!parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: %d', parseInt(process.argv[2]));
}
