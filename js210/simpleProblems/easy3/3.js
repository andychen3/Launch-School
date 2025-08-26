// https://launchschool.com/exercises/b60eaa7f

'use strict';

let relSync = require('readline-sync');
let age = Number(relSync.question('What is your age? '));
let retirementAge = Number(relSync.question('At what age would you like to retire? '));

const today = new Date();
let currentYear = today.getFullYear();
let retirementYear = retirementAge - age;

console.log(`It's ${currentYear}. You will retire in ${currentYear + retirementYear}.`);
console.log(`You have only ${retirementYear} years of work to go!`);
