// https://launchschool.com/lessons/c26a6fcc/assignments/4981d6d8

function isPrime(number) {
  if (number <= 1) {
    return false;
  }

  for (let divisor = 2; divisor < Math.floor(Math.sqrt(number)) + 1; divisor++) {
    if (number % divisor === 0) {
      return false;
    }
  }
  return true;
}

// console.log(isPrime(5))

const checkGoldbach = function(number) {
  if ((number % 2 === 1 || number < 4)) {
    console.log(null);
    return;
  }

  for (let num = 2; num < Math.floor(number / 2) + 1; num++) {
    if (isPrime(num) && (isPrime(number - num))) {
      console.log(num, number - num);
    }
  }
};

// checkGoldbach(3);
// logs: null

// checkGoldbach(4);
// // logs: 2 2

// checkGoldbach(12);
// logs: 5 7

checkGoldbach(100);
// // logs:
// // 3 97
// // 11 89
// // 17 83
// // 29 71
// // 41 59
// // 47 53