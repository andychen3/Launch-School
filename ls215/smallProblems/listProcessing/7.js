// https://launchschool.com/exercises/b31e9777

'use strict';

function leadingSubstrings(string) {
  return [...string].map((_, index) => string.slice(0, index + 1));
}

function substrings(string) {
  let result = [];

  [...string].forEach((_, index) => {
    result.push(...leadingSubstrings(string.slice(index)));
  });

  return result;
}

function isPalindrome(word) {
  return word.length > 1 && (word === word.split('').reverse().join(''));
}

const palindromes = (string) => {
  return substrings(string).filter(isPalindrome);
};

console.log(palindromes('abcd'));       // []
console.log(palindromes('madam'));      // [ "madam", "ada" ]

console.log(palindromes('hello-madam-did-madam-goodbye'));
// returns
// [ "ll", "-madam-", "-madam-did-madam-", "madam", "madam-did-madam", "ada",
//   "adam-did-mada", "dam-did-mad", "am-did-ma", "m-did-m", "-did-", "did",
//   "-madam-", "madam", "ada", "oo" ]

console.log(palindromes('knitting cassettes'));
// returns
// [ "nittin", "itti", "tt", "ss", "settes", "ette", "tt" ]