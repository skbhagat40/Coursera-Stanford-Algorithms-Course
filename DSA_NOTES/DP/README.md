0/1 Knapsack Problem, in case of large weights. We optimze for weight, i.e. minimize it for given value and number of items to pick.
The dp based solution was
initalize to float('inf').
dp[0] = 0.
now, we iterate over the array from the last, so as to optimize for the space complexity. Element of choice, either to pick an element or not pick.
so, If we follow the following code
```
for i in range(n):
   for val in range(mxval,A[i]-1,-1):
        dp[val] = min(dp[val], B[i] + dp[val-A[i]])
```
we, have all other items as inf, just dp[1] as B[1]. That means that if we are picking only one item, we will just pick the first, item and now we build on that
solution.

```
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)
        mxval = 50 * n
        dp = [0] * (mxval+1)
        for i in range(mxval+1):
            dp[i] = 1e9
        dp[0] = 0

        for i in range(n):
            for val in range(mxval,A[i]-1,-1):
                dp[val] = min(dp[val], B[i] + dp[val-A[i]])
                
        ans = 0
        for val in range(mxval,-1,-1):
            if(dp[val] <= C):
                ans = val
                break
        return ans
```

My accepted solution - 
```
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    # def solve(self, A, B, C):
    def solve(self, A, B, C):
        maxval = 50*len(A)
        prev_row = [float('inf')] * (maxval + 1)
        prev_row[0] = 0
        for i in range(len(A)):
            curr_row = [float('inf')] * (maxval + 1)
            for j in range(maxval):
                curr_row[j] = min(prev_row[j], B[i] + prev_row[j - A[i]])
            prev_row = curr_row[:]
        ans = 0
        for i in range(maxval,-1,-1):
            if curr_row[i] <= C:
               ans = max(ans, i) 
               break
        return ans
```

_let's see , where my approach went wrong,

Initially I thought that for the first row, everything is possible , but in reality only the starting item is possible.

Problem - Given an array of capacites of friends, array of filling capacities of dish, and cost of each dish, we need to minimize the overall cost such that,every person, eats item == filing capacity.

Approach - Use DP. Possiblity, eats a dish , doesn't eats it, eats it twice. Goal of dp => to minimize the cost.
Solution - 
```
import sys
sys.setrecursionlimit(100000)
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
	def solve(self, A, B, C):
	    cache = {}
	    def dp(idx, cap):
	        if idx < 0:
	            return 0, cap
	        if cap <= 0:
	            return 0, cap
	        res = cache.get((idx, cap), None)
	        if res is not None:
	            return res
	        p_cost, p_cap = dp(idx-1, cap)
	        curr_cost, curr_cap = dp(idx, cap-B[idx]) # can eat a dish twice, similar to regex matching dp problem.
	        curr_cost += C[idx]
	        if curr_cap == 0 and p_cap ==0:
	            if curr_cost < p_cost:
	                res =  curr_cost, curr_cap
	            else:
	                res =  p_cost, p_cap
	        elif curr_cap == 0:
	            res =  curr_cost, curr_cap
	        elif p_cap == 0:
	            res =  p_cost, p_cap
	        else:
	            res = float('inf'), float('inf')
	        cache[(idx, cap)] = res
	        return res
	    return sum([dp(len(B)-1, el)[0] for el in A])
```
