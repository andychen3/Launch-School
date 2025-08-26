// https://launchschool.com/exercises/df62e4d1

let relSync = require("readline-sync");
let integerOne = Number(relSync.question("==> Enter the first number: \n"));
let integerTwo = Number(relSync.question("==> Enter the second number: \n"));

console.log(`==> ${integerOne} + ${integerTwo} = ${integerOne + integerTwo}`)
console.log(`==> ${integerOne} - ${integerTwo} = ${integerOne - integerTwo}`)
console.log(`==> ${integerOne} * ${integerTwo} = ${integerOne * integerTwo}`)
console.log(`==> ${integerOne} / ${integerTwo} = ${Math.floor(integerOne / integerTwo)}`)
console.log(`==> ${integerOne} % ${integerTwo} = ${integerOne % integerTwo}`)
console.log(`==> ${integerOne} ** ${integerTwo} = ${integerOne ** integerTwo}`)