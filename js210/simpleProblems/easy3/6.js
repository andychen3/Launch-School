// https://launchschool.com/exercises/d8f7c48a

'use strict';

function isPalindromicNumber(number) {
  let strNum = String(number);

  return strNum === strNum.split('').reverse().join('');
}

isPalindromicNumber(34543);        // true
isPalindromicNumber(123210);       // false
isPalindromicNumber(22);           // true
isPalindromicNumber(5);            // true