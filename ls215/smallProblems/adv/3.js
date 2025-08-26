'use strict';

/*
input: mxn matrix
output: return new matrix rotated 90 degrees
rules:
1. Do not mutate input.

  0 1 2
0 1 5 8
1 4 7 2
2 3 9 6



  0 1 2
0 3 4 1
1 9 7 5
2 6 2 8


1 5 8
4 7 2
3 9 6

1 4 3
5 7 9
8 2 6

3 4 1
9 7 5
6 2 8

3 4 1
9 7 5
6 2 8



0,0 -> 0, 2
0,1 -> 1, 2
0,2 -> 2, 2

1,0 -> 0,1
1,1 -> 1,1
1,2 -> 2,1

2,0 -> 0,0
2,1 -> 1,0
2,2 -> 2,0

row = 2
col = 4

3 7 4 2
5 1 0 8

5 3
1 7
0 4
8 2

row ->4
col -> 2

row = 2
col = 1

[3, 5]
[7, 1]
[4, 0]

matrix[col][row]
matrix[1][2]


Q:
1.

DS:

A:
1. create result = []

Transpose
2. Itereate 0 to row to col length
3. create subarray
4. iterate 0 to col to row length
5. access matrix[col][row] and push to subarray
6. push to result


Reverse
1. iterate through result
2. reverse each row
3. return result

*/



const matrix1 = [
  [1, 5, 8],
  [4, 7, 2],
  [3, 9, 6],
];

const matrix2 = [
  [3, 7, 4, 2],
  [5, 1, 0, 8],
];

function rotate90(matrix) {
  return reverseArray(transpose(matrix));
}

function transpose(array) {
  let result = [];

  for (let row = 0; row < array[0].length; row += 1) {
    let subarray = [];
    for (let col = 0; col < array.length; col += 1) {
      subarray.push(array[col][row]);
    }

    result.push(subarray);
  }

  return result;
}

function reverseArray(array){
  return array.map(subarray => subarray.reverse());
}

const newMatrix1 = rotate90(matrix1);
const newMatrix2 = rotate90(matrix2);
const newMatrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))));

console.log(newMatrix1);      // [[3, 4, 1], [9, 7, 5], [6, 2, 8]]
console.log(newMatrix2);      // [[5, 3], [1, 7], [0, 4], [8, 2]]
console.log(newMatrix3);      // `matrix2` --> [[3, 7, 4, 2], [5, 1, 0, 8]]