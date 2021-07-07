#!/usr/bin/node
exports.esrever = function (list) {
  const revlist = [];
  for (let idx = list.length - 1; idx >= 0; idx--) {
    revlist.push(list[idx]);
  }
  return revlist;
};
