// https://launchschool.com/exercises/c87f01cc

let i = 0;
while (i < 10) {
  if (i % 3 === 0) {
    console.log(i);
  } else {
    i += 1;
  }
}

// No because after it logs zero i never gets incremented that means it will be
// an infinite loop. To fix it you always increment i and you get rid of the else statement
