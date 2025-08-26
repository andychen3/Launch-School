// https://launchschool.com/exercises/778fc8e7

// function rangeFunc(start, end) {
//   const range = [];

//   for (let element = start; element <= end; element++) {
//     range.push(element);
//   }

//   return range;
// }

// function range(end) {
//   return rangeFunc(0, end);
// }

// // Examples

// console.log(range(10, 20));
// console.log(range(5));

// function range(start, end) {
//   const range = [];

//   for (let element = start; element <= end; element++) {
//     range.push(element);
//   }

//   return range;
// }

// function range(end) {
//   return range(0, end);
// }

// // Examples

// console.log(range(10, 20));
// console.log(range(5));

function range(start, end) {
  if (arguments.length === 1) {
    end = start;
    start = 0;
  }

  const range = [];
  for (let element = start; element <= end; element++) {
    range.push(element);
  }

  return range;
}

// Examples

console.log(range(10, 20));
console.log(range(5));