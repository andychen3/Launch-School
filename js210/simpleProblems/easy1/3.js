// https://launchschool.com/exercises/10323cf5

const relSync = require('readline-sync');
let lengthInput = Number(relSync.question('Enter the length of the room in meters: '));
let widthInput = Number(relSync.question('Enter the width of the room in meters: '));

const METER_TO_FEET_CONVERSION = 10.7639;
const areaInMeters = lengthInput * widthInput;
const areaInFeet = areaInMeters * METER_TO_FEET_CONVERSION;

console.log(`The area of the room is ${areaInMeters} square_meters (${areaInFeet.toFixed(2)} square feet).`);