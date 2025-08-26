// https://launchschool.com/lessons/c26a6fcc/assignments/c778f491

function multiplesOfThreeAndFive(range) {
  for (let num = 1; num <= range; num++) {
    if (num % 15 === 0) {
      console.log(String(num) + '!');
    } else if (num % 3 === 0 || num % 5 === 0) {
      console.log(String(num));
    }
  }
}

multiplesOfThreeAndFive(100);