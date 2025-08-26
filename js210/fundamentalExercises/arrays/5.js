// https://launchschool.com/exercises/8e823938

function pop(arr) {
  if (arr.length === 0) {
    return undefined;
  }

  let lastElement = arr[arr.length - 1];
  arr.length = arr.length - 1;
  return lastElement;
}

// const array1 = [1, 2, 3];
// console.log(pop(array1));
// console.log(array1);
// console.log(pop([]));
// console.log(pop([1, 2, ['a', 'b', 'c']]));

function push(arr, ...args) {
  for (let i = 0; i < args.length; i++) {
    arr[arr.length] = args[i];
  }
  return arr.length;
}

const array2 = [1, 2, 3];
console.log(push(array2, 4, 5, 6));              // 6
console.log(array2);                // [1, 2, 3, 4, 5, 6]
console.log(push([1, 2], ['a', 'b']));          // 3
console.log(push([], 1));                       // 1
console.log(push([]));                          // 0