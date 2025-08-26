// https://launchschool.com/exercises/27444b15

'use strict';

const isUppercase = (string) => {
  return !/[a-z]/.test(string);
};

// const isUppercase = (string) => {
//   let regex = /[a-z]+/g;

//   if (string.match(regex) !== null) {
//     return false;
//   } else {
//     return true;
//   }
// };

// const isUppercase = (string) => {
//   for (let char of string) {
//     if (wordIsLower(char)) {
//       return false;
//     }
//   }

//   return true;
// };

// const wordIsLower = (char) => char >= 'a' && char <= 'z';


console.log(isUppercase('t'));               // false
console.log(isUppercase('T'));               // true
console.log(isUppercase('Four Score'));      // false
console.log(isUppercase('FOUR SCORE'));      // true
console.log(isUppercase('4SCORE!'));         // true
console.log(isUppercase(''));                // true