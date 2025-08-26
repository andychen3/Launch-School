// https://launchschool.com/exercises/1a7f4ec6

'use strict';

// const cleanUp = (string) => {
//   return string.replace(/\W+/g,' ');
// };

function isNotAlpha(char) {
  return (((char < 'a' || char > 'z') && ((char < 'A' || char > 'Z'))));
}

const cleanUp = (string) => {
  let result = '';

  for (let char of string) {
    if (isNotAlpha(char) && result[result.length - 1] === ' ') {
      continue;
    } else if (isNotAlpha(char) && result[result.length - 1] !== ' ') {
      result += ' ';
    } else {
      result += char;
    }
  }

  return result;
};

console.log(cleanUp("---what's my +*& line?"));    // " what s my line "