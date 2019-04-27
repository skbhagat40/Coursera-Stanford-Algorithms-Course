class Node(object):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return self.value
class Edge(object):
    def __init__(self,fromNode,toNode):
        self.fromNode = fromNode
        self.toNode = toNode
class Grph(object):
    def __init__(self):
        # dict mapping from a node to it's connections in the graph
        self.edges = {}
    def addNode(self,node):
        self.edges[node] = []
    def addEdge(self,edge):
        startNode = edge.fromNode
        toNode = edge.toNode
        self.edges[startNode] = self.edges.get(startNode)+[toNode]
    def getChildren(self,node):
        return self.edges[node]

#let's construct the graph
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
edge1 = Edge(node1,node2)
edge6 = Edge(node1,node3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
edge2 = Edge(node2,node4)
edge3 = Edge(node2,node5)
edge4 = Edge(node3,node6)
edge5 = Edge(node3,node7)
g = Grph()
g.addNode(node1)
g.addNode(node2)
g.addNode(node3)
g.addNode(node4)
g.addNode(node5)
g.addNode(node6)
g.addNode(node7)
g.addEdge(edge1)
g.addEdge(edge2)
g.addEdge(edge3)
g.addEdge(edge4)
g.addEdge(edge5)
g.addEdge(edge6)
# the dfs algorithm
def dfs(g,root,toFind,path,bestPath):
    path = path + [root]
    print("dfs traversal", root.value)
    # add does the trick of creating variable in new scope
    if root.value == toFind:

        return path
    else:
        print("children",g.getChildren(root))
        for child in g.getChildren(root):
            if child not in path:
                found = dfs(g,child,toFind,path,bestPath)
                if found != None:
                    bestPath = found
                    return bestPath
# calling dfs
# bestpath = dfs(g,node1,7,[],[])
# print(bestpath)
# print("following path is found out")
# for el in bestpath:
#     print("node",el.value)
# cool! it works let's try out maxval also
class Item(object):
    def __init__(self,value,cost):
        self.cost = cost
        self.value = value
    def __str__(self):
        return "value : "+str(self.value)+","+"cost : "+str(self.cost)
def maxVal(toConsider,avail):
    if len(toConsider)==0 or avail==0:
        return  (0,[])
    elif toConsider[0].cost > avail:
        return maxVal(toConsider[1:],avail)
    else:
        newItem = toConsider[0]
        withVal,withToTake = maxVal(toConsider[1:],avail-newItem.cost)
        withVal += newItem.value
        withoutVal,withoutToTake = maxVal(toConsider[1:],avail)
        print("inside function",withVal,withoutVal,newItem.value,newItem.cost)
        if withVal > withoutVal:
            print("returning",toConsider.append(newItem))
            result =  (withVal,toConsider.append(newItem))
        else:
            print("returning", toConsider)
            result = (withoutVal,toConsider)
    return result

ob1 = Item(value=20,cost=20)
ob2 = Item(value=30,cost=10)
ob3 = Item(value=10,cost=30)
list_of_items = [ob1,ob2,ob3]
res = maxVal(list_of_items,30)
print("result of maxVal is",res)
#for el in res[1]:
    #print(el)