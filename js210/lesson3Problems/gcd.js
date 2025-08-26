// https://launchschool.com/lessons/c26a6fcc/assignments/ecedac0a

const gcd = function(operand1, operand2) {
  let greatestDivisor = 1;
  let greaterOperand = operand1 >= operand2 ? operand1 : operand2

  for (let divisor = 1; divisor <= greaterOperand; divisor++) {
    if ((operand1 % divisor === 0) && (operand2 % divisor === 0)) {
      greatestDivisor = divisor;
    }
  }

  return greatestDivisor;
};

console.log(gcd(12, 4));   // 4
console.log(gcd(15, 10));  // 5
console.log(gcd(9, 2));    // 1)