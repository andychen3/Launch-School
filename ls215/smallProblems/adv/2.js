function transpose(array) {
  let result = [];

  for (let row = 0; row < array[0].length; row += 1) {
    let subarray = [];
    for (let col = 0; col < array.length; col += 1) {
      subarray.push(array[col][row]);
    }

    result.push(subarray);
  }

  return result;
}