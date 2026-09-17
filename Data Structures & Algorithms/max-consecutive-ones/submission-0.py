class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        value=0
        output=[]
        for i in nums:
            if i==1:
                value+=1
            else:
                output.append(value)
                value=0
        output.append(value)
        return max(output)
        

