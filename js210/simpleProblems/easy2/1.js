// https://launchschool.com/exercises/5f3323e6

function crunch(string) {
  let newString = '';

  for (let char of string) {
    if (newString[newString.length - 1] !== char) {
      newString += char;
    }
  }

  return newString;
}

crunch('ddaaiillyy ddoouubbllee');    // "daily double"
crunch('4444abcabccba');              // "4abcabcba"
crunch('ggggggggggggggg');            // "g"
crunch('a');                          // "a"
crunch('');                           // ""