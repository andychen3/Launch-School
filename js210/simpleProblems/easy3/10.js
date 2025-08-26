// https://launchschool.com/exercises/5401a895

'use strict';

function wordSizes(string) {
  if (!string) return {};

  let replacedString = string.replace(/[^a-z\s]/gi, '');
  console.log(replacedString)
  return replacedString.split(' ')
                       .map(word => word.length)
                       .reduce((obj, wordLength) => {
                        obj[wordLength] ? obj[wordLength] += 1 : obj[wordLength] = 1;
                        return obj;
                       }, {});
}

console.log(wordSizes('Four score and seven.'));                       // { "3": 1, "4": 1, "5": 2 }
console.log(wordSizes('Hey diddle diddle, the cat and the fiddle!'));  // { "3": 5, "6": 3 }
console.log(wordSizes("What's up doc?"));                              // { "5": 1, "2": 1, "3": 1 }
console.log(wordSizes(''));                                            // {}