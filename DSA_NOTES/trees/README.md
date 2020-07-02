







# Important questions

1. Recover Tree from pre-order(top-down) and in-order traversal. (Homework Question)
   Important concept used - 
   """
   In the recursion insead of passing the root node, we 
   pass the root node index and left and right ranges. we build the root node from the node_idx, make left and right associations, and return the triplet - root_idx,l,r.
   Unlike the previous question, where we were returning the root and the left and right ranges.
   another imp. point was to check for empty subtree.
   """