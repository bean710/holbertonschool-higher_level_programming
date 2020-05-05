#!/usr/bin/node

function fac (n) {
  if (isNaN(n)) n = 1;

  let total = n;

  for (n--; n > 0; n--) {
    total *= n;
  }

  return total;
}

console.log(fac(Number(process.argv[2])));
