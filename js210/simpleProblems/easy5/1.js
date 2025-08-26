// https://launchschool.com/exercises/478ca82d

'use strict';

function repeater(string) {
  return string.split('').map(char => char.repeat(2)).join('');
}

console.log(repeater('Hello'));        // "HHeelllloo"
console.log(repeater('Good job!'));    // "GGoooodd  jjoobb!!"
console.log(repeater(''));             // ""