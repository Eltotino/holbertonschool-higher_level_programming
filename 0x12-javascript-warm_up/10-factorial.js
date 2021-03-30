#!/usr/bin/node
function factorial (value) {
  if (!value || value < 2) {
  	return(1);
  }
  return value * factorial(value -1);
}
console.log(factorial(Number(process.argv[2])));
