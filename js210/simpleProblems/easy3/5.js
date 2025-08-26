// https://launchschool.com/exercises/2a2dbd46

'use strict';

function isRealPalindrome(string) {
  let replacedString = string.replace(/[^a-z0-9]/g, '');
  replacedString = replacedString.toLowerCase();

  return replacedString === replacedString.split('').reverse().join('');
}

console.log(isRealPalindrome('madam'));               // true
console.log(isRealPalindrome('Madam'));               // true (case does no)t matter)
console.log(isRealPalindrome("Madam, I'm Adam"));     // true (only alphanumeric)s matter)
console.log(isRealPalindrome('356653'));              // true
console.log(isRealPalindrome('356a653'));             // true
console.log(isRealPalindrome('123ab321'));            // false