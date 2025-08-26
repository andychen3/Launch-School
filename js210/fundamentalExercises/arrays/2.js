// https://launchschool.com/exercises/08ff4ec8

// let myArray = [1, 2, 3, 4];
// const myOtherArray = myArray.slice();

// myArray.pop();
// console.log(myOtherArray);

// myArray = [1, 2];
// console.log(myOtherArray);


let myArray = [1, 2, 3, 4];
const myOtherArray = myArray.map(elem => elem);

myArray.pop();
console.log(myOtherArray);

myArray = [1, 2];
console.log(myOtherArray);

// CAn use spread or array.from()