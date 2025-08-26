// https://launchschool.com/exercises/bc3c42c5

'use strict';

/*
input: string and keyword
output: ciphertext
rules:
1. Case doesn't matter
2. ONly apply to alphabets

012345678910111213141516171819202122232425
abcdefghij k l m n o p r q s t u v w x y z

3 + 16 = 19

r -> 16
a-> 0
b-> 1

B - > 1

d -> 3

p -> 15 + 12 = 27

i -> 8
e -> 4


Pine -> Bmnx

m e -> 2
12 4

index = 2
upper = False

P -> 15 + 12 = 27 % 26
i  -> 8 + 4 = 12 % 26 = 12
n ->  13 + 12 = 25 % 26 = 25
e -> 4 + 4 = 8 =

3 % 2 = 1
e -> 4


Bmzi


Q's:
1. array that maps indexes to the letters.


DS:

Algo:
0. result to empty string
1. Create array of alphabet characters mapping to index
1a. find length of keyword
2. Iterate through string
  2a. if alphabet
    3. Check if it is upper or lower then set boolean to either true or false
    4. Find what index the char is at and add it to the index of the char of the keyword
    5. mod the keyword by the length to get the index of current char of keyword
    6. if upper uppercase the char then add to result if not just add to result as is.
  6. if not alphabet
    skip doing cipher on non alphabet characters and add to result
7. return result

*/

const alphabetMapping = 'abcdefghijklmnopqrstuvwxyz'.split('');

function cipher(string, keyword) {
  let result = '';
  let length = keyword.length;
  let keyIndex = 0;

  for (let i = 0; i < string.length; i += 1) {
    let keywordUnicode = keyword[keyIndex % length].toLowerCase();
    let char = string[i];
    let lowerCaseChar = char.toLowerCase();

    if (/[A-Z]/.test(char)) {
      let unicode = (alphabetMapping.indexOf(lowerCaseChar) + alphabetMapping.indexOf(keywordUnicode)) % 26;
      result += alphabetMapping[unicode].toUpperCase();
      keyIndex += 1;
    } else if (/[a-z]/.test(char)) {
      let unicode = (alphabetMapping.indexOf(lowerCaseChar) + alphabetMapping.indexOf(keywordUnicode)) % 26;
      result += alphabetMapping[unicode];
      keyIndex += 1;
    } else {
      result += char;
    }
  }

  return result;
}


console.log(cipher('Pine', 'me')) // Bmzi
console.log(cipher("Pineapples don't go on pizzas!", 'A')) // Pineapples don't go on pizzas!
console.log(cipher("Pineapples don't go on pizzas!", 'meat')) //  Bmnxmtpeqw dhz'x gh ar pbldal!
console.log(cipher("Pineapples don't go on pizzas!", 'Aa')) // Pineapples don't go on pizzas!
console.log(cipher("Pineapples don't go on pizzas!", 'cab')) // Riogaqrlfu dpp't hq oo riabat!
console.log(cipher("Dog", 'Rabbit'))   // Uoh