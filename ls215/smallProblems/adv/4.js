'use strict';

/*
input: two sorted array
output: return one array that is sorted with both elements from each array
rules:
1. Cant use a sorting mechaninsm.
2. Not mutate the input arrays.

1 5 9.   2 6 8
x x      x x x

i = 2
j = 3

[1, 2, 5, 6, 8, 9]

9 and 8



1 2 5 6 8 9

1 1 3.  1, 2 2

i = 2
j = 1

[1, 1, 1]

3 and 1


Q:


D:
1. A result array

A:
1. Check if either input array is empty. If so return the other array.
2. create result array
3. create ptr that start at 0 to represent each array.
4. While ptr is less than length of input1 and ptr2 is less than length of input2
  5. if elemtn in input1 is less than or equal input 2
    6. add element to result.
    6a. increment ptr 1.
  7. else if input1 is greater to input 2.
    7a. add input2 element to result
    7b. increment ptr2.

8. Check if there are any more elements in input 1
  8a. add all the elements to the result array.

9a. check if htere are any more elements in put 2
  9b. add all the elements to result array

10. return result


*/


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


console.log(merge([1, 5, 9], [2, 6, 8]));      // [1, 2, 5, 6, 8, 9]
console.log(merge([1, 1, 3], [2, 2]));         // [1, 1, 2, 2, 3]
console.log(merge([], [1, 4, 5]));             // [1, 4, 5]
console.log(merge([1, 4, 5], []));             // [1, 4, 5]