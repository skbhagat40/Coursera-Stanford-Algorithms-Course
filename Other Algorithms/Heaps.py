'''Here We will implement heap data structure.
1. A heap is a perfectly balanced Binary  Tree , the parent is always smaller than it's children in Min Heap
2. Supports O(1) min/max extract operation depending on type of Heap i.e. min Heap of max Heap
3. Here we will implement following methods :-
   a. Peek - returns the min/max value
   b. Pool - returns and deletes min/max value
   c. Add - adds an Elemnt to the heap. Element is added to the Next empty position i.e. top to bottom left to right.
Here we will use array to represent Heap. LeftChild = 2*index +1 , RightChild = 2*index+2. Parent = (index-1)//2 .'''


# let's begin
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


if __name__ == '__main__':
    # let's test this heap
    h = Heap()
    h.add_item(4)
    h.add_item(1)
    h.add_item(8)
    h.add_item(7)
    print("smallest element in the heap is :", h.peek())
    assert h.peek() == 1
    # add_item and peak works !
    # let's check if poll works or not
    a = h.poll()
    print("smallest element in the heap after polling is :", h.peek())
    assert h.peek() == 4
    h.add_item(0)
    assert h.peek() == 0
    print("smallest item is now", h.peek())
    # all good thanks! :)
