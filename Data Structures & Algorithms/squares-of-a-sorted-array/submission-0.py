class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        output=[]
        for i in nums:
            output.append(abs(i)*abs(i))
        output.sort()
        return output