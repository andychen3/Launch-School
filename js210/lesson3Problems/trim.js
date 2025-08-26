const trim = function(string) {
  let beginningWordIndex = null;
  let endingWordIndex = null;

  for (let i = 0; i < string.length; i += 1) {
    if (string[i] !== ' ') {
      beginningWordIndex = i;
      break;
    }
  }

  for (let j = string.length - 1; j >= 0; j -= 1) {
    if (string[j] !== ' ') {
      endingWordIndex = j;
      break;
    }
  }

  return string.slice(beginningWordIndex, endingWordIndex + 1);
};


console.log(trim('  abc  '));  // "abc"
console.log(trim('abc   '));   // "abc"
console.log(trim(' ab c'));    // "ab c"
console.log(trim(' a b  c'));  // "a b  c"
console.log(trim('      '));   // ""
console.log(trim(''));         // ""