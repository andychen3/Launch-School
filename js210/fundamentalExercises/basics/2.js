// https://launchschool.com/exercises/33151343

const myBoolean = true;
const myString = 'hello';
const myArray = [];
const myOtherString = '';

if (myBoolean) {
  console.log('Hello');
} // Hello

if (!myString) {
  console.log('World');
} // Nothing

if (!!myArray) {
  console.log('World');
} // World

if (myOtherString || myArray) {
  console.log('!');
} // !

