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

            left = self.dfs_traversal_helper(current.left, path)
            print(current.val)
            right = self.dfs_traversal_helper(current.right, path)

    # let's add delete element functionality to our binary search tree
    def delete_item(self, value):
        '''assumes that item is present in the tree'''
        # easy case delete node.
        self.delete_item_helper(self.root, value, self.root, None)

    def delete_item_helper(self, current, value, parent, dir):
        if current.val == value:
            # found the node we want to delete
            if current.left is None and current.right is None:
                # easy case , it is a Leaf Node.
                if dir == 'r':
                    parent.right = None
                else:
                    parent.left = None
            elif current.left is None:
                # Medium Case , has only right child.
                if dir == 'r':
                    if parent is None:
                        self.root = current.right
                    parent.right = current.right
                else:
                    if parent is None:
                        self.root = current.right
                    parent.left = current.right
            elif current.right is None:
                # Medium Case has only left child
                if dir == 'r':
                    if parent is None:
                        self.root = current.left
                    parent.right = current.left
                else:
                    if parent is None:
                        self.root = current.left
                    parent.left = current.left
            else:
                # Hard Case Both The children are present.Compute current's predecessor and swap current with it.
                temp = current
                while current.left:
                    prev = current
                    current = current.left
                predecessor = current
                # swap predecessor and current
                predecessor.val, temp.val = temp.val, predecessor.val
                # let's delete predecessor
                if predecessor.left is None and predecessor.right is None:
                    prev.left = None
                if predecessor.left is None:
                    # only right child:
                    prev.left = predecessor.right
                else:
                    # only left child
                    prev.left = predecessor.left
        else:
            left, right = None, None
            current_node = current
            if current.val < value:
                right = self.delete_item_helper(current.right, value, current, 'r')
            else:
                left = self.delete_item_helper(current.left, value, current, 'l')


root = tp.pop(0)
b = BTree(root)
for el in tp:
    b.add_element(el)
# print("the tree looks like : ")
m = b.dfs_traversal()
print(max(b.max))
# let's add other operations to our binary search tree..
# let's check easy case delete_node works or not.
print("initial tree , inorder traversal is")
b.dfs_traversal()
b.delete_item(5)
print("after deleting 5 from the tree , tree becomes : ")
b.dfs_traversal()
# easy case works fine.
