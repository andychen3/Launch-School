'use strict';

/*
input: string
output: object containing three properties: lowercase, uppercase, neither
rules:
1. % of characters in the string that are lowercase letter
2. % of characters that are uppercase letter
3. % of characters that are neither.
4. string will always contain at least one char.


abCdef 123 -> 10
1 / 10 -> 10%
5 /10 -> 50


AbCd +Ef -> 8
 3/ 8 -> 37.50
 3/ 8 -> 37.50
 2 /8 -> 25

DS:


Algo:
1. Create object with 3 properties to hold the amount of chars
1a. find length of string
2. Iterate through string
3. If char is uppercase add it to prop upper
3a. if lower cadd to prop lower
3c. Anything else add to prop neither
4. return object with 3 props and their total over the total length.
4a. format to two decimal places

*/



// function letterPercentages(string) {
//   let objCount = {'lowercase': 0, 'uppercase': 0, 'neither': 0};
//   let length = string.length;

//   for (let char of string) {
//     if (/[A-Z]/.test(char)) {
//       objCount.uppercase += 1;
//     } else if (/[a-z]/.test(char)) {
//       objCount.lowercase += 1;
//     } else {
//       objCount.neither += 1;
//     }
//   }

//   return {
//     lowercase: formatString(objCount.lowercase, length),
//     uppercase: formatString(objCount.uppercase, length),
//     neither: formatString(objCount.neither, length),
//   };
// }

// function formatString(count, length) {
//   return String((count / length * 100).toFixed(2));
// }


function letterPercentages(string) {
  let count = string.length;

  return {
    lowercase: (((string.match(/[a-z]/g) || []).length / count) * 100).toFixed(2),
    uppercase: (((string.match(/[A-Z]/g) || []).length / count) * 100).toFixed(2),
    neither: (((string.match(/[^a-z]/ig) || []).length / count) * 100).toFixed(2),
  };
}


console.log(letterPercentages('abCdef 123'));
// { lowercase: "50.00", uppercase: "10.00", neither: "40.00" }

console.log(letterPercentages('AbCd +Ef'));
// { lowercase: "37.50", uppercase: "37.50", neither: "25.00" }

console.log(letterPercentages('123'));
// { lowercase: "0.00", uppercase: "0.00", neither: "100.00" }