// https://launchschool.com/exercises/0d6451f1


function calculateBonus() {
  let args = Array.from(arguments);
  return args[1] ? args[0] / 2 : 0;
}

console.log(calculateBonus(2800, true));               // 1400
console.log(calculateBonus(1000, false));              // 0
console.log(calculateBonus(50000, true));              // 25000

// This works because I can access the arguments array and index into it.