import random
nodesa = {}
tnodes = {}
edges = []
l = [[2,3,4,7],[1,3,4],[1,2,4],[1,2,3,5],[4,6,7,8],[5,7,8],[1,5,6,8],[5,6,7]]
l1 = [[2,3,4,7],[1,3,4],[1,2,4],[1,2,3,5],[4,6,7,8],[5,7,8],[1,5,6,8],[5,6,7]]
l2 = [[2,3,4,7],[1,3,4],[1,2,4],[1,2,3,5],[4,6,7,8],[5,7,8],[1,5,6,8],[5,6,7]]
n = list(range(1,9))
best_cuts  = len(n)
for i in list(range(1,9)):
    nodesa[i] = l1[i-1]
    tnodes[i] = l1[i - 1]
global copy
copy= nodesa.copy()
def get_cuts(grp1,grp2):
    cuts = 0

    global copy
    #print(copy,grp1,grp2,"copy")
    for el in grp1:
        for ela in copy[el]:
            if ela in grp2:
                cuts += 1
    return cuts
# algorithm to find the subsets having minimum cuts
# need to construct a graph first
class Edge(object):
    def __init__(self,node1,node2):
        self.nodes = [node1,node2]
    def getNodes(self):
        return self.nodes
    def __str__(self):
        return str([self.nodes])

def get_nodes():
    global l
    print('l is ',l)
    nodes = {} # dict mapping from tuple of nodes a paticular edge
    tnodes = {}
    temp = l[:]
    for i in list(range(1,9)):
        nodes[i] = l[i-1][:]
        tnodes[i] = l[i - 1][:]
    return nodes
# need to find a way of getting cuts
#number of edges from supernode a to supernode b in the original list of edges.
# easy way out iterate over all the edges. and check if elements cross.

def build_edges(nodes):
    edges = []
    for key in nodes:
        for val in nodes[key]:
            edges.append(Edge(key,val))
    return edges
# print("nodes",nodes)
# cnodes = nodes.copy()
def minCut(nodes):
    contracted = []
    while len(nodes) > 2:
        print("in nodes",nodes)
        edges = build_edges(nodes)
        #print('edges are', [str(x) for  x in edges])
        rand_ch = random.randint(0, len(edges)-1)
        selected_edge = edges[rand_ch]
        contracted.append(selected_edge)
        del edges[rand_ch]
        # todo delete the two nodes and create a supernode and rearrange the edges
        deleted_node_1,deleted_node_2 = selected_edge.getNodes()
        #super_node = min(deleted_node_1,deleted_node_2)
        try:
            nodes[deleted_node_1].remove(deleted_node_2)
            nodes[deleted_node_2].remove(deleted_node_1)
        except:
            pass
        for el in nodes[deleted_node_2]:
            nodes[deleted_node_1].append(el)
        del nodes[deleted_node_2]
        for key in nodes:
            if deleted_node_2 in nodes[key]:
                nodes[key] = [deleted_node_1 if x==deleted_node_2 else x for x in nodes[key]]
        for key in nodes:
            nodes[key] = [x  for x in nodes[key] if x != key]
    return nodes,contracted
for i in range(20):
    print('passed dict',get_nodes())
    result,cedges = minCut(get_nodes())
   # print("result is",result)
    grp1,grp2 = [list(result.keys())[0]],[list(result.keys())[1]]
    for el in cedges:
        if el.getNodes()[0] in grp1:
            grp1.append(el.getNodes()[1])
        else:
            grp2.append(el.getNodes()[1])
    cuts = get_cuts(grp1,grp2)
    #print("cuts are",cuts,'groups are',grp1,grp2)
    if cuts<best_cuts:
        best_cuts = cuts
        best_grps = [grp1,grp2]
print("best cuts",best_cuts,best_grps)