// https://launchschool.com/exercises/3e2832f7

'use strict';

function swapCase(string) {
  let newString = '';

  for (let char of string) {
    if (/[a-z]/.test(char)) {
      newString += char.toUpperCase();
    } else if (/[A-Z]/.test(char)) {
      newString += char.toLowerCase();
    } else {
      newString += char;
    }
  }

  return newString;
}

console.log(swapCase('CamelCase'));              // "cAMELcASE"
console.log(swapCase('Tonight on XYZ-TV'));      // "tONIGHT ON xyz-tv"