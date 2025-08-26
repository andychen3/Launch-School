// https://launchschool.com/exercises/9d44cd7d

function oddities(array) {
  const oddElements = [];

  for (let i = 0; i < array.length; i += 2) {
    oddElements.push(array[i]);
  }

  return oddElements;
}

oddities([2, 3, 4, 5, 6]) === [2, 4, 6];      // false
oddities(['abc', 'def']) === ['abc'];         // false

// Arrays are only equal if they reference the same array. in this function
// We are creating a new array. OddElements does not reference the same array as
// the one being compared to on the right. That is why we get false.
// In javascript it doesnt matter if an array has the same elements it is only true
// When they both reference teh same array.