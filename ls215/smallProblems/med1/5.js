// https://launchschool.com/exercises/f9bfe9aa

'use strict';

/*
input: string
output: string with string numbers converted to digits
rules:
1. every number converted to their numerical value
2. Rest of the string is unchanged.


DS:
1. Map to hold the string numeric values to their digit counterparts




Algo:
1. Create a map that holds the value
1a. set result to an empty array
2. Split the string into an array.
3. Loop through the array and check if word in map. If so replace it.
If not just add the current value
4. Join array



*/


// function wordToDigit(string) {
//   if (!string) return '';
//   let digitObj = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
//     'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
//   let result = []

//   for (let word of string.split(' ')) {
//     let sanitizedWord = word.replace(/[.?!]$/g, '');
//     let punctuation = word[word.length - 1].match(/[!.?]/g);

//     if (sanitizedWord in digitObj) {
//       let digit = digitObj[sanitizedWord];
//       if (punctuation !== null) {
//         digit += word[word.length - 1];
//       }
//       result.push(digit);
//     } else {
//       result.push(word);
//     }
//   }

//   return result.join(' ');
// }




console.log(wordToDigit('Please call me at five five five one two three four. Thanks.'));
// "Please call me at 5 5 5 1 2 3 4. Thanks."

