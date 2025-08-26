// https://launchschool.com/exercises/a887cdb7?track=python

function sum(number) {
  return String(number)
    .split('')
    .reduce(((total, num) =>  total + Number(num)), 0);
}

sum(23);           // 5
sum(496);          // 19
sum(123456789);    // 45