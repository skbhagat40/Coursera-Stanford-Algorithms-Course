DSU - Union Find / Disjoint Set Union

Need to perform following operations in an efficient manner - 1. Find 2. Union 3. Rank

Possible approaches - 

1. Use a set 2. Mapping

1. Set - A hash map of set vs list of items. i.e. A - {1, 2, 3}, B - {4, 5, 6}
2. Mapping - Map each node to it's corres. category.

Time complexities - 
  1. Set Approach - all O(n)
  2. Mapping approach - O(1) O(1) O(n) (find , rank , union)
  
Let's try to optimize the union in the Second One by being lazy.
For the operation a U b. we create a lazy link from a to b, saying the category of a is same as of b.

Find Becomes the crucial operation. TC of find is O(n). 

Optimizing find - Whenever we find the category of a, we branch off all the intermediate nodes in the path.
Optimizing union - Make the tree having smaller size(good enough proxy for height) the child.
Constant amortized TC. Worst case TC O(logn).

Inc. the size on union, only when the two roots are different.

Implementation Note - In the start each node as it's own category with size 1.

If the nodes are not known beforehand, use a hash map. If a node is not present in the map, it's the category. 
Same for the size. If the size is not present , the size is 1.

Applications of DSU - 1. MST using Kruskul's algo - 
