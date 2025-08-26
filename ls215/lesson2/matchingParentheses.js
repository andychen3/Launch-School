// https://launchschool.com/lessons/08996120/assignments/bb6d711f

'use strict';

function isBalanced(string) {
  let stack = [];

  for (let char of string) {
    if (char === '(') {
      stack.push(char);
    } else if (char === ')') {
      if ((stack[stack.length - 1] !== '(')) {
        return false;
      } else {
        stack.pop()
      }
    }
  }

  return stack.length === 0;
}

isBalanced('What (is) this?');        // true
isBalanced('What is) this?');         // false
isBalanced('What (is this?');         // false
isBalanced('((What) (is this))?');    // true
isBalanced('((What)) (is this))?');   // false
isBalanced('Hey!');                   // true
isBalanced(')Hey!(');                 // false
isBalanced('What ((is))) up(');       // false