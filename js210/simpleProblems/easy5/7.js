// https://launchschool.com/exercises/e284a929

'use strict';

function swapName(string) {
  return string.split(' ').reverse().join(', ');
}

console.log(swapName('Joe Roberts'));    // "Roberts, Joe"