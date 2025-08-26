// https://launchschool.com/exercises/d543b302

// 1 and some other number
// if they are multiples of 3 or 5.

function multisum(num) {
  return Array.from({ length: num }, (_, index) => index + 1)
              .reduce((accumulator, currentNumber) => {
                if (currentNumber % 3 === 0 || currentNumber % 5 === 0) {
                  accumulator += currentNumber;
                }

                return accumulator;
              }, 0);
}

multisum(3);       // 3
multisum(5);       // 8
multisum(10);      // 33
multisum(1000);    // 234168