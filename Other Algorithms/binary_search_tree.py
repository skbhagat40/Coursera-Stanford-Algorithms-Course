'''
Binary Search Tree Implementation
'''

# Write your code here
print("enter")
n = input()
print("enter again")
other = input()
tp = other.split()
tp = [int(x) for x in tp]


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def add_element(self, value):
        # print("root",type(self.root))
        self.add_element_helper(self.root, value, None, None)

    def get_height(self):
        pass

    def add_element_helper(self, current, value, parent, dir):
        if current == None:
            if dir == 'r':
                parent.right = Node(value)
            else:
                parent.left = Node(value)
            # return True
        else:
            left, right = None, None
            current_node = current
            if current.val < value:
                right = self.add_element_helper(current.right, value, current, 'r')
            else:
                left = self.add_element_helper(current.left, value, current, 'l')
            # if left:
            #     current_node.left = Node(value)
            # else:
            #     current_node.right = Node(value)
            # return None

    def dfs_traversal(self):
        self.max = []
        self.dfs_traversal_helper(self.root, [])

    def dfs_traversal_helper(self, current, path):
        if current is None:
            return None
        else:
            path = path + [current.val]
            self.max.append(len(path))
            print("path", path)
            print(current.val)
            left = self.dfs_traversal_helper(current.left, path)

            right = self.dfs_traversal_helper(current.right, path)


root = tp.pop(0)
b = BTree(root)
for el in tp:
    b.add_element(el)
# print("the tree looks like : ")
m = b.dfs_traversal()
print(max(b.max))

