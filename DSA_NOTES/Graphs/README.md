Types of Graphs - 
1. Directed / Undirected
2. Weighted / Unweighted
3. Cyclic / Acyclic

Considering Simple Graphs (a. No self loops b. No parallel edges)

Max no. of edges = n*(n-1)/2 or nC2
Least no. of edges to be connected = N - 1
N-1 edges doesn't mean connected. Cycles can use it up.
Connectedness of Directed Graphs - No. of SCCS. (SCC - either cycle or single node)

Graph Representations - 1. Set O(V + E) 2. Adjecency list O(V + E) 3. Adjecency matrix O(N^2)

Child Lookup 1. O(E) 2. O(E) 3. O(N)
Check for edge - 1. O(E) 2. O(E) 3. O(1) b/w 2 nodes
List all adjecent nodes - 1. O(E) 2. O(1) 3. O(N)

Problems - 

1. Find the land masses - (DFS and mark as visited, increase the count.)
2. Find the islands - DFS if meet boundary - discard. 
   Another approach - DFS from all boundary (pass 1). Count islands in pass 2.  