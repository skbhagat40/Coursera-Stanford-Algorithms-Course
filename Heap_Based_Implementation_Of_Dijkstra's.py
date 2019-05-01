'''Here we will do heap based implementation of Dijkstra's Shortest Path Algorithm'''
# let's implement dijkstra using modified Heap
from math import inf

'''Here we will implement modified version of the Heap
It will support deletion of elements from middle of the Heap also.
We will use this implementation in Dijkstra's Shortest Path Algorithm'''
# let's try to add a map that will store vertex value and it's position in the heap array.

class HeapNode(object):
    def __init__(self, value=None, key=None):
        self.value = value
        self.key = key

    def __str__(self):
        return "value : " + str(self.value) + "," + "key : " + str(self.key)


class Heap(object):
    def __init__(self):
        self.size = 0
        self.items = []  # an array that will store heap nodes
        self.map = {} # a dictionary that will store heap node value and it's position in the heap array.

    @staticmethod
    def get_left_child_index(index):
        return 2 * index + 1

    @staticmethod
    def get_right_child_index(index):
        return 2 * index + 2

    @staticmethod
    def get_parent_index(index):
        return (index - 1) // 2

    def has_left_child(self, index):
        return 2 * index + 1 < self.size

    def has_right_child(self, index):
        return 2 * index + 2 < self.size

    @staticmethod
    def has_parent(index):
        return (index - 1) // 2 >= 0

    def get_parent(self, index):
        return self.items[self.get_parent_index(index)]

    def get_left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def get_right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def peek(self):
        if self.size == 0:
            raise IndexError("The Heap Is empty")
        else:
            return self.items[0]

    def poll(self):
        to_ret = self.items[0]
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.size -= 1
        self.heapify_down()
        return to_ret

    def add_item(self, value):
        self.items.append(value)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):  # Nodes are now heap nodes.
        index = self.size - 1
        while self.has_parent(index) and self.get_parent(index).key > self.items[index].key:
            parent_index = self.get_parent_index(index)
            self.items[parent_index], self.items[index] = self.items[index], self.items[parent_index]
            index = self.get_parent_index(index)
            self.map[self.items[self.size - 1].value] = index
    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index).key < self.items[smaller_child_index].key:
                smaller_child_index = self.get_right_child_index(index)
            if self.items[index].key < self.items[smaller_child_index].key:
                break
            else:
                self.items[index], self.items[smaller_child_index] = self.items[smaller_child_index], self.items[index]
            index = smaller_child_index
            self.map[self.items[0].value] = index

# we will modify our existing heap implementation and add extra functionality to it.

class ModifiedHeap(Heap):
    def __init__(self):
        super().__init__()

    def heapify_up_modified(self, index):
        # index = self.size - 1
        orig = index
        try:
            while self.has_parent(index) and self.get_parent(index).key > self.items[index].key:
                parent_index = self.get_parent_index(index)
                self.items[parent_index], self.items[index] = self.items[index], self.items[parent_index]
                index = self.get_parent_index(index)
                self.map[self.items[orig].value] = index
        except:
            pass

    def heapify_down_modified(self, index):
        # index = 0
        orig = index
        try:
            while self.has_left_child(index):
                smaller_child_index = self.get_left_child_index(index)
                if self.has_right_child(index) and self.get_right_child(index).key < self.items[
                    smaller_child_index].key:
                    smaller_child_index = self.get_right_child_index(index)
                if self.items[index].key < self.items[smaller_child_index].key:
                    break
                else:
                    self.items[index], self.items[smaller_child_index] = self.items[smaller_child_index], self.items[
                        index]
                index = smaller_child_index
                self.map[self.items[orig].value] = index
        except:
            pass

    def delete_node_modified(self, value):
        for i, e in enumerate(self.items):
            if e.value == value:
                # print("index",i,"value at index",self.items[i].value)
                index = i
                break
        # try:
        #     index = self.map[value]
        # except:
        #     for i, e in enumerate(self.items):
        #         if e.value == value:
        #             # print("index",i,"value at index",self.items[i].value)
        #             index = i
        #             break
        ''' Deletes a Node at a given Index. Input is the index of the Node. Modifies the heap. Output is None.
        Steps - 1. Swap the element at current index with the element at the last index
                2. Delete the element at the last index . Decrease the size of the Heap.
                3. Heapify Up and Heapify Down'''
        self.items[index], self.items[-1] = self.items[-1], self.items[index]
        del self.items[-1]
        self.size -= 1
        self.heapify_up_modified(index)
        self.heapify_down_modified(index)


# Let's check if our implementation of Heap based on Heap Node is working correctly or not.
# h = ModifiedHeap()
# h.add_item(HeapNode(4, 9))
# h.add_item(HeapNode(1, 6))
# h.add_item(HeapNode(8, 5))
# h.add_item(HeapNode(7, 2))
# h.add_item(HeapNode(9, 0))
# h.poll()
# h.delete_node_modified(1)
# print("finally the heap structure is")
# for el in h.items:
#     print(el)
# ok! it's working correctly.

# let's try to implement dijkstra algorithm using out Heap.
# Initialize the graph and the heap.
h = ModifiedHeap()
file = open(r'C:\Users\skbha\videos\dijkstra.txt')
data = file.readlines()
num_nodes = 201
graph = [[] for el in range(num_nodes)]
edge_cost = [[] for el in range(num_nodes)]
for line in data:
    items = line.split()
    node = int(items[0])
    for el in items[1:]:
        temp = el.split(",")
        graph[node].append(int(temp[0]))
        edge_cost[node].append(int(temp[1]))
print("graph", graph[:5])
# graph = [[1, 2], [3], [6, 4], [4, 6], [5], [6], []]
# edge_cost = [[2, 3], [5], [2, 2], [1, 4], [2], [3]]
over_head = [inf] * num_nodes

conquered = [False] * num_nodes
seen = set()
for el in range(num_nodes):
    if el != 1:
        h.add_item(HeapNode(el, inf))


def dijkstra(source):
    conquered[source] = True
    seen.add(source)
    over_head[source] = 0
    # h.delete_node_modified(source)
    h.add_item(HeapNode(source, 0))
    # for index, child in enumerate(graph[source]):
    #     if child not in seen:
    #         # constructing heap node
    #         h.delete_node_modified(child)
    #         key_child = over_head[source] + edge_cost[source][index]
    #         h.add_item(HeapNode(child, key_child))
    # Now our dijkstra's algorithm is initialized.
    # Next Steps that follow are -
    # 1. First We Do Polling.
    # 2. We look for children of the vertex we get after polling
    # 3. We update the keys of children if possible.
    # 4. We update over_head,conquered and seen
    # print("heap after first add operation")
    # for el in h.items:
    #     print(el)
    while len(h.items) != 0:
        w = h.poll()
        w_star = w.value
        seen.add(w_star)
        conquered[w_star] = True
        over_head[w_star] = w.key
        # print("overhead for",w.value,w.key)
        for index, child in enumerate(graph[w_star]):
            if not conquered[child]:
                new_over_head = over_head[w_star] + edge_cost[w_star][index]
                if new_over_head >= over_head[child]:
                    continue
                else:
                    # print("deleting",child)
                    h.delete_node_modified(child)
                    new_cost = new_over_head
                    # print("modifying child",child,new_cost)
                    over_head[child] = new_cost
                    h.add_item(HeapNode(child, new_cost))


dijkstra(1)
print(over_head)
# after first polling operation the structure of the heap is :-
print("heap after dijkstra's operation")
for el in h.items:
    print(el)
print("over_head", over_head)
res = []
for el in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
    res.append(over_head[el])
print("r", res)
