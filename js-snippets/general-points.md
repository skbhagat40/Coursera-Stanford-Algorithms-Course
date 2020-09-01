**Output of the following snippet is as follows -**
```
function print() {
  var x = "5";
  console.log(x + y);
  }
  var x = 3
  var y = 2
  print() // the output is 52 as expected.
  console.log(x+y) // the output is 5. poss. exp - var defined in function is block scoped, or related to main object / eval binding which changes outside to inside of the function.
```
