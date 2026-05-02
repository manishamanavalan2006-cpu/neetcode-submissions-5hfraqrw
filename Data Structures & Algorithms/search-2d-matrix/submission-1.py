class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])

        left=0
        right=row*col-1

        while left<=right:
            mid=(left+right)//2

            rows=mid//col
            cols=mid%col
            if matrix[rows][cols]==target:
                return True
            elif matrix[rows][cols]<target:
                left=mid+1
            else:
                right=mid-1
        return False