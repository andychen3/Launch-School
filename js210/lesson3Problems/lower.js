// https://launchschool.com/lessons/c26a6fcc/assignments/7a0c1db0

// 65 - 90

function toLowerCase(string) {
  const CONVERSION_OFFSET = 32;
  let lowerCaseWord = '';

  for (let index = 0; index < string.length; index += 1) {
    let asciiNumber = string.charCodeAt(index);

    if (asciiNumber < 65 || asciiNumber > 90) {
      lowerCaseWord += string[index];
    } else {
      asciiNumber += CONVERSION_OFFSET;
      lowerCaseWord += String.fromCharCode(asciiNumber);
    }
  }

  return lowerCaseWord;
}


console.log(toLowerCase('ALPHABET'));    // "alphabet")
console.log(toLowerCase('123'));         // "123")
console.log(toLowerCase('abcDEF'));