// https://launchschool.com/exercises/a5099dc9

function concat(...args) {
  return [...args].flat()
}

// function concat(array1, ...secondArgument) {
//   let newArray = [...array1];

//   for (let elements of secondArgument) {
//     if (Array.isArray(elements)) {
//       newArray.push(...elements)
//     } else {
//       newArray.push(elements);
//     }
//   }

//   return newArray;
// }

console.log(concat([1, 2, 3], [4, 5, 6], [7, 8, 9]));
console.log(concat([1, 2], 'a', ['one', 'two']));
console.log(concat([1, 2], ['three'], 4));