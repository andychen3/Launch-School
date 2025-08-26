// https://launchschool.com/exercises/5196dead

'use strict';

// function doubleConsonants(string) {
//   return string.split('').map(isAlpha).join('');
// }

// function isAlpha(char) {
//   let lowerChar = char.toLowerCase();
//   if (!'aeiou'.includes(lowerChar) && (lowerChar >= 'b' && lowerChar <= 'z')) {
//     return char + char;
//   } else {
//     return char;
//   }
// }

function doubleConsonants(string) {
  return string.replace(/([^aeiou\W_\d])/gi, '$1$1');
}

console.log(doubleConsonants('String'));          // "SSttrrinngg"
console.log(doubleConsonants('Hello-World!'));    // "HHellllo-WWorrlldd!"
console.log(doubleConsonants('July 4th'));        // "JJullyy 4tthh"
console.log(doubleConsonants(''));                // ""