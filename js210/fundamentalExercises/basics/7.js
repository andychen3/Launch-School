// https://launchschool.com/exercises/a6a29fea

function stringToInteger(string) {
  const numberMap = {"0": 0, "1": 1, "2": 2, "3": 3,
                    "4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9
  }
  let number = 0;
  for (let i = 0; i < string.length; i++){
    let charAtString = string[i];
    number += numberMap[charAtString] * (10**(string.length - i - 1));
  }

  return number;
}

console.log(stringToInteger('4321'));
console.log(stringToInteger('570'));