# implementation of topological sort using a. Vertex Deletion Algo and b. DFS implementation
class Node(object):
    def __init__(self, value):
        self.value = value
        self.visited = None

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
        self.edges[start] = self.edges[start].append(end)

    def get_children(self, node):
        return self.edges[node]
# topological sort function
def topological_sort(g):
    nodes = list(g.edges.keys())
    while len(nodes) > 0:
        a = nodes[0]
        ch = g.get_children(a)[0]
        while ch != None:
            prev = ch
            ch = g.get_children(ch)[0]
        nodes.remove(prev)
        print("removed",prev.value)
        for el in g.edges:
            try:
                g.edges[el].remove(prev)
            except:
                pass
g = Graph()

