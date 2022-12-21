#!/usr/bin/node
exports.esrever = function (list) {
  const tsil = [];
  for (let i = list.length - 1; i >= 0; i--) {
    tsil.push(list[i]);
  }
  return tsil;
};
