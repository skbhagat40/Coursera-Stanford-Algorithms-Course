Some Example problems solved using stack.
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3464/
Max time to buy and sell stock.
Approach = Using stack to keep track of maximum price on the right.

Another possible way of solving this problem - 
_Kaden's Algo_  // based on the concept of local_max and global_max. possible example = max substring sum.
Other optimized solution is similar to dp based / kaden's algo, we remeber / update the min from the past and keep updating max_profit which can occur at any stage.
```
for price in prices:
  current_min = min(price, current_min)
  max_profit = max(max_profit, current_min - price)
```
**I think in general, in subarray, subsequence type problems, kaden's algo (dp/ memoizing past values) can be used to optimize the n2 complexity to n.

Another example using stack - finding 132 pattern.
stack to keep track for all the numbers , maximum numbers to the right so far, number in stack is s2 ( greatest one ). popped one is s2. s1 is the incoming element.

Sliding window maximum, using deque concept - https://github.com/skbhagat40/LeetCode-Challanges/blob/master/november/29.py
