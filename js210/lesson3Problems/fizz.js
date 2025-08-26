// https://launchschool.com/lessons/c26a6fcc/assignments/3fdc2a52

function fizzbuzz() {
  for (let num = 1; num <= 100; num++) {
    if (num % 15 === 0) {
      console.log('FizzBuzz')
    } else if (num % 3 === 0) {
      console.log('Fizz');
    } else if (num % 5 === 0) {
      console.log('Buzz');
    }

    console.log(num);
  }
}

fizzbuzz();