// https://launchschool.com/exercises/e9aa7157

'use strict';

/*
input: n -> reptitions
output: -> array of lights taht are on.
rules:
1. N represents the number of passes
2. It also represents the array of numbers

1 2 3 4 5 -> 1
1.  3.  5 -> 2  [ 2 and 4 are off]
1       5 -> 3. [ 2 3 4 are off]
1.    4 5 -> 4  [2 3 are off]
1.    4.  -> 5. [ 2 3 5 are off]

1 2 3 4 5 6 -> 1
1.  3.  5   -> 2  [ 2 and 4 are off]
1       5 6 -> 3. [ 2 3 4 are off]
1.    4 5 6 -> 4  [2 3 are off]
1.    4.  6 -> 5. [ 2 3 5 are off]
1.    4.   -> 6. [ 2 3 5 are off]

100

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Q's
1. Would n ever be 0 or negative? If so what do i provide?
2.


DS:
array to hold result



Algo:
1. Create result array
2. While num is less than n
3. We square num and check if it is less than n. if so add to result
4. increment num by 1
5. return result


*/


// function lightsOn(switches) {
//   let result = [];
//   let numSwitch = 1;

//   while (numSwitch * numSwitch <= switches) {
//     result.push(numSwitch * numSwitch);
//     numSwitch += 1;
//   }

//   return result;
// }

function lightsOn(switches) {
  return Array.from({length: Math.floor(Math.sqrt(switches))}, (_, i) => (i + 1) ** 2);
}

console.log(lightsOn(5));        // [1, 4]
// Detailed result of each round for `5` lights
// Round 1: all lights are on
// Round 2: lights 2 and 4 are now off;     1, 3, and 5 are on
// Round 3: lights 2, 3, and 4 are now off; 1 and 5 are on
// Round 4: lights 2 and 3 are now off;     1, 4, and 5 are on
// Round 5: lights 2, 3, and 5 are now off; 1 and 4 are on

console.log(lightsOn(25)); // [1, 4, 9, 16, 25]

console.log(lightsOn(25)); // [1, 4, 9, 16, 25]


console.log(lightsOn(100));      // [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]