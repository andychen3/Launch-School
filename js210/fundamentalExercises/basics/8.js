// https://launchschool.com/exercises/38861cc1


function stringToSignedInteger(string) {
  const numberMap = {"0": 0, "1": 1, "2": 2, "3": 3,
                    "4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9
  }
  let number = 0;
  let sign = false;

  for (let i = 0; i < string.length; i++){
    if (string[i] === '-') {
      sign = true;
      continue;
    } else if (string[i] === '+') {
      continue;
    }

    let charAtString = string[i];
    number += numberMap[charAtString] * (10**(string.length - i - 1));
  }
  if (sign) {
    number *= -1
  }

  console.log(number);
}

stringToSignedInteger('4321');      // 4321
stringToSignedInteger('-570');      // -570
stringToSignedInteger('+100');      // 100