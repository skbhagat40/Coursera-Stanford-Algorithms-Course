import sys, threading
sys.setrecursionlimit(900000)
threading.stack_size(67108864)
class Node(object):
    def __init__(self, val):
        self.val = val
        self.leader = None
        self.finish = None
        self.visited = False

    def __str__(self):
        return str(self.val) + "," + str(self.finish)


numbers = []
edges = {}
rev_edges = {}
nodes_list = []
with open(r'C:\Users\skbha\videos\SCC.txt', 'r') as f:
    for line in f.readlines():
        n = line.split()
        temp = [int(x) for x in n if x.isalnum()]
        numbers.append(temp)
        nodes_list.extend(temp)
        edges[temp[0]] = []
        rev_edges[temp[1]] = []
print('finished reading')
# let's build the edges
print(numbers[1:20])
for el in numbers[:]:
  if el[0] != el[1]:
        edges[el[0]].append(el[1])
        rev_edges[el[1]].append(el[0])
print('finished building')
nodes_list_sorted_by_finish_time = []
print(rev_edges[2])
# dfs subbroutine for first dfs pass on reverse graph of KosaRaju's Algorithm
ctr =0

def dfsr( node,rev_edges=rev_edges):
    global visited
    global ctr
    ctr += 1
    print(len(visited),"visin","c",ctr)
    if node is not None:
        if node not in visited:
            visited.add(node)
    if node is not None:
        for child in rev_edges.get(node,[]):
            if type(child) != type([1]) and child not in visited:
                dfsr( child)
    global nodes_sorted_by_finish_time
    nodes_list_sorted_by_finish_time.append(node)

leaders = {}
# dfs Subroutine for second DFS pass of Kosaraju's algorithm on Forward Graph
def dfs( node,edges = edges):
    global visitedf
    if node is not None:
        if node not in visitedf:
            visitedf.add(node)
    for child in edges.get(node,[]):
        if type(child) != type([1]) and child not in visited :
            dfs( child)
    global s
    global leaders
    leaders[s] = leaders.get(s,[]) + [node]
visited = set()

# forward dfs pass of kosaraju's algorithm computes finishing time on reverse graph
t_current = 1
for node in nodes_list:
    print(len(visited),"vis")
    if node not in visited:
        dfsr( node)
print('finished first pass')
#nodes_list_sorted_by_finish_time = sorted(nodes_list,key=lambda x:x.finish,reverse=True)
visitedf = set()
# let's do the forward pass of the kosaraju's algorithm
s = None
for node in nodes_list_sorted_by_finish_time[:]:
    if node not in visitedf:
        s = node
        dfs(node)
# lets computed the strongly connected components
print(len(visited),len(visitedf))
print(list(leaders.values())[:5])

#print('lets see the correctness and print if node is visited and has a valid leader',nodes_list_sorted_by_finish_time[0].visited,nodes_list_sorted_by_finish_time[0].leader)