// https://launchschool.com/exercises/9d6492cd

let relSync = require('readline-sync');
let billAmount = Number(relSync.question('What is the bill? '));
let tipAmount = Number(relSync.question('What is the tip percentage? '));

let calculatedTip = billAmount * (tipAmount / 100);
let total = calculatedTip + billAmount;

console.log(`The tip is $${calculatedTip.toFixed(2)}`);
console.log(`The total is $${total.toFixed(2)}`);
