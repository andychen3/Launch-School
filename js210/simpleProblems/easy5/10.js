// https://launchschool.com/exercises/2d0aaa14

'use strict';

function reverseWords(string) {
  return string.split(' ').map(word => word.length >= 5 ? reversed(word) : word).join(' ')
}

function reversed(word) {
  return word.split('').reverse().join('');
}

console.log(reverseWords('Professional'));             // "lanoisseforP"
console.log(reverseWords('Walk around the block'));    // "Walk dnuora the kcolb"
console.log(reverseWords('Launch School'));            // "hcnuaL loohcS"