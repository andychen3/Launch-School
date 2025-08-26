// https://launchschool.com/exercises/3c9aad3b

const shortLongShort = function(string1, string2) {
  if (string1.length <= string2.length) {
    return string1 + string2 + string1;
  }

  return string2 + string1 + string2;
};

console.log(shortLongShort('abc', 'defgh'));
console.log(shortLongShort('abcde', 'fgh'));
console.log(shortLongShort('', 'xyz'));


