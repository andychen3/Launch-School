// https://launchschool.com/exercises/ef1f43c3

function reverse(inputForReversal) {
  let results = '';
  let length = inputForReversal.length;

  if (Array.isArray(inputForReversal)) {
    results = [];
    for (let i = length - 1; i >= 0; i--) {
      results.push(inputForReversal[i]);
    }
  } else {
    for (let i = length - 1; i >= 0; i--) {
      results += inputForReversal[i];
    }
  }

  return results;
}

console.log(reverse('Hello'));
console.log(reverse('a'));
console.log(reverse([1, 2, 3, 4]));
console.log(reverse([]));
const array = [1, 2, 3]
console.log(reverse(array));
console.log(array);