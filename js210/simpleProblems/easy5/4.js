// https://launchschool.com/exercises/91f90abf

'use strict';

function centerOf(string) {
  let length = string.length;
  let mid = Math.floor(length / 2);

  if (length % 2 === 1) {
    return string[mid];
  } else {
    return string.slice(mid - 1, mid + 1);
  }
}

centerOf('I Love JavaScript'); // "a"
centerOf('Launch School');     // " "
centerOf('Launch');            // "un"
centerOf('Launchschool');      // "hs"
centerOf('x');                 // "x"