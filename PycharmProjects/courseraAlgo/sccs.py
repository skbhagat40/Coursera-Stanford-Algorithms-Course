# my submission for programming assignment 1 for part 2 of the algorithms specialization course by coursera. Program finishes under a minute !
from collections import defaultdict
import sys,threading
threading.stack_size(52428800)
class Node(object):
    def __init__(self,val):
        self.val = val
        self.visited = False
        self.Finish = None
        self.leader = None

num_nodes = 875715
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]
visited = [False] * num_nodes
# the list index represents the node.
scc = [0] * num_nodes
stack = []  # Stack for DFS
order = []  # The finishing orders after the first pass
# Importing the graphs
file = open(r"C:\Users\skbha\videos\SCC.txt", "r") # I named the input file W1_SCC_edges.txt, but you can name it whatever you wish
data = file.readlines()

for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]
# DFS on reverse graph
print('dfs started')
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
added = [False]*num_nodes

for node in range(num_nodes):
    if visited[node]==False:
        stack.append(node)
    while stack:
        stack_node = stack[-1]
        #print("dfs traversal",stack_node)
        if visited[stack_node]==True :
            if not added[stack_node]:
                order.append(stack_node)
                added[stack_node] = True
            stack.pop(-1)
        visited[stack_node] = True
        for head in r_gr[stack_node]:
            if visited[head] == False:
                stack.append(head)

#print("order",order)
order = order[::-1]
print('dfs finished')
print("length of order",len(order))
stack = []
visited = [False] * len(visited)  # Resetting the visited variable
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
# Getting the five biggest sccs
scc.sort(reverse=True)
print(scc[:5])
