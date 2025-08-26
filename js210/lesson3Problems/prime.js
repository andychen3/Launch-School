// https://launchschool.com/lessons/c26a6fcc/assignments/7889d322

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

console.log(isPrime(1));   // false
console.log(isPrime(2));   // true
console.log(isPrime(3));   // true
console.log(isPrime(43));  // true
console.log(isPrime(55));  // false
console.log(isPrime(0));   // false
console.log(isPrime(9));   // false