// https://launchschool.com/exercises/93e3185d

// function shift(arr) {
//   if (arr.length === 0) {
//     return undefined;
//   }

//   let firstElement = arr[0];

//   for (let i = 1; i < arr.length; i++) {
//     arr[i - 1] = arr[i];
//   }

//   arr.length = arr.length - 1;

//   return firstElement;
// }

// where to insert / how many to remove / what item

function shift(arr) {
  let result;

  if (arr.length !== 0) {
    result = arr.splice(0, 1).pop()
  }

  return result;
}

// console.log(shift([1, 2, 3]));
// console.log(shift([]));
// console.log(shift([[1, 2, 3], 4, 5]));

// function unshift(arr, ...args) {
//   arr.length = arr.length + args.length;
//   let argLength = args.length - 1;

//   for (let i = arr.length - 1; i >= 0; i--) {
//     if (i === argLength) {
//       arr[i] = args[argLength];
//       argLength -= 1;
//     } else {
//       arr[i] = arr[i - 1];
//     }
//   }

//   return arr.length;
// }

function unshift(arr, ...args) {
  for (let i = 0; i < args.length; i++) {
    arr.splice(i, 0, args[i]);
  }

  return arr.length;
}

// console.log(unshift([1, 2, 3], 5, 6));
// console.log(unshift([1, 2, 3]));
// console.log(unshift([4, 5], [1, 2, 3]));


const testArray = [1, 2, 3];
console.log(shift(testArray));
console.log(testArray);
console.log(unshift(testArray, 5));
console.log(testArray);