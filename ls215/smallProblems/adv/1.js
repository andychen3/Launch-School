'use strict';

/*
input:  2D matrix
output: 2x matrix but transposed
rules:
1. Do not modify original matrix

  0 1 2
0 1 5 8
1 4 7 2
2 3 9 6

  0 1 2
0 1 4 3
1 5 7 9
2 8 2 6

0, 1

1. 0

0, 2
2, 0

1, 0
0, 1

0 -> 2
i + 1 -> 2

i = 1
j = 1

1, 2


Q:

DS:
1. Nested array

A:
1. Make a new copy of the matrix
2. Iterate from 0 to length of matrix -> row
  3. iterate from i to end of matrix -> col
    4. switch matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
5. return new copy transposed matrix



*/

const matrix = [
  [1, 5, 8],
  [4, 7, 2],
  [3, 9, 6]
];

function transpose(matrix) {
  let copy = matrix.map(row => row.slice());

  for (let row = 0; row < copy.length; row += 1) {
    for (let col = row; col < copy.length; col += 1) {
      [copy[row][col], copy[col][row]] = [copy[col][row], copy[row][col]];
    }
  }

  return copy;
}

const newMatrix = transpose(matrix);

console.log(newMatrix);      // [[1, 4, 3], [5, 7, 9], [8, 2, 6]]
console.log(matrix);         // [[1, 5, 8], [4, 7, 2], [3, 9, 6]]