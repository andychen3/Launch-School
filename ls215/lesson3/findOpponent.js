'use strict';

/*
input: obj of different opponents, and position
output: person's position that is closet to active opponent
rules:
1. If two opponents are equidistant return opponent with higher position.
2. If object is empty return null
3. active position has a number and exterminated is null so we can skip null

Questions:
1. WHat happens if there are no opponents?
2. Will the position always be a positive integer?
3. Will the positions always be an object with at least one person? If not how to
handle? return null
4. How do you handle if a opponent's position is not a number like null? Do you
skip it?
5. Are there a limit to how many opponents there will be?
6.

h = 5
distance = 2;

[1, 5] 3

5 - 3 = 2

DS:
Array

Algo:
0. If positions is {} return null
1. Convert input into an array of values
1a. create variable to hold highestPos
1b. create variable with closet distance
2. Iterate through the array of values and do the absolute difference between pos and value
  2aa. if null skip iteration
  2a. if absolute distance is less than distance update distance with new value
  2b. update the highestpos if the distance is closer to input pos
    3b. if absolute distance === distance then update max of h
4. return h

*/


function findClosestOpponent(positions, position) {
  if (Object.keys(positions).length === 0) return null;

  let result = Object.values(positions).reduce((obj, pos) => {
    if (pos === null) return obj;

    let distance = Math.abs(position - pos);
    if (distance < obj.minDistance) {
      obj.minDistance = distance;
      obj.highestPos = pos;
    } else if (distance === obj.minDistance) {
      obj.highestPos = Math.max(obj.highestPos, pos);
    }

    return obj;
  }, {'highestPos': 0, 'minDistance': Infinity});
  return result.highestPos;
}

// function findClosestOpponent(positions, position) {
//   if (Object.keys(positions).length === 0) return null;

//   let arrayPos = Object.values(positions);
//   let highestPos = 0;
//   let minDistance = Infinity;

//   for (let pos of arrayPos) {
//     if (pos === null) continue;

//     let distance = Math.abs(pos - position);
//     if (distance < minDistance) {
//       minDistance = distance;
//       highestPos = pos;
//     } else if (distance === minDistance) {
//       highestPos = Math.max(pos, highestPos);
//     }
//   }

//   return highestPos;
// }

/*

h = 1
dis = 2

[1, 5] 3

distance = 15 - 10

*/


console.log(findClosestOpponent({}, 10) === null); // null

console.log(findClosestOpponent({
  "Opponent 1" : 1,
  "Opponent 2" : 15,
  "Opponent 3" : 37
}, 10) === 15); // 15

console.log(findClosestOpponent({
  "Opponent 1a" : 1,
  "Opponent 1b" : 5
}, 3) === 5); // 5

console.log(findClosestOpponent({
  "Opponent 1a" : 1,
  "Opponent 1b" : null
}, 3)); // 1

console.log(findClosestOpponent({
  "Opponent 1a" : 1, "Opponent 1b" : 5,
  "Opponent 1c" : 50, "Opponent 1d" : 100, "Opponent 1e" : null
}, 150)); // 100

// edge case



console.log(findClosestOpponent({
  "he" : 1,
  "them" : 15,
  "she" : 37
}, 10)); // 15

console.log(findClosestOpponent({
  "Opponent 1a" : null, "Opponent 1b" : 5, "Opponent 1c" : null,
  "Opponent 1d" : null, "Opponent 1e" : 200, "Opponent 1f" : 400
}, 300)); // 400