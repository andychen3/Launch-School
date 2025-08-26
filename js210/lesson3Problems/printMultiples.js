// https://launchschool.com/lessons/c26a6fcc/assignments/4258ed28

const logMultiples = function(number) {
  for (let num = 100; num >= 0; num--) {
    if (num % number === 0 && num % 2 === 1) {
      console.log(num);
    }
  }
}

logMultiples(17);
logMultiples(21);