// https://launchschool.com/exercises/1be5b58c

function logInBox(string) {
  let length = string.length;
  let outsideBorder = `+${'-'.repeat(length + 2)}+`;

  console.log(`${outsideBorder}`);
  console.log(`| ${' '.repeat(length)} |`);
  console.log(`| ${string} |`);
  console.log(`| ${' '.repeat(length)} |`);
  console.log(`${outsideBorder}`);
}

logInBox('To boldly go where no one has gone before.');