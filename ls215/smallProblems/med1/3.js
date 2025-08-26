
'use strict';

/*
input: Number
output:
rules:

735291 -> 6 -> 352917
012345

352917 -> 5 ->
012345

length = 6
end = 6 - 5 = 1

front = 3
mid = 2917
end = 5

Q:


D:


A:


*/




function maxRotation(number) {
  let strNum = String(number);
  let newNum = number;

  for (let i = strNum.length; i > 0; i -= 1) {
    newNum = rotateRightmostDigits(newNum, i);
  }

  return newNum;
}

function rotateRightmostDigits(number, n) {
  let strNum = String(number);
  let length = strNum.length;
  let end = length - n;
  let front = strNum.slice(0, end);
  let middle = strNum.slice(end + 1);
  let endingNum = strNum[end];


  return Number(front + middle + endingNum);
}



console.log(maxRotation(735291));          // 321579
console.log(maxRotation(3));               // 3
console.log(maxRotation(35));              // 53
console.log(maxRotation(105));             // 15 -- the leading zero gets dropped
console.log(maxRotation(8703529146));      // 7321609845