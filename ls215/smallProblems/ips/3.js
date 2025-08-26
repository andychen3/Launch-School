// https://launchschool.com/exercises/ff1cee69

'use strict';

/*
input: string
output: boolean
rules:
1. case insensitive.

B:O   X:K   D:Q   C:P   N:A
G:T   R:E   F:S   J:W   H:U
V:I   L:Y   Z:M

(J,E, S, T)

jest

T

Q's
1. Ever be an empty string?
2. What about numbers or other symbols?

DS:
1. set to check for dups
2. hash map to build out the blocks


Algo:
1. lowercase all the words
2. Build hashmap both ways of the blocks
3. Iterate through the string
4 check if the string's partner is in the seen set
  4a. if not add the current string to seen
  4b. if it is automatically return false
5. return true

*/

const pairs = [
  ['B', 'O'], ['G', 'T'], ['V', 'I'], ['X', 'K'], ['R', 'E'], ['L', 'Y'],
  ['D', 'Q'], ['F', 'S'], ['Z', 'M'], ['C', 'P'], ['J', 'W'], ['N', 'A'],
  ['H', 'U']
];

function isBlockWord(string) {
  const blockMap = new Map(pairs.flatMap(([a, b]) => [[a, b], [b, a]]));
  let seen = new Set();

  for (let char of string.toUpperCase()) {
    let blockMate = blockMap.get(char);
    if (seen.has(blockMate) || seen.has(char)) return false;
    seen.add(char);
    seen.add(blockMate);
  }

  return true;
}


// function isBlockWord(string) {
//   const blockMap = new Map(
//     pairs.flatMap(([a, b]) => [[a, b], [b, a]])
//   );
//   let seen = new Set();
//   let lowerString = string.toLowerCase();

//   for (let char of lowerString) {
//     let blockMate = blockMap.get(char);
//     if (seen.has(blockMate) || seen.has(char)) return false;
//     seen.add(char);
//     seen.add(blockMate);
//   }

//   return true;
// }

// console.log(isBlockWord('BATCH'));      // true
// console.log(isBlockWord('BUTCH'));      // false
// console.log(isBlockWord('jest'));       // true
// console.log(isBlockWord('bon'));       // false

console.log(isBlockWord('BATCH'));      // true
console.log(isBlockWord('BUTCH'));      // false
console.log(isBlockWord('jest'));       // true
console.log(isBlockWord('floW'));       // true
console.log(isBlockWord('APPLE'));      // false
console.log(isBlockWord('apple'));      // false
console.log(isBlockWord('apPLE'));      // false
console.log(isBlockWord('Box'));        // false