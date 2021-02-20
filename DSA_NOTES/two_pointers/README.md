Two Pointers.
Things to consider when applying two pointers.
1. Physical significance of the two pointers. (Range/Pair)
2. How to initialize the pointers. (We are able to make decision and converge to solution.)
3. How to move the pointers.
4. When to stop Iteration.

Applications - 

1. Given a sorted array of integers, find a pair whose sum is K.

To find - a[i] + a[j] = K. i < j.

case 1 - a[i] + a[j] > K, decrease j. (since, the array is sorted.)
case 2 - a[i] + a[j] < K, increase i. (since, we need a bigger value.)

So, using above observation, we initialize pointers s,e = 0, len(a) - 1. 

_variation_ - count all pairs. In that case, if a[i] != a[j], ans += count(i) * count(j), else use nC2.

2. Given a sorted array of integers, find a pair whose difference is K. (diffK)

To find a[i] - a[j] = K.

case 1 - a[i] - a[j] > K. (Either increase i or decrease j)
case 2 - a[i] - a[j] < K. (either increase j or decrease j)

s = 0, e = 1. (We eliminate the option of decreasing j when sum is greater, and vice-versa. since, we have already looked at all previous combinations.)

**I doubt wheather this approach can work with sum also. Coz in this case we have the option to increase both the pointers also.**.

3. Rectangle pairs.

given a sorted array, find the pair of integers with area < B. squares are also possible.

similiar to sumK problem. find i,j such that a[i]*a[j] < B. ans += 2x(j-i+1) - 1.

then increment i. No need to reset the end pointer because the array is sorted. and bigger value will only give bigger area.


4. 3 pointers.
Given 3 arrays return min(abs(max(a,b,c)- min(a,b,c))).

Observation - Since, the array is sorted, we can only increase the min.
i,j,k = 0.

# only need to keep track of minimum and maximum, third element is useless.

keep incrementing the index with min value. keep updating answer. stop when any of the array exhausts.

**Cases where two pointes is used in unsorted array.**

5. Sliding Window - To find a subarray with sum K.

4. Container with maximum area.

6. Trapping Rain water -> https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2975/. similar to container with max area.

8. Merge k sorted lists. (possibly)

Observation- for a[i] we need to find farthest j, such that a[j] >= a[i]. If not, we find the answer for a[j].

**Use Cases of Sliding Window**
1. Longest substring with atmost k distinct characters.
2. Special Integer - In combination with binary search (over answer space). We use sliding window for finding subarray with sum K.ßsß
