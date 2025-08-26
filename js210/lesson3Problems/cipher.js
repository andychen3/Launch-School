// https://launchschool.com/lessons/c26a6fcc/assignments/c91b43bb

function rot13(string) {
  const LETTERS_IN_ALPHABET = 26;
  const CIPHER_OFFSET = 13;
  let cipher = '';

  for (let index = 0; index < string.length; index += 1) {
    let currentChar = string[index];
    let asciiNumber = string.charCodeAt(index) + CIPHER_OFFSET;
    let newChar = String.fromCharCode(asciiNumber);

    if (currentChar >= 'a' && currentChar <= 'z') {
      if (newChar > 'z') {
        asciiNumber -= LETTERS_IN_ALPHABET;
        newChar = String.fromCharCode(asciiNumber);
      }
    } else if (currentChar >= 'A' && currentChar <= 'Z') {
      if (newChar > 'Z') {
        asciiNumber -= LETTERS_IN_ALPHABET;
        newChar = String.fromCharCode(asciiNumber);
      }
    } else {
      cipher += currentChar;
      continue;
    }

    cipher += newChar;
  }

  return cipher;
}
// console.log(rot13('Teachers open the door, but you must enter by yourself.'));

console.log(rot13(rot13('Teachers open the door, but you must enter by yourself.')));


