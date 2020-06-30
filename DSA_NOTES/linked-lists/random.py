def maxone(self, A, B):                          
	    count = 0                               [ 1, 0, 0, 0,   0, 0, 1, 0, 1, 1 ]
	    maxCount = -1                           B = 1
	    indices = set()                         i = 2 , j = 2 indices = {2}
	    res = []                                count =  2  maxLen = 3 incdices = [0 3]
	    i = j = 0
	    while j < len(A):
	        if A[j] == 1:
	            count += 1
	            j += 1
	        else:
	            if B > 0:
	                count += 1
	                indices.add(j)
	                j += 1
	                B -= 1
	            else:
	                while B == 0:
	                    if i == j:
	                        break
	                    if i in indices:
	                        B += 1
	                        indices.remove(i)
	                    i += 1
	                    count -= 1
	               # print('after',i,j, count)
	                if i == j:
	                    i += 1
	                    j += 1
	                elif A[i] == 0:
	                    i += 1
	        if count > maxCount:
	            maxCount = count
	            res = [i, j]
	    return list(range(res[0], res[1]))