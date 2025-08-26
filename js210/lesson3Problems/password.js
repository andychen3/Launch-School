// https://launchschool.com/lessons/c26a6fcc/assignments/9754deb9

const relSync = require('readline-sync');
let tries = 1;

while (true) {
  let userInput = relSync.question('What is the password: ');

  if (userInput === 'password') {
    console.log('You have successfully logged in.');
    break;
  }

  if (tries === 3) {
    console.log('You have been denied access.');
    break;
  }

  tries++
}


