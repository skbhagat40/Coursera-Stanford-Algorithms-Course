class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        from collections import defaultdict
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b, a%b)
        lines = defaultdict(int)
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                x1,y1 = A[i],B[i]
                x2,y2 = A[j],B[j]
                if x2 == x1:
                    lines[float('inf'),x1] += 1
                    continue
                elif y2!=y1 and x2 - x1 != 0:
                    m = (y2-y1)/(x2-x1)
                    c = y2 - m*x2
                    g = gcd(y2-y1,x2-x1)
                    lines[(((y2-y1)//g, (x2-x1)//g),c)] += 1
                elif x2-x1 != 0:
                    m = (y2-y1)/(x2-x1)
                    c = y2 - m*x2
                    lines[0,c] += 1
        print(lines)
        # next go to all the points and check wheather they fit in this equation or not
        for p in range(len(A)):
            for line in lines:
                x,y = A[p],B[p]
                if line[0] == float('inf'):
                    # print('here')
                    if y==line[1]:
                        lines[line] += 1
                        continue
                    continue
                elif line[0] != float('inf') and y == (line[0][0]/line[0][1])*x + line[1]:
                    # print('here')
                    lines[line] += 1
        # print(lines)
        return max(lines.values())
            
s = Solution()
A = [ 6, -7, 5, 9, -9, -7 ]
B = [ 7, 5, 5, 9, -8, 2 ]
s.solve(A,B)