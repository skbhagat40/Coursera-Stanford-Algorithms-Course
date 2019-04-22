stack = []
num_nodes = 6
order = []
visited = [False]*num_nodes
r_gr= [[1,2],[3],[4],[4],[5],[]]
r_gr= [[1,2],[3],[4],[4],[5],[]]
gr = [[],[0],[0],[1],[2,3],[4]]
# for node in range(num_nodes):
#     if visited[node]==False:
#         stack.append(node)
#     while stack:
#         stack_node = stack.pop(-1)
#         print("dfs traversal",stack_node)
#         if not visited[stack_node]:
#             order.append(stack_node)
#         visited[stack_node] = True
#         for head in r_gr[stack_node]:
#             if visited[head] == False:
#                 stack.append(head)
#
#
# print("order",order)
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
order = order[::-1]
scc = [0]*num_nodes
visited = [False]*num_nodes
for node in order:
    if visited[node]==False:
        stack.append(node)
    while stack:
        stack_node = stack.pop(-1)
        if not visited[stack_node]:
            scc[node] += 1
        visited[stack_node] = True
        for head in gr[stack_node]:
            if visited[head] == False:
                stack.append(head)
    if visited[node]==False:
        stack.append(node)
    while stack:
        stack_node = stack.pop(-1)
        if not visited[stack_node]:
            scc[node] += 1
        visited[stack_node] = True
        for head in gr[stack_node]:
            if visited[head] == False:
                stack.append(head)
print(scc)