class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        for i in range(m):
            for k in range(n):
                if matrix[i][k] == 0:
                    ans.append([i,k])
        for an in ans:
            a,b = an
            for j in range(n):
                matrix[a][j] = 0
            for z in range(m):
                matrix[z][b] = 0
