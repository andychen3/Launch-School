// https://launchschool.com/lessons/c26a6fcc/assignments/7d2c6cf9


function substr(string, start, length) {
  if (start < 0) {
    start = string.length + start;
  }

  if (length > string.length) {
    length = string.length;
  }

  let substring = '';

  for (let count = 0; count < length; count += 1) {
    if (start + count === string.length) {
      break;
    }
    substring += string[start + count];
  }

  return substring;
}

let string = 'hello world';

console.log(substr(string, 2, 4));      // "llo "
console.log(substr(string, -3, 2));     // "rl"
console.log(substr(string, 8, 20));     // "rld"
console.log(substr(string, 0, -20));    // ""
console.log(substr(string, 0, 0));      // ""