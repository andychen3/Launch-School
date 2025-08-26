'use strict';

/*
input:
output: 1, -1, 0 To represent equality
rules:
1. if version 1 > version 2 return 1
2. if version 1 < version 2 return -1
3. if version 1 === version2 return 0.
4. If number contains other than digits and . return null

Questions:
1. Will i ever get an empty input and if so do i return null?
2. Is the format a string? String.
3. Will there ever be negative numbers?



DS:
Array when we split

Algo:
1. Check if the version numbers are valid return null if not.
2. Split versions into an array based on period
3. Iterate through both arrays
  3a. if one of the versions is greater return 1 or -1
  3b. if they don't have the same length
    ii. Continue iterating on the one that still has elements
    ii. If the element is not 0 then return 1
4. if any of the other conidtions don't get triggerd return 0

*/
function validateInput(version1, version2) {
  let match1 = version1.match(/[^\d.]/g);
  let match2 = version2.match(/[^\d.]/g);
  if (match1 || match2) return null;

  let arr1 = version1.split('.');
  let arr2 = version2.split('.');

  if (arr1.includes('') || arr2.includes('')) return null;
}


function compareVersions(version1, version2) {
  let input = validateInput(version1, version2);
  if (input === null) return null;
  let arr1 = version1.split('.').map(Number);
  let arr2 = version2.split('.').map(Number);
  let arr1Index = 0;
  let arr2Index = 0;

  while (arr1Index < arr1.length && arr2Index < arr2.length) {
    if (arr1[arr1Index] > arr2[arr2Index]) return 1;
    if (arr1[arr1Index] < arr2[arr2Index]) return -1;
    arr1Index += 1;
    arr2Index += 1;
  }


  while (arr1Index < arr1.length) {
    if (arr1[arr1Index] !== 0) return 1;
    arr1Index += 1;
  }

  while (arr2Index < arr2.length) {
    if (arr2[arr2Index] !== 0) return -1;
    arr2Index += 1;
  }

  return 0;
}

/* Refactored
function compareVersions(version1, version2) {
  let regex = /^\d+(\.\d+)*$/;

  if (!regex.test(version1) || !regex.test(version2)) return null;

  let arr1 = version1.split('.').map(Number);
  let arr2 = version2.split('.').map(Number);
  let maxIndex = Math.max(arr1.length, arr2.length);

  for (let index = 0; index < maxIndex; index += 1) {
    let validArr1 = arr1[index] || 0;
    let validArr2 = arr2[index] || 0;

    if (validArr1 > validArr2) return 1;
    if (validArr1 < validArr2) return -1;
  }

  return 0;
}


*/

console.log(compareVersions('1', '1'));            // 0
console.log(compareVersions('1.1', '1.0'));        // 1
console.log(compareVersions('2.3.4', '2.3.5'));    // -1
console.log(compareVersions('1.a', '1'));          // null
console.log(compareVersions('.1', '1'));           // null
console.log(compareVersions('1.', '2'));           // null
console.log(compareVersions('1..0', '2.0'));       // null
console.log(compareVersions('1.0', '1.0.0'));      // 0
console.log(compareVersions('1.0.0', '1.1'));      // -1
console.log(compareVersions('1.0', '1.0.5'));      // -1 (this doesn't work yet)

// console.log(compareVersions('0.1', '1') === -1);

// console.log(compareVersions('1.0', '1') === 0);

// console.log(compareVersions('1.0', '1.1') === -1);


// console.log(compareVersions('1.2', '1.1') === 1);


// console.log(compareVersions('1.2', '1.2.0.0') === 0);

// console.log(compareVersions('1.2.0.0', '1.18.2') === -1);


// console.log(compareVersions('13.37', '1.18.2') === 1);


// // Edge cases

// console.log(compareVersions('A13.37', '1.18.2') === null);


// console.log(compareVersions('.1', '1.18.2') === null);


// console.log(compareVersions('', '1.18.2') === null);


// console.log(compareVersions('123', '1?23') === null);

// console.log(compareVersions('AS', 'cat') === null);


// console.log(compareVersions('-123', '52') === null);


// console.log(compareVersions('123', '-52') === null);


// console.log(compareVersions('123..0', '52') === null);


