// https://launchschool.com/exercises/ae3a4c99

`It will still log 7. Because the function creates a copy of the a that is passed as
an argument into the function. When it performs a+= 10 it is incrementing the copy of that a.
And since 7 is a primitive value and primitive values are immutable it does not affect
the global variable a. The a in the function shadows the one outside so you can't access it.`