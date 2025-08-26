// https://launchschool.com/exercises/3b86afc7


'use strict';

/*
input: 3 numbers that are sides of triangle
output: string on whether or not triangle is valid
rules:
1. Equilateral all three sides are equal length
2. Isosceles is two sides are equal length while third is different
3. Scalene is where all three sides are of different length.

4. Invalid triangle is length that is 0. Or if two shortest sides are not greather then longest.

Q:


DS:


Algo:
1. Validate input check if triangle is invalid
2. Check sides if all equal is eqiiateral
3. if two of the sides are equal then isoscles
4. else scalene

*/



function triangle(side1, side2, side3) {
  let sideArray = validateTriangle([side1, side2, side3]);

  if (sideArray === 'invalid') return 'invalid';

  let set = new Set(sideArray);

  if (set.size === 1) {
    return 'equilateral';
  } else if (set.size === 2) {
    return 'isosceles';
  } else {
    return 'scalene';
  }
}

function validateTriangle(array) {
  let sortedArray = array.sort((a, b) => a - b).filter(side => side !== 0);

  if (sortedArray.length !== 3) return 'invalid';
  if (sortedArray[0] + sortedArray[1] <= sortedArray[2]) return 'invalid';

  return sortedArray;
}



console.log(triangle(3, 3, 3));        // "equilateral"
console.log(triangle(3, 3, 1.5));      // "isosceles"
console.log(triangle(3, 4, 5));        // "scalene"
console.log(triangle(0, 3, 3));        // "invalid"
console.log(triangle(3, 1, 1));        // "invalid"