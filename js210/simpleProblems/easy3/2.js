// https://launchschool.com/exercises/3e06242a

'use strict';

let relSync = require('readline-sync');
let numbers = [];
let lastNumber = null;

for (let i = 1; i <= 6; i += 1) {
  let number = (Number(relSync.question(`Enter the ${getNumber(i)} number: `)));
  if (i !== 6) {
    numbers.push(number);
  } else {
    lastNumber = number;
  }

}

if (numberInArray(lastNumber)) {
  console.log(`The number ${lastNumber} appears in [${numbers.join(', ')}].`);
} else {
  console.log(`The number ${lastNumber} does not appears in [${numbers.join(', ')}].`);
}


function numberInArray(number) {
  return numbers.some(num => number === num);
}


function getNumber(num) {
  switch (num) {
    case 1: return '1st';
    case 2: return '2nd';
    case 3: return '3rd';
    case 6: return 'last';
    default: return String(num) + 'th';
  }
}