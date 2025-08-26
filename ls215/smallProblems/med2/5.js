// https://launchschool.com/exercises/c1bfff07

'use strict';

/*

input: Number
output: featured number. Else error message
rules:
1. Odd number that is a multiple of 7
2. With all of its digit occuring exactly once.

49 Yes

98 No not odd


133 No because 3 appears twice.




Q:

DS:


Algo:
0. If number is 9876543201 then return error message

1. See if the current number is a multiple of 7.
2. IF not then increment it till it is
  3. Check if it is even. IF it is even add 7
  3a. Check if it has dups. if it does add 14.
  4. IF it is not that is our number. and return number
3. Else add 14 and check if there are dups.
  if there are dups then add 14.

*/


function featured(number) {
  if (number === 9876543201) return 'There is no possible number that fulfills those requirements.';

  return findNumber(number);

}

function findNumber(num) {
  if (num % 7 === 0 && !noDups(num)) return num + 14;

  let nextNum = num += 1;

  while (nextNum % 2 === 0 || nextNum % 7 !== 0) {
    nextNum += 1;
  }

  while (noDups(nextNum)) {
    nextNum += 14;
  }

  return nextNum;
}

function noDups(num) {
  let strNum = String(num);
  let set = new Set(strNum);

  if (set.size !== strNum.length) return true;

  return false;
}


console.log(featured(12));           // 21
console.log(featured(20));           // 21
console.log(featured(21));           // 35
console.log(featured(997));          // 1029
console.log(featured(1029));         // 1043
console.log(featured(999999));       // 1023547
console.log(featured(999999987));    // 1023456987
console.log(featured(9876543186));   // 9876543201
console.log(featured(9876543200));   // 9876543201
console.log(featured(9876543201));   // "There is no possible number that fulfills those requirements."