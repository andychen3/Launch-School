// https://launchschool.com/exercises/063ab637

'use strict';

function century(year) {
  let getCentury = Math.floor(year / 100) + 1;

  if (year % 100 === 0) {
    getCentury -= 1;
  }

  return String(getCentury) + centurySuffix(getCentury);
}

function centurySuffix(centuryNumber) {
  if (catchWithTh(centuryNumber % 100)) {
    return 'th';
  }

  let lastDigit = centuryNumber % 10;
  switch (lastDigit) {
    case 1: return 'st';
    case 2: return 'nd';
    case 3: return 'rd';
    default: return 'th';
  }
}

function catchWithTh(lastTwo) {
  return lastTwo === 11 || lastTwo === 12 || lastTwo === 13;
}

console.log(century(2000));        // "20th"
console.log(century(2001));        // "21st"
console.log(century(1965));        // "20th"
console.log(century(256));         // "3rd"
console.log(century(5));           // "1st"
console.log(century(10103));       // "102nd"
console.log(century(1052));        // "11th"
console.log(century(1127));        // "12th"
console.log(century(11201));       // "113th"

/*
divide by 100

always round up.

and if mod is 0 then add. 1




11 th -> th
1st
2nd
3rd


*/