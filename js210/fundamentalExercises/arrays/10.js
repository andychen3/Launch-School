// https://launchschool.com/exercises/af3ae23e

function areArraysEqual(array1, array2) {
  if (array1.length !== array2.length) {
    return false;
  }

  let charMap = {}

  for (let val of array1) {
    let key = typeof(val) === 'string' ? val + 's' : val;
    if (key in charMap) {
      charMap[key] += 1;
    } else {
      charMap[key] = 1;
    }
  }

  for (val of array2) {
    let key = typeof(val) === 'string' ? val + 's' : val;
    if (!(key in charMap)) {
      return false;
    }

    charMap[key] -= 1
    if (charMap[key] === 0) {
      delete charMap[key];
    }
  }

  return true;
}

console.log(areArraysEqual([1, 2, 3], [1, 2, 3]));
console.log(areArraysEqual([1, 2, 3], [3, 2, 1]));
console.log(areArraysEqual(['a', 'b', 'c'], ['b', 'c', 'a']));
console.log(areArraysEqual(['1', 2, 3], [1, 2, 3]));
console.log(areArraysEqual([1, 1, 2, 3], [3, 1, 2, 1]));
console.log(areArraysEqual([1, 2, 3, 4], [1, 1, 2, 3]));
console.log(areArraysEqual([1, 1, 2, 2], [4, 2, 3, 1]));
console.log(areArraysEqual([1, 1, 2], [1, 2, 2]));
console.log(areArraysEqual([1, 1, 1], [1, 1]));
console.log(areArraysEqual([1, 1], [1, 1]));
console.log(areArraysEqual([1, '1'], ['1', 1]));