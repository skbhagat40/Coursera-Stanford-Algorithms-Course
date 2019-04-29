'''Naive Implementation of Dijkstra's Single Source Shortest Path Algorihtm.
Computes The shortest path of Source to all the vertices.
Uses Greedy Approach.
Nodes are represented as lists.
Edges are represented as list of lists
And we will have an path cost matrix. Sort of Node Overhead Matrix'''
from math import inf

num_nodes = 7
graph = [[1, 2], [3], [6, 4], [4, 6], [5], [6], []]
edge_cost = [[2, 3], [5], [2, 2], [1, 4], [2], [3]]
over_head = [inf] * num_nodes

conquered = [False] * num_nodes
seen = set()


def dijkstra(source):
    conquered[source] = True
    seen.add(source)
    over_head[source] = 0
    while sum(conquered) != num_nodes:
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

        conquered[selected] = True
        seen.add(selected)
        over_head[selected] = minimum
        print("over_head", over_head)


dijkstra(0)
print(over_head)
