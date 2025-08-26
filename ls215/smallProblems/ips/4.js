// https://launchschool.com/exercises/1998e7d6

'use strict';

/*
input: string, shift value
output: string that is encrypted
rules:
1. Only encrypts letters both uppper and lower. Rest leave as is
2. If key value exceeds length of alphabet it wraps around to beginning
3. There are 26 alphabets.



012345
ABCDEF



Mod the shift value


Q's
1. Empty string?
2. Negative shift value?

DS:
1. Object to hold values


Algo:
0. Have result as empty string
1. Iterate through the string
2. Determine if the character is an upper or lowercase letter
  2a. If alphabet we find unicode
    2aa. We add this unicode value by the (shift value mod 26).
      2aaa. If it is lowercase and we add shift value is over 122 we mod by 122 and then add 96
      2aaa. If it is uppercase and we add shift value is over 90 we mod by 90 and then add 64
    2ab. Then add that char to result
  2b. else if not we leave as is an add to result
3. return result

*/


function caesarEncrypt(string, shiftValue) {
  let result = '';

  for (let char of string) {
    if (/[a-z]/.test(char)) {
      result += lowercase(char, shiftValue % 26);
    } else if (/[A-Z]/.test(char)) {
      result += uppercase(char, shiftValue % 26);
    } else {
      result += char;
    }
  }

  console.log(result);
}


function lowercase(char, shiftVal) {
  let unicodeValue = char.charCodeAt() + shiftVal;

  if (unicodeValue > 122) {
    unicodeValue = unicodeValue % 122 + 96;
  }

  return String.fromCharCode(unicodeValue);
}

function uppercase(char, shiftVal) {
  let unicodeValue = char.charCodeAt() + shiftVal;

  if (unicodeValue > 90) {
    unicodeValue = unicodeValue % 90 + 64;
  }

  return String.fromCharCode(unicodeValue);
}


// simple shift
caesarEncrypt('A', 0);       // "A"
caesarEncrypt('A', 3);       // "D"

// wrap around
caesarEncrypt('y', 5);       // "d"
caesarEncrypt('a', 47);      // "v"

// all letters
caesarEncrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 25);
// "ZABCDEFGHIJKLMNOPQRSTUVWXY"


caesarEncrypt('The quick brown fox jumps over the lazy dog!', 5);
// "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl!"
// many non-letters
caesarEncrypt('There are, as you can see, many punctuations. Right?; Wrong?', 2);
// "Vjgtg ctg, cu aqw ecp ugg, ocpa rwpevwcvkqpu. Tkijv?; Ytqpi?"
    i?