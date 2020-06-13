class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        self.A = A
        self.ans = []
        self.columns = [-1]*A
        res = self.backtrack(0,0,0,0)
        print(res, 'res')
        print(self.ans)
        return self.ans
        # recursion will only happen till all possiblites in the last row is exhausted.
        # need a way to keep track of the queens placed till now, that will be our columns array.
        # columns array need to be outside of the recursion stack to stop it from re-initializing every time.
    
    def isPossible(self,row_number, col_number, i,j):
        A = self.A
        if j > A-1:
            return False
        if i > A-1:
            return False
        # print('columns', self.columns, row_number, col_number)
        if i == 0 and j == 0:
            return True
        for c in range(j+1):
            if self.columns[c] == j:
                print('22 ret false', self.columns, c)
                return False
            if row_number + col_number == i+j or abs(row_number-col_number) == abs(i-j):
                print('25 ret false', self.columns)
                return False
        return True
    
    def backtrack(self, row_number, col_number, curr_row, curr_col):
        print('rc', curr_row, curr_col)
        A = self.A
        # need an argument to keep track of row number. row position will be mantained by the columns array.
        if row_number == A-1 and self.isPossible(row_number, col_number, curr_row, curr_col):
            print('**'*20)
            self.ans.append(self.columns)
        # do step and explore other possiblities.
        print('is pos', self.isPossible(row_number, col_number, curr_row, curr_col))
        if self.isPossible(row_number, col_number, curr_row, curr_col):
            if curr_row > A-1:
                return False
            if curr_col > A-1:
                return False
            self.columns[curr_row] = curr_col
            # print('here')
            self.backtrack(row_number, col_number, curr_row + 1, 0)
        else:
            for i in range(1,A):
                if curr_row > A-1:
                    return False
                if curr_col > A-1:
                    return False
                self.columns[curr_row] = curr_col
                self.backtrack(row_number, col_number, curr_row, curr_col + i)
            # if curr_row > A-1:
            #     return False
            # if curr_col > A-1:
            #     return False
            # self.columns[curr_row] = curr_col
            # print('here down'*3)
            # self.backtrack(row_number, col_number, curr_row, curr_col + 1)