// https://launchschool.com/exercises/8c20053b

` it will log hello world! to the console. because in javascript there are
two execution phases and in the creation phase the interpreter identifies all the identifiers
such as variables, and function definition. so when logValue() is called it already has the
function defined. This is hoisting.`

var logValue = 'foo';

function logValue() {
  console.log('Hello, world!');
}

console.log(typeof logValue);