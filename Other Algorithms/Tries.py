# here we will try to implement the trie data structure.
'''Trie is used to find wheather a word is in collection of words or not.
It is used for prefix based which dicts can't perform'''


# operations - search,delete,insert
# time complexity - O(l*n) l= averge word length n=no. of words in the trie.
# trie consists of trie nodes , which contain referecn to children i.e. a dict and a boolean field.
# let's do it !

class TrieNode(object):
    def __init__(self, map={}):
        self.map = {}
        self.booleanfield = False

    def __str__(self):
        return str(self.map)


class Trie(object):

    def __init__(self):
        self.root_node = TrieNode()

    def addWord(self, word):
        current = self.root_node
        for el in word:
            print(el)
            node = current.map.get(el, None)
            print("node", node)
            if node is None:
                node = TrieNode()
                current.map[el] = node
            current = node
        current.booleanfield = True

    def searchWord(self, word):
        current = self.root_node
        for c, el in enumerate(word):
            if c == len(word) - 1:
                node = current.map.get(el, None)
                if node is not None:
                    #print("end Node")
                    # end of the word check the boolean field
                    return node.booleanfield
                else:
                    return False
            else:
                node = current.map.get(el, None)
                if node is None:
                    return False
                current = node

    def deleteWord(self, word):
        self.delete_word_helper(self.root_node, word, 0)  # cuurent_node,word,index

    def delete_word_helper(self, current_node, word, index):
        if index == len(word) :  # this is our base case
            #node = current_node.map.get(word[index])
            # if node is None:
            #     return False
            # else:
            #     node.booleanfield = False
            #     return len(node.map.keys()) == 0  # This is and indicator to delete this node or not
            if not current_node.booleanfield:
                return False

            current_node.booleanfield = False
            print(list(current_node.map.values()),"the list",len(current_node.map.values()))
            return len(current_node.map.values())==0
        else:
                node = current_node.map.get(word[index],None)
                if node is None:
                    return False
                should_delete = self.delete_word_helper(node, word, index + 1)
                if should_delete:
                    del current_node.map[word[index]]
                    return len(current_node.map.values()) == 0
                return False


# let's check if trie node works
t = Trie()
t.addWord("shailesh")
t.addWord("sam")
root = t.root_node
print(root.map['s'])
print('checking search for sam', t.searchWord("sam"))
# Trie search Implementation
# search a complete word , iterative implementation
# The search word implementation works! yea ! :)
# Let's try to implement the delete word functionality. So, the idea is as follows -
'''First we are going to find the word. If the node corresponding to the last word is a leaf node we delete that node and if parent node has
no child we delete that too.
In case the Node to be deleted is also the parent for some other node , we set it's boolean field to False'''
print('deleting word sam')
t.deleteWord('sam')
print('checking if sam is deleted or not',t.searchWord('sam'))
print('checking if shailesh still exists',t.searchWord('shailesh'))
print('adding word abc')
t.addWord('abc')
print('searching abc',t.searchWord('abc'))
print(t.root_node)
# cool
# yeah , so it sort of works