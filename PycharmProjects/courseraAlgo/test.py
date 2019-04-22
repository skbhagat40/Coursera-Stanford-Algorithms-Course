stack = []
num_nodes = 5
order = []
visited = [False]*num_nodes
r_gr= [[1,2],[3],[4],[],[]]
for node in range(num_nodes):
    if visited[node]==False:
        stack.append(node)
    while stack:
        stack_node = stack[-1]
        print("dfs traversal",stack_node)
        if visited[stack_node]==True :
            order.append(stack_node)
            stack.pop(-1)
        visited[stack_node] = True
        for head in r_gr[stack_node]:
            if visited[head] == False:
                stack.append(head)

print("order",order)