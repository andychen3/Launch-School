// https://launchschool.com/exercises/6948ddb4

const triangle = (n) => {
  for (let stars = 1; stars <= n; stars += 1) {
    console.log(`${' '.repeat(n - stars)}${'*'.repeat(stars)}`);
  }
};

triangle(5);

//     *
//    **
//   ***
//  ****
// *****

triangle(9);

//         *
//        **
//       ***
//      ****
//     *****
//    ******
//   *******
//  ********
// *********