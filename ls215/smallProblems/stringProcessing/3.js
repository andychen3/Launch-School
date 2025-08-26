// https://launchschool.com/exercises/ae099a61

'use strict';

function letterCaseCount(string) {
  let counter = {lowercase: 0, uppercase: 0, neither: 0};

  for (let char of string) {
    if (char.match(/[a-z]/g) !== null) {
      counter.lowercase += 1;
    } else if (char.match(/[A-Z]/g) !== null) {
      counter.uppercase += 1;
    } else {
      counter.neither += 1;
    }
  }

  return counter;
}

console.log(letterCaseCount('abCdef 123'));  // { lowercase: 5, uppercase: 1, neither: 4 }
console.log(letterCaseCount('AbCd +Ef'));    // { lowercase: 3, uppercase: 3, neither: 2 }
console.log(letterCaseCount('123'));         // { lowercase: 0, uppercase: 0, neither: 3 }
console.log(letterCaseCount(''));            // { lowercase: 0, uppercase: 0, neither: 0 }