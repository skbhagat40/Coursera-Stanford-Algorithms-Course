"""
This piece of code implements the logic of
counting the number of islands.
We will use depth first search algorithm here.
"""
# grid = None
indices = []
current_index = None


def count_islands(grid):
    global A
    A = grid
    # Method to traverse through all elements in the array.
    global grid_copy
    grid_copy = [[False] * len(grid[0]) for _ in range(len(grid))]
    # Keeps Track weather a particular 1 has been visited earlier or not.
    for idx, el in enumerate(grid):
        for idxi, eli in enumerate(el):
            if eli == 1 and not grid_copy[idx][idxi]:
                global current_index
                current_index = (idx, idxi)
                grid_copy[idx][idxi] = True
                dfs((idx, idxi))


def dfs(tup):
    # tup is a tuple which represents the co-ordinates.
    # This dfs operates on a node. need a root node, End the
    # dfs when Node is None. Will use a tuple here.
    print(tup, grid_copy)
    if tup is None:
        return None
    else:
        children = getChildren(tup)
        for child in children:
            print(child)
            if child is not None and not(grid_copy[child[0]][child[1]]):
                print('child', child)
                grid_copy[child[0]][child[1]] = True
                indices.append(current_index)
                return dfs(child)


def getChildren(tup):
    print('tup', tup, grid_copy)
    # This function takes a cordinate and return it's children.
    # sanity check to see if children are within limits.
    # can have at max 4 children.
    # child1 is the left child.
    # child2 is the top child.
    # child3 is the right child.
    # child4 is the bottom child.
    child1, child2, child3, child4 = None, None, None, None
    i, j = tup
    left_boundary = 0
    right_boundary = len(A[0]) - 1
    top_boundary = 0
    bottom_boundary = len(A) - 1
    if j - 1 >= left_boundary:
        child1 = (i, j-1)
        if A[child1[0]][child1[1]] != 1:
            child1 = None
    if i - 1 >= top_boundary:
        child2 = (i-1, j)
        if A[child2[0]][child2[1]] != 1:
            child2 = None
    if j + 1 <= right_boundary:
        child3 = (i, j+1)
        if A[child3[0]][child3[1]] != 1:
            child3 = None
    if i + 1 <= bottom_boundary:
        child4 = (i+1, j)
        if A[child4[0]][child4[1]] != 1:
            child4 = None
    print('returning', [child1, child2, child3, child4], grid_copy)
    return [child1, child2, child3, child4]


count_islands([
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 1, 0]
])
print('indices', indices)
print('grid copy', grid_copy)
