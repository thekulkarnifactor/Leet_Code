class Solution:
    def numSpecial(self, mat):
        m = len(mat)
        n = len(mat[0])
        row_sum = [0] * m
        col_sum = [0] * n
        count = 0

        # Calculate the sums of row and column 
        for i in range(m):
            for j in range(n):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]

        # Check for Special Positions in a Binary Matrix
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    count += 1

        return count