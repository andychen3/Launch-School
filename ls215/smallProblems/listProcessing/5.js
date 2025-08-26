// https://launchschool.com/exercises/91427112

'use strict';

function leadingSubstrings(string) {
  return [...string].map((_, index) => string.slice(0, index + 1));
}

leadingSubstrings('abc');      // ["a", "ab", "abc"]
leadingSubstrings('a');        // ["a"]
leadingSubstrings('xyzzy');    // ["x", "xy", "xyz", "xyzz", "xyzzy"]