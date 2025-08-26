// https://launchschool.com/exercises/85e333ca

'use strict';

let relSync = require('readline-sync');
let noun = relSync.question('Enter a noun: ');
let verb = relSync.question('Enter a verb: ');
let adjective = relSync.question('Enter an adjective: ');
let adverb = relSync.question('Enter an adverb: ');

console.log(`Do you ${verb} your ${adjective} ${noun} ${adverb}? That's hilarious!`);
