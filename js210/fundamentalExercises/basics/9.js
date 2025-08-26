// https://launchschool.com/exercises/4a1cd983

function integerToString(number) {
  let array = [];

  do {
    digit = number % 10;
    array.push(digit);
    number -= digit;
    number = Math.floor(number / 10);
  } while (number)

  return array.reverse().join("");
}

console.log(integerToString(4321));      // "4321"
console.log(integerToString(0));         // "0"
console.log(integerToString(5000));      // "5000"