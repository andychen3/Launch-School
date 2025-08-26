// https://launchschool.com/lessons/c26a6fcc/assignments/4e531b61

function indexOf(firstString, secondString) {
  let startIndex = -1;
  let word = '';
  let secondStringIndex = 0;

  for (let index = 0; index < firstString.length; index += 1) {
    if (secondStringIndex >= secondString.length) {
      break;
    }

    if (firstString[index] === secondString[secondStringIndex]) {
      word += firstString[index];
      secondStringIndex += 1;
      if (startIndex === -1) {
        startIndex = index;
      }
    } else {
      startIndex = -1;
      word = '';
      secondStringIndex = 0;
    }
  }

  if (word === secondString) {
    return startIndex;
  } else {
    return -1;
  }

}

function lastIndexOf(firstString, secondString) {
  let startIndex = -1;
  let word = '';
  let secondStringIndex = 0;

  for (let index = 0; index < firstString.length; index += 1) {
    if (firstString[index] === secondString[secondStringIndex]) {
      word += firstString[index];
      secondStringIndex += 1;
      if (startIndex === -1) {
        startIndex = index;
      }
    } else {
      startIndex = -1;
      word = '';
      secondStringIndex = 0;
    }
  }

  if (word === secondString) {
    return startIndex;
  } else {
    return -1;
  }

}

console.log(indexOf('Some strings', 's'));                      // 5
console.log(indexOf('Blue Whale', 'Whale'));                    // 5
console.log(indexOf('Blue Whale', 'Blute'));                    // -1
console.log(indexOf('Blue Whale', 'leB'));                      // -1


console.log(lastIndexOf('Some strings', 's'));                  // 11
console.log(lastIndexOf('Blue Whale, Killer Whale', 'Whale'));  // 19
console.log(lastIndexOf('Blue Whale, Killer Whale', 'all'));    // -1