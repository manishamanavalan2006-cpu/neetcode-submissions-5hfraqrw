class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]#transpose
        
        for k in range(n):
            left=0
            right=n-1

            while left<right:
                matrix[k][left],matrix[k][right]=matrix[k][right],matrix[k][left]
                left+=1
                right-=1
                

