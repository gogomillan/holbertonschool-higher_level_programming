#!/usr/bin/node
/*
   script that computes and prints a factorial
   - The first argument is integer (argument can be cast as integer) used for
     computing the factorial
   - Factorial of NaN is 1
   - Recursively
*/
function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
