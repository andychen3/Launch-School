// https://launchschool.com/exercises/26cebb22

/*

c = 89

[1, 5, 7, 11, 23, 45, 65, 89, 102
 0.  1 2.  3.  4.  5.  6. 7.   8

l = 0
h = 9

mid = Math.floor((l + h) / 2)

mid = 0 + 9 / 2 = 4





*/


'use strict';

function binarySearch(list, candidate) {
  let low = 0;
  let high = list.length;

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);

    if (list[mid] === candidate) {
      return mid;
    } else if (list[mid] < candidate) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return -1;
}



const yellowPages = ['Apple Store', 'Bags Galore', 'Bike Store', 'Donuts R Us', 'Eat a Lot', 'Good Food', 'Pasta Place', 'Pizzeria', 'Tiki Lounge', 'Zooper'];
console.log(binarySearch(yellowPages, 'Pizzeria'));                   // 7
console.log(binarySearch(yellowPages, 'Apple Store'));                // 0

console.log(binarySearch([1, 5, 7, 11, 23, 45, 65, 89, 102], 77));    // -1
console.log(binarySearch([1, 5, 7, 11, 23, 45, 65, 89, 102], 89));    // 7
console.log(binarySearch([1, 5, 7, 11, 23, 45, 65, 89, 102], 5));     // 1

console.log(binarySearch(['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler'], 'Peter'));  // -1
console.log(binarySearch(['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler'], 'Tyler'));  // 6