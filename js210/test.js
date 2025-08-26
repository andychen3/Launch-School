'use strict';

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


