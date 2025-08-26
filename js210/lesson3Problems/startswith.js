// https://launchschool.com/lessons/c26a6fcc/assignments/b818db3f

function startsWith(string, searchString) {
  if (searchString === '') {
    return true;
  }

  let searchStringLength = searchString.length;
  let word = '';

  for (let index = 0; index < searchStringLength; index += 1) {
    word += string[index];
  }

  return word === searchString;
}


let str = 'We put comprehension and mastery above all else';
console.log(startsWith(str, 'We'));              // true
console.log(startsWith(str, 'We put'));          // true
console.log(startsWith(str, ''));                // true
console.log(startsWith(str, 'put'));             // false

let longerString = 'We put comprehension and mastery above all else!';
console.log(startsWith(str, longerString));      // false