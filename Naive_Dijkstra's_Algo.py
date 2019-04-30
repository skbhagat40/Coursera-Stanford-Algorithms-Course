'''Naive Implementation of Dijkstra's Single Source Shortest Path Algorihtm.
Computes The shortest path of Source to all the vertices.
Uses Greedy Approach.
Nodes are represented as lists.
Edges are represented as list of lists
And we will have an path cost matrix. Sort of Node Overhead Matrix
Runtime Complexity is O(m*n) where m = no. of edges , n = no. of vertices'''
from math import inf

# print("hello")
# file = open(r'C:\Users\skbha\videos\dijkstra.txt')
# data = file.readlines()
# num_nodes = 201
# graph = [[] for el in range(num_nodes)]
# edge_cost = [[] for el in range(num_nodes)]
# for line in data:
#     items = line.split()
#     node = int(items[0])
#     for el in items[1:]:
#         temp = el.split(",")
#         graph[node].append(int(temp[0]))
#         edge_cost[node].append(int(temp[1]))
# print(graph,edge_cost)
# print("carry on")
num_nodes =7
graph = [[1, 2], [3], [6, 4], [4, 6], [5], [6], []]
edge_cost = [[2, 3], [5], [2, 2], [1, 4], [2], [3]]
# graph = [[],[2,8],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,1]]
# edge_cost = [[],[1,2],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,2]]
over_head = [inf] * num_nodes

conquered = [False] * num_nodes
seen = set()


def dijkstra(source):
    conquered[source] = True
    seen.add(source)
    over_head[source] = 0
    for i in range(num_nodes):
        print("still running",conquered)
        minimum = inf
        selected = None
        for node in seen:
            for index, child in enumerate(graph[node]):
                if child not in seen:
                    print(node, child)
                    cost = over_head[node] + edge_cost[node][index]
                    print("cost", cost)
                    if cost < minimum:
                        minimum = cost
                        selected = child
                        print("selected", child)
        if selected is not None:
            conquered[selected] = True
            seen.add(selected)
            over_head[selected] = minimum

        # res = []
        # for el in [7,37,59,82,99,115,133,165,188,197]:
        #     res.append(over_head[el])
        # print(res)



dijkstra(1)
print(over_head)
