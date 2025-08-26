// https://launchschool.com/exercises/17ebf9eb

const buyFruit = (array) => {
  let result = [];

  array.forEach((groceryList) => {
    for (let count = 0; count < groceryList[1]; count += 1) {
      result.push(groceryList[0]);
    }
  })

  return result;
};

// const buyFruit = (groceryList) => {
//   return groceryList.flatMap(([fruit, count]) => Array(count).fill(fruit));
// };


console.log(buyFruit([['apple', 3], ['orange', 1], ['banana', 2]]));
// returns ["apple", "apple", "apple", "orange", "banana", "banana"]