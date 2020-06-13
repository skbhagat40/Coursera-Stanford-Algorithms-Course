_HW questions - converting Fib To tail recursion and Time Complexity Analysis using Mathematics._

Recursion - A function calling itself. The idea is to break down a problem into smaller subproblems.

There are three important steps in recursion - 

1. Initialization Step
2. Termination Step / Base Condition. (The case for which answer is known.)
3. Recursive Calls (Breaking the problem into smaller subproblems)

Types of recursion - 1. Normal Recursion 2. Tail Recursion (the recursive calls are the last statement in the program.)

Each recursive call pushes into memory current state of the function.

Tail Recursion Has better space complexity as it doesn't store recursive stacks.(Compiler optimizes it as an iterative approach.)

_Related Concepts_ - Stack Unfolding

Example of recursion - 

```
def addNTimes(a, N):
    if N == 0:
        return 0
    return a + addNtimes(a, N-1)
```
Same Example written as Tail Recursion - 

```
def addNTimes(a,N,result):
    if N == 0:
        return result
    addNTimes(a,N-1,result + a)
```

Examples Using Recursion - 

1. Fibonacci O(2^N) Iterative O(N)
2. Fast Power O(logN)

Recursion can be optimized by using memoization.

Applications of Recursion - 

1. Compute all subsets. (Given an array of numbers(no duplicates), compute all subsets)

Approach 1 -  Bit Masking. (Using Binary Representation).

Approach 2 - Using Recursion

Intution - Each element in array has two choices either to be there in subset or not.
Based on the current choice we further have two choices for the element at next index, depending on the current subset.
Based on this approach, we can build a recursion tree. https://1drv.ms/u/s!AkicLUy5pNvNmFoAwVVz8P62FCJC

2. Compute all permutations. (Given an array of numbers(can have duplicates), compute all permutations)
   
Intution - Similar to build sets.
For first position we have N choices, for second N-1 and so on.
for each index (i.e. current positon) swap with remaining , build recursion tree (i.e. recursive calls after swapping. increment the current positon.)

Handling Repition - Keep a set, ignore recursive call if same element occuring twice at the current position.

*Tip* - It is better to write recursive conditions as mathematical functions.

f(x) = 1 x<=0
     = x + f(x-1) x >= 1