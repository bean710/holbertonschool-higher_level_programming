#!/usr/bin/node

function secondLargest (arr) {
  if (arr.length === 0 || arr.length === 1) return 0;

  let max = -Infinity;
  let res = -Infinity;

  for (const num of arr) {
    if (num >= max) {
      res = max;
      max = num;
    } else if (num > res) {
      res = num;
    }
  }

  return res;
}

const arr = process.argv.slice(2, process.argv.length);
for (let i = 0; i < arr.length; i++) {
  arr[i] = Number(arr[i]);
}
console.log(secondLargest(arr));
