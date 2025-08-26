// https://launchschool.com/lessons/c26a6fcc/assignments/fabf4a46

const splitString = function(string, delimiter) {
  if (delimiter === undefined) {
    console.log('Error: No delimiter');
    return;
  }

  let word = '';

  for (let char of string) {
    if (delimiter === '') {
      console.log(char);
    } else if (char === delimiter) {
      console.log(word);
      word = '';
    } else {
      word += char;
    }
  }
  if (word) {
    console.log(word);
  }
};

splitString('abc,123,hello world', ',');
// logs:
// abc
// 123
// hello world

splitString('hello');
// logs:
// ERROR: No delimiter

splitString('hello', '');
// logs:
// h
// e
// l
// l
// o

splitString('hello', ';');
// logs:
// hello

splitString(';hello;', ';');