// https://launchschool.com/lessons/c26a6fcc/assignments/a31baf27

function logOddNumbers(number) {
  for (let num = 1; num <= number; num++) {
    if (num % 2 === 0) {
      continue;
    }
    console.log(num);
  }
}

logOddNumbers(19);