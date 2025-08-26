// https://launchschool.com/exercises/9a7cb86f

function penultimate(string) {
  return string.split(' ').splice(-2)[0];
}

console.log(penultimate('last word'));                    // expected: "last"
console.log(penultimate('Launch School is great!'));      // expected: "is"

// The problem is that negative indexing does not go from the back.
// If will try to access a non-existent index.