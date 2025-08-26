// https://launchschool.com/exercises/e8d8cc55

function slice(array, begin, end) {
  if (begin > array.length) {
    begin = array.length;
  }

  if (end > array.length) {
    end = array.length;
  }

  let newArray = [];

  for (let i = begin; i < end; i++) {
    newArray.push(array[i]);
  }

  return newArray;
}

// console.log(slice([1, 2, 3], 1, 2));
// console.log(slice([1, 2, 3], 2, 0));
// console.log(slice([1, 2, 3], 5, 1));
// console.log(slice([1, 2, 3], 0, 5));

// const arr1 = [1, 2, 3];
// console.log(slice(arr1, 1, 3));
// console.log(arr1);

function splice(array, start, deleteCount, ...args) {
  if (start > array.length) {
    start = array.length;
  }

  if (deleteCount > array.length) {
    deleteCount = array.length - start;
  }

  let deletedElements = slice(array, start, start + deleteCount);
  let remainingArr = slice(array, start + deleteCount, array.length);

  array.length = start;
  array.push(...args);
  array.push(...remainingArr);

  return deletedElements;
}

// console.log(splice([1, 2, 3], 1, 2));
// console.log(splice([1, 2, 3], 1, 3));
// console.log(splice([1, 2, 3], 1, 0));
// console.log(splice([1, 2, 3], 0, 1));
// console.log(splice([1, 2, 3], 1, 0, 'a'));


const arr2 = [1, 2, 3];
console.log(splice(arr2, 1, 1, 'two'));             // [2]
console.log(arr2);                                  // [1, "two", 3]

const arr3 = [1, 2, 3];
console.log(splice(arr3, 1, 2, 'two', 'three'));
console.log(arr3);

const arr4 = [1, 2, 3];
console.log(splice(arr4, 1, 0));
console.log(splice(arr4, 1, 0, 'a'));
console.log(arr4);

const arr5 = [1, 2, 3];splice(arr5, 0, 0, 'a');
console.log(arr5);