'use strict';

/*
input: string
output: string but numbers replaced with alphaberts and vice versa
rules:
1. Switch the same number of numbers with same number of alphabets.
2. If there is not enough numbers or alphabet to switch those chars remain the same
3. Can have different lengths of numbers and alphabets.
4. CAn have other characters but we will leave them as is.

1a2b3c -> a1b2c3

res = 123dabc

d



abcd123
.......



abcd123 -> 123dabc

Q:
1. Will the input always be a string?
2. What do i return for an empty string? return itself?
3. What if there is other characters what to do with those?
4. How long is the string?
5. Could their be uppercase letters?

DS:


Algo:
1. Return empty string if empty string
2. replace the string with only alphabet characters
3. replace the string with only numeric characters
4. Iterate through original string
  4a.  and check if it is a number then add alphabet
    4aa. check if there is any alphabets left
        4ab. if not then add original char.
  4b. if it is a alphabet add number
    4bb. check if there is any alphabets left.
        4ab. if not then add original char
  4c. if its anything else just add that anything else
5. return result

*/

const isAlpha = char => /[a-z]/i.test(char);
const isDigit = char => /\d/.test(char);


function swap(str) {
  let alphabets = str.match(/[a-z]/ig);
  let digits = str.match(/\d/g);

  if (alphabets === null || digits === null) return str;

  return [...str].map(char => {
    if (isAlpha(char) && digits.length > 0) return digits.shift();
    if (isDigit(char) && alphabets.length > 0) return alphabets.shift();
    return char;
  }).join('');

  // for (let char of str) {
  //   if (/[a-z]/i.test(char)) {
  //     if (digitIndex < digits.length) {
  //       result += digits[digitIndex];
  //       digitIndex += 1;
  //     } else {
  //       result += char;
  //     }
  //   } else if (/\d/.test(char)) {
  //     if (alphaIndex < alphabets.length) {
  //       result += alphabets[alphaIndex];
  //       alphaIndex += 1;
  //     } else {
  //       result += char;
  //     }
  //   } else {
  //     result += char;
  //   }
  // }

  // return result;
}


// function swap(str) {
//   let alphabets = str.replace(/[^a-z]/ig, '');
//   let digits = str.replace(/[^\d]/g, '');
//   let alphaIndex = 0;
//   let digitIndex = 0;
//   let result = '';

//   for (let char of str) {
//     if (/[a-z]/i.test(char)) {
//       if (digitIndex < digits.length) {
//         result += digits[digitIndex];
//         digitIndex += 1;
//       } else {
//         result += char;
//       }
//     } else if (/\d/.test(char)) {
//       if (alphaIndex < alphabets.length) {
//         result += alphabets[alphaIndex];
//         alphaIndex += 1;
//       } else {
//         result += char;
//       }
//     } else {
//       result += char;
//     }
//   }

//   return result;
// }

console.log(swap("") === ""); // true

console.log(swap("1a2b3c") === "a1b2c3"); // true
console.log(swap("abcd123") === "123dabc"); // true
console.log(swap("12a") === "a21"); // true
console.log(swap("ab1") === "1ba"); // true
console.log(swap("abcd") === "abcd"); // true
console.log(swap("1") === "1"); // true
console.log(swap("123-4a#b$") === "ab3-41#2$"); // true
console.log(swap('125-e-b') === 'eb5-1-2')
console.log(swap("ab1CD23") === "12a3DbC"); // true