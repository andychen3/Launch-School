// https://launchschool.com/exercises/35f0d44e

'use strict';

/*
input: 3 integer values
output: string representing acute right obtuse or invalid
rules:
1. Right angle is one angle is 90
2. Acute is all angles are less then 90
3. Obtuse is one angle is greater then 90

4. Invalid is when sum of all angles is not exactly 180. And if there
is an angle that is 0.


Q:



DS:



Algo:




*/



function triangle(angle1, angle2, angle3) {
  if (validateTriangle([angle1, angle2, angle3]) === 'invalid') return 'invalid';
  let angleArray = [angle1, angle2, angle3];

  if (angleArray.every(angle => angle !== 90)) {
    return 'acute';
  } else if (angleArray.includes(90)) {
    return 'right';
  } else {
    return 'obtuse';
  }
}

function validateTriangle(array) {
  if (array.some(angle => angle === 0)) return 'invalid';

  if (array.reduce((total, angle) => total + angle, 0)!== 180) return 'invalid';

  return 'valid';
}


console.log(triangle(60, 70, 50));       // "acute"
console.log(triangle(30, 90, 60));       // "right"
console.log(triangle(120, 50, 10));      // "obtuse"
console.log(triangle(0, 90, 90));        // "invalid"
console.log(triangle(50, 50, 50));       // "invalid"