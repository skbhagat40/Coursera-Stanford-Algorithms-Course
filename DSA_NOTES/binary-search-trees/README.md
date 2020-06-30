Binary Search Tree needs to satisfy following conditions - 
1. It is a binary tree
2. LST and RST are BST
3. root.val >= max(LST)
4. root.val < max(RST)

Operations on a BST - 

1. Addition of a Node - 
   Try to find the node and add it there.
2. Deletion of Node - 
    case 1/2 : _leaf node or node with only child_ (easy case)
    case 2 : *swap and convert to case 1/2 and then do the deletion*.

Problems - 

1. Check Binary Tree or not - 
    Approach - Brute force - For each node check the conditions individually.
    Optimizations - 
        Take bottom up approach , post order traversal, return max till now at each level.

    *Related Problem* - Largest Size of BST in a BT.
    In this case return triplet = (size, max, min)

2. Size of subtree in BST - HashMap/Pair + post - order traversal.

3. Kth smallest element in BST
   Approach - 
    case 1 size_l = K-1, return the root.
    case 2 size_l > K - 1, traverse left and find kth smallest
    case 3 size_l < K - 1, traverse right and find K - size_l - 1 (th smallest element).