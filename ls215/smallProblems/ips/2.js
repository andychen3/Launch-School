// https://launchschool.com/exercises/c4ee64c7

'use strict';
/*
input: an odd n number.
output: nxn diamond
rules:
1. n is always odd.

1

*


3

 *
***
 *

5

  *
 ***
*****
 ***
  *


9

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *


spaces before inserting asterik

0 -> n
0 -> 3

 *

i = 1
space = n // 2 = 0

1 * 2 = 2 - 1
2 * 2 = 4 - 1
3 * 2 = 6 - 1
4 * 2 = 8 - 1

  *
 ***
*****
 ***
  *

5 // 2 = 2

Top half:
1 -> 2 + 1
spaces = 5 // 2 = 2

  *
 ***
*****
 ***
  *

i = 1
spaces = 2
(1 * 2) - 1

i = 2
spaces = 1
(2 * 2) - 1


i = 3
spaces = 0
(3 * 2) - 1

 2 -> 0
Bottom half:
i = 2
spaces = 1
(2 * 2) - 1

i = 1
spaces = 2
(1 * 2) - 1


Q:
1. Can n be 0?
2. Can n be a negative odd number?
3. Is there a max number for n?



DS:


Algo:
1. Floor n divide by 2 to get num iterations
2. Top half
  2a. Iterate from 0 to less than equal to n // 2 + 1
      spaces = n // 2
      asteriks are (i * 2) - 1
      spaces -= 1
3. Bottom half
  3a. Iterate in reverse from n // 2 -> greater than 0
      spaces = 1
      asteriks = (i * 2) - 1
      spaces += 1

*/


function diamond(n) {
  let range = Math.floor(n / 2);

  buildTopHalf(range);
  buildBottomHalf(range);
}

function buildTopHalf(range) {
  let spaces = range;

  for (let i = 1; i <= range + 1; i += 1) {
    let numStars = (i * 2) - 1;
    console.log(`${' '.repeat(spaces)}${'*'.repeat(numStars)}`);
    spaces -= 1;
  }
}

function buildBottomHalf(range) {
  let spaces = 1;

  for (let i = range; i > 0; i -= 1) {
    let numStars = (i * 2) - 1;
    console.log(`${' '.repeat(spaces)}${'*'.repeat(numStars)}`);
    spaces += 1;
  }
}


diamond(1);
// logs
// *



diamond(3);
// logs
//  *
// ***
//  *

diamond(5);


diamond(9);
// // logs
// //     *
// //    ***
// //   *****
// //  *******
// // *********
// //  *******
// //   *****
// //    ***
// //     *