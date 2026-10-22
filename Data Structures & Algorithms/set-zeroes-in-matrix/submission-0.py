class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n=len(matrix)
        rows=[0]*n
        columns=[0]*len(matrix[0])

        for i in range(n):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==0:
                    rows[i]=1
                    columns[j]=1
        
        for i in range(n):
            for j in range(len(matrix[0])):
                if rows[i]==1 or columns[j]==1:
                    matrix[i][j]=0
        