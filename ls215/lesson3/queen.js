'use strict';

/*
input: string represntation of board
output: return true or false depending on whether or not queen can attack each other
rules:
1. Queen can attack pieces on same row, column, diagonal.
2. Positison on board equate to coordinate number

Question:
1. Will input ever be null? If so what will i return?
2. Will there ever be more then one white queen or black queen? If so what happens there
3. Will there ever be one missing queen?
4. What does the string board look like?
'---W--' + '---b--'?
'---W--\n' + '---B--\n'?
5. How big is the board is it always an 8x8 board?



  0 1 2 3 4 5 6 7
0 _ W _ _ _ _ _ _
1 _ _ _ _ _ _ _ _
2 _ _ _ _ _ _ _ _
3 _ _ _ _ _ _ _ _
4 _ _ _ _ _ _ _ _
5 _ _ _ _ _ _ _ _
6 _ _ _ _ _ _ _ B
7 _ _ _ _ _ _ _ _

(2,3) (5, 6) -> abs(row1 -row2, col1 - col2) = 3, 3

(0, 1) (6,7)

DS:
Array -> each of elements will equal an index
Map -> To have the pieces of Queens

Algo:
1. Split the board so i can have an array
2a. Create hashmap to keep track of coordinates of W and B queen.
2. Iterate through the board.
  2a. If W queen found add to map. If duplicate automatically return undefined
  2b. If B queen found add to map. If duplicate automtically return undefined.
  2c. Check if the size of map is 2 if not return undefined
3. If both exist then find if they attack each other (canAttack)
  3a. Pass in coordinates
  4. Find out same row (2,3) -> (2, 5)
  5. Find out same column (4,6) -> (1, 6)
  6. Find out same diagonal (abs of both row and col are the same number)





*/

function queenAttack(board) {
  let playableBoard = board.split('\n');
  let queenMap = validateBoard(playableBoard);

  if (queenMap === undefined) return undefined;

  return canAttack(queenMap.get('W'), queenMap.get('B'));
}

function validateBoard(playableBoard) {
  let queenMap = new Map();

  for (let i = 0; i < playableBoard.length; i += 1) {
    for (let j = 0; j < playableBoard[0].length; j += 1) {
      if (playableBoard[i][j] === 'W') {
        if (queenMap.has('W')) {
          return undefined;
        }

        queenMap.set('W', [i, j]);
      } else if (playableBoard[i][j] === 'B') {
        if (queenMap.has('B')) {
          return undefined;
        }

        queenMap.set('B', [i, j]);
      }
    }
  }

  if (queenMap.size !== 2) {
    return undefined;
  }

  return queenMap;
}


function canAttack(q1, q2) {
  if (q1[0] === q2[0]) {
    return true;
  } else if (q1[1] === q2[1]) {
    return true;
  } else if (Math.abs(q1[0] - q2[0]) === Math.abs(q1[1] - q2[1])) {
    return true;
  }

  return false;
}

/* Refactored
function queenAttack(board) {
  let playableBoard = board.split('\n');
  let queenMap = validateBoard(playableBoard);

  if (queenMap.size !== 2) return undefined;

  return canAttack(queenMap.get('W'), queenMap.get('B'));
}

function validateBoard(playableBoard) {
  let queenMap = new Map();

  playableBoard.forEach((row, rowIndex) => {
    if (row.includes('W') && queenMap.has('W')) return undefined;
    if (row.includes('W') && !queenMap.has('W')) queenMap.set('W', [rowIndex, row.indexOf('W')]);
    if (row.includes('B') && queenMap.has('B')) return undefined;
    if (row.includes('B') && !queenMap.has('B')) queenMap.set('B', [rowIndex, row.indexOf('B')]);
  });

  return queenMap;
}


function canAttack(q1, q2) {
  if (q1[0] === q2[0]) return true;
  if (q1[1] === q2[1]) return true;
  if (Math.abs(q1[0] - q2[0]) === Math.abs(q1[1] - q2[1])) return true;

  return false;
}




*/

// Same Row
console.log(queenAttack('________\n' +
                        '___W__B_\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n') === true);

// Same Row
console.log(queenAttack('W______B\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n') === true);



// Same Column
console.log(queenAttack('________\n' +
                        '________\n' +
                        '________\n' +
                        '_W______\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '_B______\n') === true);

                        // Same Column
console.log(queenAttack('_______W\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '_______B\n') === true);


// Same Diagonal
console.log(queenAttack('_______W\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        'B_______\n') === true);

                        // Same Diagonal
console.log(queenAttack('___W____\n' +
                        '________\n' +
                        '________\n' +
                        '______B_\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n') === true);

// False cases
console.log(queenAttack('___W____\n' +
                        '________\n' +
                        '________\n' +
                        '_____B__\n' +
                        '________\n' +
                        '________\n' +
                        '________\n' +
                        '________\n') === false);


//Edge case
// Missing queens
console.log(queenAttack("__W_____\n" +
                        "________\n" +
                        "________\n" +
                        "________\n" +
                        "________\n" +
                        "________\n" +
                        "________\n" +
                        "________\n") === undefined);


console.log(queenAttack("________\n" +
                        "________\n" +
                        "________\n" +
                        "________\n" +
                        "_B______\n" +
                        "________\n" +
                        "________\n" +
                        "________\n") === undefined);

console.log(queenAttack("________\n" +
                        "________\n" +
                        "____B___\n" +
                        "________\n" +
                        "_B______\n" +
                        "________\n" +
                        "________\n" +
                        "________\n") === undefined);

console.log(queenAttack("________\n" +
                        "_____W__\n" +
                        "________\n" +
                        "________\n" +
                        "________\n" +
                        "_W______\n" +
                        "________\n" +
                        "________\n") === undefined);


//Empty Board
console.log(queenAttack("________\n" +
                        "________\n" +
                        "________\n" +
                        "________\n" +
                        "________\n" +
                        "________\n" +
                        "________\n" +
                        "________\n") === undefined);


