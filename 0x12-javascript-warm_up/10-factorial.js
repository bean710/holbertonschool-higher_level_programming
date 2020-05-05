#!/usr/bin/node

function fac (n) {
  if (isNaN(n) || n === 1) return 1;

  return n * fac(n - 1);
}

console.log(fac(Number(process.argv[2])));
