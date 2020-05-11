#!/usr/bin/node
exports.esrever = function (list) {
  const ret = [];

  for (let i = 0; i < list.length; i++) {
    ret.unshift(list[i]);
  }

  return ret;
};
