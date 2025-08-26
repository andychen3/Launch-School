// https://launchschool.com/exercises/757204fb

'use strict';

function leadingSubstrings(string) {
  return [...string].map((_, index) => string.slice(0, index + 1));
}

function substrings(string) {
  let result = [];

  [...string].forEach((_, index) => {
    result.push(...leadingSubstrings(string.slice(index)));
  });

  return result;
}

substrings('abcde');

// 'use strict';

// function leadingSubstrings(string) {
//   return [...string].map((_, index) => string.slice(0, index + 1));
// }

// function substrings(string) {
//   return [...string].flatMap((_, index) => leadingSubstrings(string.slice(index)));
// }

// // let result = [];

//   // for (let i = 0; i < string.length; i += 1) {
//   //   for (let j = i; j < string.length; j += 1) {
//   //     result.push(string.slice(i, j + 1));
//   //   }
//   // }

//   // return result;


// // function substrings(string) {
// //   return [...string].flatMap((_, i, array) => [...string].slice(i).map((_, j) => string.slice(i, j + i + 1)));
// // }


// console.log(substrings('abcde'));

// // returns
// // [ "a", "ab", "abc", "abcd", "abcde",
// //   "b", "bc", "bcd", "bcde",
// //   "c", "cd", "cde",
// //   "d", "de",
// //   "e" ]