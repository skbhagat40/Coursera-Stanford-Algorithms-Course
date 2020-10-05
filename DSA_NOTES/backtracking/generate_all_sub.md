Generating all possible subsequences from a given string, backtracking / dfs problem.
It can be though of as appending, and each append starting a new recursion tree, with it's own rem (remaining elements to choose from)

// My mistake, to get all possiblites, I only need to last value, as other one is already pushed into the recursion stack.
