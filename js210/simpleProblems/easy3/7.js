// https://launchschool.com/exercises/f3a0ccc0

// function runningTotal(array) {
//   let result = [];
//   let total = 0;

//   array.forEach(num => {
//     total += num;
//     result.push(total);
//   });

//   return result;
// }

function runningTotal(array) {
  let total = 0;

  return array.map(num => {
    total += num;
    return total;
  });
}

runningTotal([2, 5, 13]);             // [2, 7, 20]
runningTotal([14, 11, 7, 15, 20]);    // [14, 25, 32, 47, 67]
runningTotal([3]);                    // [3]
runningTotal([]);                     // []