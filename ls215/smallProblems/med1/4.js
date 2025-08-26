// https://launchschool.com/exercises/6d0a9bf4?track=python

'use strict';


function minilang(string) {
  let register = 0;
  let stack = [];

  for (let value of string.split(' ')) {
    if (value === 'PRINT') {
      console.log(register);
    } else if (value === 'ADD') {
      register = stack.pop() + register;
    } else if (value === 'SUB') {
      register = register - stack.pop();
    } else if (value === 'PUSH') {
      stack.push(register);
    } else if (value === 'MULT') {
      register = stack.pop() * register;
    } else if (value === 'DIV') {
      register = Math.floor(register / stack.pop());
    } else if (value === 'REMAINDER') {
      register = register % stack.pop();
    } else if (value === 'POP') {
      register = stack.pop()
    } else {
      register = Number(value);
    }
  }
}


console.log(minilang('PRINT'));
// 0

console.log(minilang('5 PUSH 3 MULT PRINT'));
// 15

console.log(minilang('5 PRINT PUSH 3 PRINT ADD PRINT'));
// 5
// 3
// 8

minilang('5 PUSH POP PRINT');
// 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT');
// 5
// 10
// 4
// 7


minilang('3 PUSH PUSH 7 DIV MULT PRINT');
// 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT');
// 12

minilang('-3 PUSH 5 SUB PRINT');
// 8

minilang('6 PUSH');
// (nothing is printed because the `program` argument has no `PRINT` commands)