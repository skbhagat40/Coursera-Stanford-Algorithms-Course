Bitwise Operators -
Operate on Binary numbers
&(And) |(Or) ^(XOR) ~(Compliment)

XOR is 1 when the two bits are different.

Identities - a^a = 0, a^0 = a, a^b = b^a. a^b^c = c^b^a

if a^b = k, b = k^a.

Other Bitwise Operations - <<(left shift - multiply by 2. After Overflow Becomes 0.) and >>(right shift - divide by 2)

Application - Check if ith bit is set.
Take & with number having ith bit set.
```
return N & (0<<i)
```

Implement sizeof operator
Keep left shifting until it overflows.
logN time complexity.
```
size = 0
while num != 0:
    size += 1
    num << 1
```

Find the element which occurs once in the array.(If there is only one such element.)
```
Take xor of all elements in the array. The other elements will cancel out.
```

Find the element which occurs once in the array.(If there are two such elements. a and b) - 
1. Take XOR of the whole array.
2. The result will be XOR of a and b. XOR of two numbers is set at the place where the bits differ.
Find the position of the bit set in a^b. let it be i.
3. Make two sets of number based on the ith bit. a and b will lie in different sets.
4. return xor of set1, set2.
```
res = reduce(lambda a,b: a^b, arr[:])
p = 0
while ! res & (res << i){
    p+= 1
}
xor1, xor2 = 0, 0
for el in arr:
    if el & 1<<p:
        xor1 ^= el
    else:
        xor2 ^= el
return xor1,xor2
```

Given an array find a pair which gives minimum xor.

Intution - XOR reflects the difference between two numbers a^a = 0.
sort the array. take xor of consecutive elements and keep updating the array.(Kaden's Algo.)

** Given an array find sum of hamming distance of all possible pairs. **
hd(101,100) = 2.
Intution - same approach as sum of all possible submatrices question. use the **Contribution** of an element.
contribution of ith bit = 2 * (no. of elements having set bits at ith position) *  (no. of elements having unset bits at ith position)
```
for i in range(32):
    count0, count1 = 0, 0
    for i,el in enumerate(arr):
        if (el & (0<<i)):
            count0 += 1
        else:
            count1 += 1
    ans += 2 * count0 * count1
```