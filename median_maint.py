from functools import reduce

file = open(r'C:\Users\skbha\videos\Median.txt')
data = file.readlines()
nums = []
for line in data:
    nums.append(int(line))
'''Algorithm to manatain median of a given sequence.
Uses Two Heaps. First Heap contains lower n/2 elements and Second Heap contains upper n/2 elements.First one is a min Heap and Second One is the MaxHeap
Median is the root of the Min Heap or Max Heap depending on which one has larger element. If Both heaps have tie , then both roots are median'''


class MinHeap(object):
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
            return None
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


class MaxHeap(MinHeap):
    def __init__(self):
        super().__init__()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.get_parent(index) < self.items[index]:
            parent_index = self.get_parent_index(index)
            self.items[parent_index], self.items[index] = self.items[index], self.items[parent_index]
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index) > self.items[smaller_child_index]:
                smaller_child_index = self.get_right_child_index(index)
            if self.items[index] > self.items[smaller_child_index]:
                break
            else:
                self.items[index], self.items[smaller_child_index] = self.items[smaller_child_index], self.items[index]
            index = smaller_child_index

res = []
# Let's test the MaxHeap
h = MaxHeap()
items = [9, 5, 33, 45, 8, 66, 76, 100,4,2]
for el in items:
    h.add_item(el)
assert h.peek() == 100
print("peek works fine !")
h.poll()
assert h.peek() == 76
print("poll works fine !")
res = []
l_half = MaxHeap()
u_half = MinHeap()
def add_element(el):
    if l_half.peek() is None:
        # print("in if",el)
        l_half.add_item(el)
        return None
    if u_half.peek() is None:
        # print("in elif",el)
        if el > l_half.peek():
            u_half.add_item(el)
        else:
            temp  = l_half.poll()
            l_half.add_item(el)
            u_half.add_item(temp)
        return None
    else:
        if el < l_half.peek():
            # print("adding in",el)
            l_half.add_item(el)
        else:
            # print("adding in",el)
            u_half.add_item(el)
        check_balancing(l_half, u_half)

def check_balancing(lower_half, upper_half):
    if len(lower_half.items) - len(upper_half.items) >= 2:
        i = lower_half.poll()
        upper_half.add_item(i)
    elif len(upper_half.items) - len(lower_half.items) >= 2:
        i = upper_half.poll()
        lower_half.add_item(i)


# let's try to implement get_median using min heap and max heap !.
def getMedian(arr):
    lower_half = MaxHeap()
    upper_half = MinHeap()
    el1, el2 = arr[0], arr[1]
    sorts = sorted([el1, el2])
    arr = arr[2:]
    lower_half.add_item(sorts[0])
    upper_half.add_item(sorts[1])
    for el in arr:
        if el < lower_half.peek():
            lower_half.add_item(el)
        else:
            upper_half.add_item(el)
        check_balancing(lower_half, upper_half)
    return lower_half, upper_half

def final_medain():
    l = l_half
    h = u_half
    t = None
    # print("lower half and upper half are")
    # print(l.peek(), h.peek())
    if len(l.items)>len(h.items):
        median = l.peek()
        # res.append(l.peek())
        print("median is c",l.peek())
    elif len(l.items)<len(h.items):
        median = h.peek()
        # res.append(l.peek())
        print("median is b",h.peek())
    else:
        median = l.peek()
        print("median is a",l.peek())
    # print(" MWSIan",median)
    global res
    res.append(median)
    print("res is ",res)
    return median

temp = []
for el in nums:
    print("adding",el)
    #print("heap states",l_half.items,u_half.items)
    add_element(el)
    final_medain()
print("res is ",res)
print("len",len(res),reduce(lambda x,y:x+y,res)%10000)
