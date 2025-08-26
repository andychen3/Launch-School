// https://launchschool.com/exercises/e312c4cf?track=python

'use strict';

function fibonacci(n) {
  let first = 1;
  let second = 1;

  for (let i = 1; i < n; i += 1) {
    let temp = first + second;
    second = first;
    first = temp;
  }

  return second;
}


console.log(fibonacci(20));       // 6765
console.log(fibonacci(50));       // 12586269025
console.log(fibonacci(75));       // 2111485077978050