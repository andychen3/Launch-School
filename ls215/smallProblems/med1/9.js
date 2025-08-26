// https://launchschool.com/exercises/9b1769ca


'use strict';

let memo = {}

function fibonacci(n) {
  if (n <= 2) return 1;
  if (n in memo) return memo[n];
  memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
  return memo[n];
}







console.log(fibonacci(1));       // 1
console.log(fibonacci(2));       // 1
console.log(fibonacci(3));       // 2
console.log(fibonacci(4));       // 3
console.log(fibonacci(5));       // 5
console.log(fibonacci(12));      // 144
console.log(fibonacci(1000));      // 6765