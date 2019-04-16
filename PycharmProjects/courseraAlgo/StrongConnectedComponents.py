class Node(object):
    def __init__(self,val):
        self.val = val
        self.leader = None
        self.finish = None
        self.visited = False
    def __str__(self):
        return str(self.val)+","+str(self.finish)
class Edge(object):
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __str__(self):
        return "from : "+str(self.start)+"to :"+ str(self.end)
class Graph(object):
    def __init__(self):
        self.edges = {}
    def addNode(self,node):
        self.edges[node] = []
    def addEdge(self,edge):
        start = edge.start
        end = edge.end
        self.edges[start]=self.edges[start]+[end]
    def get_children(self,node):
        return self.edges[node]
g = Graph()
nodes_list = [Node(i) for i in range(1,11)]
for node in nodes_list:
    g.addNode(node)
g.addEdge(Edge(nodes_list[0],nodes_list[1]))
g.addEdge(Edge(nodes_list[1],nodes_list[2]))
g.addEdge(Edge(nodes_list[2],nodes_list[0]))
g.addEdge(Edge(nodes_list[1],nodes_list[3]))
g.addEdge(Edge(nodes_list[4],nodes_list[3]))
g.addEdge(Edge(nodes_list[4],nodes_list[5]))
g.addEdge(Edge(nodes_list[5],nodes_list[6]))
g.addEdge(Edge(nodes_list[6],nodes_list[4]))
g.addEdge(Edge(nodes_list[7],nodes_list[6]))
g.addEdge(Edge(nodes_list[7],nodes_list[8]))
g.addEdge(Edge(nodes_list[8],nodes_list[9]))
g.addEdge(Edge(nodes_list[9],nodes_list[7]))
print("the graph is :")
print(g.edges)
for k in g.edges:
    for v in g.edges[k]:
        print(k.val,v.val)

# dfs subroutine
def dfs(g,node):
    if node is not None:
        if node.visited == False:
            node.visited = True
    if node is not None:
        for child in g.get_children(node):
            if child.visited == False:
                dfs(g,child)
    global t_current
    node.finish = t_current
    t_current += 1
def dfsr(g,node):
    if node is not None:
        if node.visited == False:
            node.visited = True
    for child in g.get_children(node):
        if child.visited == False:
            dfsr(g,child)
    global s
    node.leader = s
# forward dfs pass of kosaraju's algorithm computes finishing time
t_current = 1
for node in nodes_list:
    if node.visited == False:
        dfs(g,node)
print('after dfs traversal')
for n in list(g.edges.values()):
    print([str(x) for x in n])
# backward dfs pass of kosaraju's algorithm computes leader
s = None
nodes_list_sorted = sorted(nodes_list,key=lambda x:x.finish,reverse=True)
print('before after')
print([str(n) for  n in nodes_list])
print([str(n) for n in nodes_list_sorted])
s = None # to keep track of leader
# need to reverse the graph first
# pass copy of graph here
def reverse_graph(g):
    rev = {}
    for k in g:
        for el in g[k]:
            rev[el] = rev.get(el,[]) + [k]
    return rev
rev = reverse_graph(g.edges.copy())
print('original graph')
for k in g.edges:
    for v in g.edges[k]:
        print(k.val,v.val)
print('reversed graph')
print(rev)
for k in rev:
    for v in rev[k]:
        print(k.val,v.val)
g_rev = Graph()
for nodes in nodes_list:
    g_rev.addNode(nodes)
g_rev.edges = rev
# lets traverse
for node in nodes_list_sorted[:]:
    node.visited = False
for node in nodes_list_sorted[:]:
    if node.visited == False:
        s = node
        dfsr(g_rev,node)
# ok lets see the strongly connected components
print('sccs')
for eld in g_rev.edges.values():
    print([(el.val,str(el.leader)) for el in eld])
# yay ! it worked !