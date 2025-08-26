'use strict';

function mergeSort(array) {
  if (array.length === 1) {
    return array;
  }

  let mid = Math.floor(array.length / 2);
  let array1 = mergeSort(array.slice(0, mid));
  let array2 = mergeSort(array.slice(mid));

  return merge(array1, array2);
}

function merge(arr1, arr2) {
  if (arr1.length === 0) return arr2;
  if (arr2.length === 0) return arr1;

  let result = [];
  let ptr1 = 0;
  let ptr2 = 0;

  while (ptr1 < arr1.length && ptr2 < arr2.length) {
    if (arr1[ptr1] <= arr2[ptr2]) {
      result.push(arr1[ptr1]);
      ptr1 += 1;
    } else if (arr1[ptr1] > arr2[ptr2]) {
      result.push(arr2[ptr2]);
      ptr2 += 1;
    }
  }

  if (ptr1 < arr1.length) {
    result = result.concat(arr1.slice(ptr1,));
  }

  if (ptr2 < arr2.length) {
    result = result.concat(arr2.slice(ptr2,));
  }

  return result;
}


console.log(mergeSort([9, 5, 7, 1]));               // [1, 5, 7, 9]
console.log(mergeSort([5, 3]));                     // [3, 5]
console.log(mergeSort([6, 2, 7, 1, 4]));            // [1, 2, 4, 6, 7]
console.log(mergeSort([9, 2, 7, 6, 8, 5, 0, 1]));   // [0, 1, 2, 5, 6, 7, 8, 9]

console.log(mergeSort(['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']));
// ["Alice", "Bonnie", "Kim", "Pete", "Rachel", "Sue", "Tyler"]

console.log(mergeSort([7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46]));
// [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54]