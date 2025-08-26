// https://launchschool.com/exercises/cfd1f1ac

function integerToString(number) {
  let array = [];

  do {
    let digit = number % 10;
    array.push(digit);
    number -= digit;
    number = Math.floor(number / 10);
  } while (number)

  return array.reverse().join("");
}



function signedIntegerToString(number) {
  if (number < 0) {
    return ('-' + integerToString(-number));
  } else if (number > 0) {
    return ('+' + integerToString(number));
  } else {
    return integerToString(number);
  }
}

console.log(signedIntegerToString(4321));      // "+4321"
console.log(signedIntegerToString(-123));      // "-123"
console.log(signedIntegerToString(0));         // "0"
console.log(signedIntegerToString(-0) === "-0");