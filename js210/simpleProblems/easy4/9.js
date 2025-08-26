// https://launchschool.com/exercises/2b9f8b47

'use strict';

// function countOccurrences(listOfVehicles) {
//   let objMap = {};

//   for (let vehicle of listOfVehicles) {
//     objMap[vehicle] ? objMap[vehicle] += 1 : objMap[vehicle] = 1;
//   }

//   for (let [key, value] of Object.entries(objMap)) {
//     console.log(`${key} => ${value}`);
//   }
// }

function countOccurrences(listOfVehicles) {
  let vehicleMap = new Map();

  for (let vehicle of listOfVehicles) {
    vehicleMap.set(vehicle, (vehicleMap.get(vehicle) ?? 0) + 1);
  }

  vehicleMap.forEach((value, key) => console.log(`${key} => ${value}`));
}


const vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
                'motorcycle', 'suv', 'motorcycle', 'car', 'truck'];

countOccurrences(vehicles);

// console output
// car => 4
// truck => 3
// SUV => 1
// motorcycle => 2
// suv => 1