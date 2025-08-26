// https://launchschool.com/exercises/70e15061

const myArray = [5, 5];
myArray[-1] = 5;
myArray[-2] = 5;

function average(array) {
  let sum = 0;

  for (let i = -2; i < array.length; i += 1) {
    console.log(array[i]);
    sum += array[i];
  }

  return sum / array.length;
}

console.log(average(myArray));

// No because by trying to add arrays with negative indexes it doesn't get counted
// in the for loop.