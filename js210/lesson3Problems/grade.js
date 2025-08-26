// https://launchschool.com/lessons/c26a6fcc/assignments/e25d11ee

const relSync = require('readline-sync');

const firstGrade = Number(relSync.question('Enter score 1: '));
const secondGrade = Number(relSync.question('Enter score 2: '));
const thirdGrade = Number(relSync.question('Enter score 3: '));

let average = Math.floor((firstGrade + secondGrade + thirdGrade) / 3);
let grade = null;

if (average >= 90) {
  grade = 'A';
} else if (70 <= average < 90) {
  grade = 'B';
} else if (50 <= average < 70) {
  grade = 'C';
} else {
  grade = 'F';
}

console.log(`Based on the average of your 3 scores your letter grade is "${grade}".`)