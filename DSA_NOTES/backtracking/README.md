Tracing back steps to explore different possiblities.

Problems - 
1. Find path in a maze .
2. placing N queens in a chessboard. (mantaining a column for position (i, c[i]))

O(n^n) n possiblites for n positons.
No need to do undo step coz change in past is not affecting the current step here.

Some cases, there is need to reset the state, in some not.
marking visited nodes, to avoid cycles.
recursion takes care of exploring all other possiblities.

3. Soduku

Need to reset the state here. O(n^(n*n)) n*n spaces to fill.

4. Grey Code

Using formula, not using backtracking.

General  Approach of using BackTracking - (Steps)

1. Check for Completion Conditon (return True)
2. Try to prune the possiblities (If the current state is invalid ignore it.)
3. Iterate over all the possiblities (all possible states).
4.  Do step - Doing something for the current state. (Changing/modifying the state. e.g. marking visited. Marking column in case of queens problem.)
5.  Recursive call.
6.  Undo Step (If current state is invalid or returning back from the recursion. using if else condition on the return value.)

Undo step is needed only when if change in past is affecting the current state and (current state is checked for previous states). In soduku example.