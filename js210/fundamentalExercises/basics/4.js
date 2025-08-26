// https://launchschool.com/exercises/67a51bac

// let myName = 'Bob';
// const saveName = myName;
// myName = 'Alice';
// console.log(myName, saveName);

// Alice Bob

const myName = 'Bob';
const saveName = myName;
myName.toUpperCase();
console.log(myName, saveName);

// Bob Bob because toUpper can't mutate a primitive value. It creates a new
// bob value and uppercase it. Since it was not reassigned. myName retained
// the original value.