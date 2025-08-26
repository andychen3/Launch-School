// https://launchschool.com/exercises/ee15e5a3

'use strict';

// function sequence(num1, num2) {
//   let start = 0;
//   return Array.from({length: num1}).map(() => {
//     start += num2;
//     return start;
//   });
// }

function sequence(num1, num2) {
  return Array.from({ length: num1 }).map((_, idx) => num2 * (idx + 1));
}

console.log(sequence(5, 1));          // [1, 2, 3, 4, 5]
console.log(sequence(4, -7));         // [-7, -14, -21, -28]
console.log(sequence(3, 0));          // [0, 0, 0]
console.log(sequence(0, 1000000));    // []