'''Heap Sort Agorithm'''


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


h = Heap()
arr = [9, 55, 1,  6, 8, 12, 36]  # We will sort this array using Heap Sort Algorithm
for el in arr:
    h.add_item(el)
res = []
print("initial",h.items)
# print(h.poll())
while len(h.items) >= 1:
    a = h.poll()
    print(a)
    res.append(a)
print("sorted array is")
print(h.items)
print(res)