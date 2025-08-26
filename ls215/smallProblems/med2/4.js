// https://launchschool.com/exercises/28e1b056

'use strict';

function fridayThe13ths(year) {
  let array = [];

  for (let i = 0; i < 12; i += 1) {
    let date = new Date(year, i, 13);
    array.push(date);
  }

  return array.filter(date => date.getDay() === 5).length;

}



console.log(fridayThe13ths(1986));      // 1
console.log(fridayThe13ths(2015));      // 3
console.log(fridayThe13ths(2017));      // 2