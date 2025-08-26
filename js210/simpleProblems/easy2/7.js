// https://launchschool.com/exercises/176497b0

'use strict';

function twice(number) {
  let strNum = String(number);
  let mid = Math.floor(strNum.length / 2);
  let num1 = strNum.slice(0, mid);
  let num2 = strNum.slice(mid);

  if (num1 === num2) {
    return number;
  } else {
    return number * 2;
  }
}

twice(37);          // 74
twice(44);          // 44
twice(334433);      // 668866
twice(444);         // 888
twice(107);         // 214
twice(103103);      // 103103
twice(3333);        // 3333
twice(7676);        // 7676