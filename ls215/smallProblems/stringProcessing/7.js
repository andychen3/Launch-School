https://launchschool.com/exercises/96764a36

'use strict';

function staggeredCase(string) {
  let currIndex = 0;
  let newString = '';

  for (let char of string) {
    if (/[a-zA-Z]/.test(char) === true) {
      if (currIndex % 2 === 0) {
        newString += char.toUpperCase();
      } else {
        newString += char.toLowerCase();
      }

      currIndex += 1;
    } else {
      newString += char;
    }
  }

  return newString;
}

const tests = [
  { input: 'I Love Launch School!', expected: 'I lOvE lAuNcH sChOoL!' },
  { input: 'ALL CAPS', expected: 'AlL cApS' },
  { input: 'ignore 77 the 444 numbers', expected: 'IgNoRe 77 ThE 444 nUmBeRs' },
  {
    input: 'ignore 777 the 444 numbers',
    expected: 'IgNoRe 777 ThE 444 nUmBeRs',
  },
  { input: '', expected: '' },
  { input: 'a', expected: 'A' },
  { input: '1', expected: '1' },
  { input: '1aB', expected: '1Ab' },
  { input: 'ab', expected: 'Ab' },
  { input: 'aB', expected: 'Ab' },
  { input: 'a1', expected: 'A1' },
  { input: 'a1B', expected: 'A1b' },
  { input: 'a11B', expected: 'A11b' },
  { input: 'a12B', expected: 'A12b' },
  { input: 'a111B', expected: 'A111b' },
  { input: 'A1B', expected: 'A1b' },
  { input: 'a!a', expected: 'A!a' },
  { input: 'ab!ab', expected: 'Ab!Ab' },
  { input: 'ab!!ab', expected: 'Ab!!Ab' },
  { input: 'ab!!!ab', expected: 'Ab!!!Ab' },
  { input: 'ab!a!!ab', expected: 'Ab!A!!aB' },
];

function runTests(tests, fn, verbose = false) {
  let allPassed = true;

  tests.forEach((test) => {
    let passed;
    let output;

    try {
      output = fn(test.input);
      passed = output === test.expected;
    } catch (e) {
      output = e;
    }

    if (!passed) allPassed = false;

    console.log(passed ? 'pass' : 'FAIL');
    if (!passed || verbose) {
      console.log(`Input: ${test.input}`);
      console.log(`Output:`);
      console.dir(output);
      console.log(`Expected:`);
      console.dir(test.expected);
    }
  });

  console.log(allPassed ? 'All tests passed' : 'One or more tests failed.');
}

runTests(tests, staggeredCase);

// console.log(staggeredCase('I Love Launch School!'));        // "I lOvE lAuNcH sChOoL!"
// console.log(staggeredCase('ALL CAPS'));                     // "AlL cApS"
// console.log(staggeredCase('ignore 77 the 444 numbers'));    // "IgNoRe 77 ThE 444 nUmBeRs"