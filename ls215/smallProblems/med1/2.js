// https://launchschool.com/exercises/1aa322c0

'use strict';

/*
input: number, and n rotations
output: A number but with digits rotated
rules:
1. Will input ever not be a number?
2. Will n ever be 0? and if so what does that mean?
3. If n is 1 then number doesn't change. and if n is 6 its the same rotates
4.

735291
012345

length = 6

f - 0, 5 -> 73529
m -  5 + 1 6 -> ''
e - 6 - 1 = 5 slice(-1)

73529 + '' + 1 = 735291

735291 2 -> 735219
012345

7352 1 9

735291 3 -> 735912
012345

735 91 2

f - (0, 3) -> 735
m - (3 + 1,) = (4,) -> 91
e - 6 -3 = num[l - n] = 2



735 9 12

735291 4 -> 732915
012345

l - 6 - 4 = 2

73 291 5

front - slice(0, end)
mid - slice(end + 1)
end - length - n

front + mid + end;

735291 6 -> 352917
012345

'' + 35291 + 7

f - slice(0, 0) -> ''
m - slice(end + 1) -> 35291
e - length - n = 0 num[0] -> 7


DS:

Algo:
1. Conver the number to a string
2. End - Length of string minus n rotations to find number to move. And that is the end
3. Front - beginning to number that moves to end and exclude - slice(0, end)
4. middle - end not including all the way to the end - slice(end + 1)
5. front + middle + end;
6. convert back to a number


*/

function rotateRightmostDigits(number, n) {
  let strNum = String(number);
  let length = strNum.length;
  let end = length - n;
  let front = strNum.slice(0, end);
  let middle = strNum.slice(end + 1);
  let endingNum = strNum[end];


  return Number(front + middle + endingNum);
}




console.log(rotateRightmostDigits(735291, 1));      // 735291
console.log(rotateRightmostDigits(735291, 2));      // 735219
console.log(rotateRightmostDigits(735291, 3));      // 735912
console.log(rotateRightmostDigits(735291, 4));      // 732915
console.log(rotateRightmostDigits(735291, 5));      // 752913
console.log(rotateRightmostDigits(735291, 6));      // 352917