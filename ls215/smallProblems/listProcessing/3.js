// https://launchschool.com/exercises/60b9ea01

function multiplyAllPairs(arr1, arr2) {
  let result = [];

  arr1.forEach(arr1Nums => {
    arr2.forEach(arr2Nums => {
      result.push(arr1Nums * arr2Nums);
    })
  })

  return result.sort((a, b) => a - b);
}

console.log(multiplyAllPairs([2, 4], [4, 3, 1, 2]));    // [2, 4, 4, 6, 8, 8, 12, 16]
