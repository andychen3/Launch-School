// https://launchschool.com/exercises/d4132bc9

// function interleave(arr1, arr2) {
//   let result = [];

//   arr1.forEach((element, index) => result.push(...[element, arr2[index]]));
//   return result;
// }

function interleave(arr1, arr2) {
  return arr1.flatMap((element, index) => [element, arr2[index]]);
}


console.log(interleave([1, 2, 3], ['a', 'b', 'c']));