// https://launchschool.com/exercises/519926e4

'use strict';

/*
input: n integer
output: 8 pointed stars on the console
rules:
1. Smallest n is 7


Q:s
1. Do i have to handle the cases for when n is less then 7?
2. Is there. amax for n?
3. Is n always going to be odd?

n = 7
7x7 grid

*  *  *  0, 2 spaces
 * * *  1, 1 space in between
  ***   2, 0 spaces before and after
*******
  ***
 * * *
*  *  *

n = 7
0 -> 7 /2 - 1 floor
0 -> 2

spaces before = 2
spaces between = 0

i = 2
*  *  *
 * * *
  ***
*******
  ***
 * * *
*  *. *
2 -> 0
space before = 0
spaces between = 2

i = 0

*   *   * 0, 3 spaces
 *  *  *.  1,  2
  * * *    2, 1
   ***.    3 , 0
*********
   ***
  * * *
 *  *  *
*   *   *

n

DS


Algo:
0. create variable range that is floored divide by 2
1. Call top function pass range
  1a. initialize space = 0
  1b. initialize space between = range
  1c. iterate from 0 up to range
    2. Build string based on the space before and space between
    2a. increment space before
    2b. decrement space in between
2. Log n stars to console
3. Call bottom function pass range
  1a. initialize space = range
  1b. initialize space between = 0
  1c. iterate reverse from range up to 0
    2. Build string based on the space before and space between
    2a. decrement space before
    2b. increment space in between
*/


function star(n) {
  let range = Math.floor(n / 2);
  buildTop(range);
  console.log('*'.repeat(n));
  buildBottom(range);
}

function buildTop(n) {
  let spaceBefore = 0;
  let spaceBetween = n - 1;

  for (let i = 0; i < n; i += 1) {
    let parts = [' '.repeat(spaceBefore), '*', ' '.repeat(spaceBetween), '*', ' '.repeat(spaceBetween), '*'];
    console.log(parts.join(''));
    // console.log(' '.repeat(spaceBefore) + '*' + ' '.repeat(spaceBetween) + '*' + ' '.repeat(spaceBetween) + '*' + ' '.repeat(spaceBefore));
    spaceBefore += 1;
    spaceBetween -= 1;
  }
}

function buildBottom(n) {
  let spaceBefore = n - 1;
  let spaceBetween = 0;

  for (let i = n; i > 0; i -= 1) {
    console.log(' '.repeat(spaceBefore) + '*' + ' '.repeat(spaceBetween) + '*' + ' '.repeat(spaceBetween) + '*' + ' '.repeat(spaceBefore));
    spaceBefore -= 1;
    spaceBetween += 1;
  }
}



star(7);
// logs
// *  *  *
//  * * *
//   ***
// *******
//   ***
//  * * *
// *  *  *


// star(9);
// logs
// *   *   *
//  *  *  *
//   * * *
//    ***
// *********
//    ***
//   * * *
//  *  *  *
// *   *   *