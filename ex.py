def s(A):
    if len(str(A)) == 1:
        return A == 1
    return s(sum([int(x) for x in str(A)]))
print(s(1234))

def s1(A):
    return A == 1 if len(str(A)) == 1 else s1(sum([int(x) for x in str(A)]))
# print(s1(12341))

def total_ways(A,c):
    if A == 1 or A==0:
        return 1
    else:
         return total_ways(A-1,) + total_ways(c+1)
print(total_ways(4,1))