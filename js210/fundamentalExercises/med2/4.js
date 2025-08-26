// https://launchschool.com/exercises/4b0d0727


function makeDoubler(caller) {
  return number => {
    console.log(`This function was called by ${caller}.`);
    return number + number;
  };
}


const doubler = makeDoubler('Victor');
let num = doubler(5);
console.log(num);