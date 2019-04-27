# implementation of topological sort using a. Vertex Deletion Algo and b. DFS implementation
class Node(object):
    def __init__(self, value):
        self.value = value
        self.visited = None
        self.order = None

    def __str__(self):
        return str(self.value)


class Edge(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "from : " + str(self.start) + "to : " + str(self.end)


class Graph(object):
    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        self.edges[node] = []

    def add_edge(self, edge):
        start = edge.start
        end = edge.end
        self.edges[start] = self.edges.get(start,[]) + [end]

    def get_children(self, node):
        return self.edges[node]


# topological sort function
def topological_sort(g,node,order):
# let's implement it in a recursive way
    if len(g.get_children(node)) == 0:
        print("node",node.value,order)
        del g.edges[node]
        for el in g.edges:
            try:
                g.edges[el].remove(node)
            except:
                pass
    else:
        try:
            topological_sort(g,g.get_children(node)[0],order)
        except:
            pass

g = Graph()
n1 = Node('a')
n2 = Node('b')
n3 = Node('c')
n4 = Node('d')
e1 = Edge(n1, n2)
e2 = Edge(n2, n3)
e3 = Edge(n1, n4)
e4 = Edge(n4, n3)
g.add_node(n1)
g.add_node(n2)
g.add_node(n3)
g.add_node(n4)
g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)
g.add_edge(e4)
print("graph is",g.edges)
for key in g.edges:
    for el in g.edges[key]:
        print(key.value,el.value)
order = 4
# while len(g.edges)>0:
#     topological_sort(g,n1,order)
#     order -= 1
# implementation using dfs
print('dfs implementation starts here')
n_current = 4
def dfs(graph,start,path):
    if start != None:
        path = path + [start]
        print("exploring",start.value,start.order)
    for child in graph.get_children(start):
        if child not in path:
            dfs(graph,child,path)
    global n_current
    if start.order == None:
        start.order = n_current
        n_current -= 1
    print(start.value,start.order,n_current)
dfs(g,n1,[])
for key in g.edges:
    for el in g.edges[key]:
        print(key.value,el.value,key.order,"key order",el.order,'el order')