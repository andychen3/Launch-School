// https://launchschool.com/exercises/8c72838d

'use strict';

function union(arr1, arr2) {
  return [...new Set([...arr1, ...arr2])];
}

console.log(union([1, 3, 5], [3, 6, 9]));    // [1, 3, 5, 6, 9]
