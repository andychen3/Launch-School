// https://launchschool.com/exercises/c86ceb32

'use strict';

// function swap(string) {
//   let splitString = string.split(' ');
//   let newString = [];

//   for (let word of splitString) {
//     newString.push(switchFirstAndLast(word));
//   }

//   return newString.join(' ');
// }

// function switchFirstAndLast(word) {
//   let newWord = word.split('');
//   let length = word.length - 1;

//   [newWord[0], newWord[length]] = [newWord[length], newWord[0]];

//   return newWord.join('');
// }

function swap(string) {
  return string.split(' ').map(word => {
    if (word.length === 1) {
      return word;
    } else {
      return word[word.length - 1] + word.slice(1, -1) + word[0];
    }
  }).join(' ');
}

console.log(swap('Oh what a wonderful day it is'));  // "hO thaw a londerfuw yad ti si"
console.log(swap('Abcde'));                          // "ebcdA"
console.log(swap('a'));                              // "a"