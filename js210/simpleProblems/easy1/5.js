// https://launchschool.com/exercises/cf7fce81?track=python

let relSync = require('readline-sync');
let integer = Number(relSync.question('Please enter an integer greater than 0: '));
let sumOrProduct = relSync.question('Enter "s" to compute the sum, or "p" to compute the product. ');

let arr = Array.from({ length: integer }, (_, i) => i + 1);

const product = arr.reduce((product, number) => product * number, 1);

const sum = arr.reduce((sum, number) => sum + number);

if (sumOrProduct === 's') {
  console.log(`The sum of the ingers between 1 and ${integer} is ${sum}.`);
} else if (sumOrProduct === 'p') {
  console.log(`The product of the ingers between 1 and ${integer} is ${product}.`);
}