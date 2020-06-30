Linked Lists - contains of nodes.
Each node has Two parts - value and next-pointer.
Advantage over array - Ease of insertion and deletion.
Disadvantage - Random access, cache unfriendly, using extra memory for pointers.

Initialization of a linked list - 
1. Create a ListNode using new. Need to mantain a head pointer. If head is None make it head, else we have two choices -
                                                      1. Make it new head
                                                      2. Append it to the last. (Merging Two Linked lists in reverse order).
    Ideally the initialization logic should be placed in the constructor. (of class LinkedList)

Operations - 

1. Insert / Delete at Kth position.
2. Len / Print the linked list.

Problems - 
1. Finding Length of the linked list.

Approach 1. Iterative Approach.
```
len = 0
current = head # Important to not loose the head.
while current:
    current = current.next
    len += 1
```

2. Printing the linked list
   
Approach 1. Iterative Approach.
```
current = head
while current
    print(current)
    current = current.next
```

Approach 2. Recursive Approach
```
def printLL(head):
    if head is None:
        return
    print(head)
    printLL(head.next) # somewhat similar to tail recursion.
```
3. Print Linked List in reverse order

Approach 1. Iterative Approach using stack
Approach 2. Using Recursion

General Template for permforming some action starting from the end using recursion
```
def reverseOperation(head):
    if head is None:
        return
    reverseOperation(head.next)
    # do the operation here
```
4. Kth node from the end of the linked list.
Approach 1. Iterate till the end. Find the len. index from the start is len-k

Approach 2. use recursion pass on the len. (Keep it passing. somewhat similar to reverse the linked list. maintaining the head of the rest and passing it down the line.)

Approach 3. Make a window of size K, keep sliding it, when it reaches the end, answer will be the left pointer.

5. Mid of the Linked List.
Approach 1.  find the len and then use sliding window.
Approach 2. Tortoise and hare algo. i.e. using slow and fast pointers.
```
slow = fast = head
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
```
when fast reaches the end, slow reaches the mid.

6. Reverse the Linked List.

Approach 1. Using Stack
Approach 2. Using Recursion.
Approach 3. Using prev current and next

Approach 2. Using Recursion
# use the template for performing the reverse operation.
```
    rest = reverseLL(head.next)
    head.next.next = head
    head.next = null
    return rest # we are preserving the rest
```

Approach 3. 
```
prev = null
curr = head
while curr is not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
```

7. Reverse only K nodes of a linked list.
Approach - Using recursion.
Observation - can mantain a count for nodes reversed. After reversing K nodes, prev is the head and head points to the intersection and the forward pointer is the previous of the next recursion.
# using forward recursion in this case.

```
def revK(head, k):
    if head is None:
        return head # this will be our last head.
    current = head
    count = 0
    prev = None
    while current is not None and count < K:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head.next = revK(current)
    return prev
```

8. Spiral List

9. Merge Linked list => 4 pointers p q head current and move them respectively.

10. Hard Copy of Linked List with random pointers.

Approach 1. Using Hash Map

Store the original Node and created node in the map and add the random pointers.

Approach 2. 
Linked List without using extra space.

Each time we create a new node, we do 
originalNode.next = newNode.
originalNode.next.random = originalNode.random.next
originalNode = originalNode.next.next

Now in the next traversal, we do 

we remove the connection between original node and new nodes.


Basic operations in linked list are - Finding the mid, reversing, merging. Applications - Palindrome, Spiral Order etc..