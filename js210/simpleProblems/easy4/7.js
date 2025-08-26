// https://launchschool.com/exercises/7369178f

'use strict';

function multiplyList(arr1, arr2) {
  return arr1.map((num, index) => num * arr2[index]);
}

console.log(multiplyList([3, 5, 7], [9, 10, 11]));    // [27, 50, 77])