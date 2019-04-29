'''Here we will implement modified version of the Heap
It will support deletion of elements from middle of the Heap also.
We will use this implementation in Dijkstra's Shortest Path Algorithm'''

class Heap(object):
    def __init__(self):
        self.size = 0
        self.items = []  # an array that will store heap nodes

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
        index = 0
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.size -= 1
        self.heapify_down()
        return self.items[index]

    def add_item(self, value):
        self.items.append(value)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.get_parent(index) > self.items[index]:
            parent_index = self.get_parent_index(index)
            self.items[parent_index], self.items[index] = self.items[index], self.items[parent_index]
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index) < self.items[smaller_child_index]:
                smaller_child_index = self.get_right_child_index(index)
            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.items[index], self.items[smaller_child_index] = self.items[smaller_child_index], self.items[index]
            index = smaller_child_index
# we will modify our existing heap implementation and add extra functionality to it.

class ModifiedHeap(Heap):
    def __init__(self):
        super().__init__()

    def heapify_up_modified(self, index):
        # index = self.size - 1
        while self.has_parent(index) and self.get_parent(index) > self.items[index]:
            parent_index = self.get_parent_index(index)
            self.items[parent_index], self.items[index] = self.items[index], self.items[parent_index]
            index = self.get_parent_index(index)

    def heapify_down_modified(self, index):
        # index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index) < self.items[smaller_child_index]:
                smaller_child_index = self.get_right_child_index(index)
            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.items[index], self.items[smaller_child_index] = self.items[smaller_child_index], self.items[index]
            index = smaller_child_index

    def delete_node_modified(self, index):
        ''' Deletes a Node at a given Index. Input is the index of the Node. Modifies the heap. Output is None.
        Steps - 1. Swap the element at current index with the element at the last index
                2. Delete the element at the last index . Decrease the size of the Heap.
                3. Heapify Up and Heapify Down'''
        self.items[index], self.items[-1] = self.items[-1], self.items[index]
        del self.items[-1]
        self.size -= 1
        self.heapify_up_modified(index)
        self.heapify_down_modified(index)

# let's check if it is working correctly.
h = ModifiedHeap()
h.add_item(6)
h.add_item(4)
h.add_item(0)
h.add_item(24)
h.add_item(7)
assert h.peek() == 0
print(h.items)
h.delete_node_modified(2)
print(h.items)
