class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        

        for i in range(1,len(nums)):
            value=nums[i]%2!=0
            value1=nums[i-1]%2!=0
            if not(value^value1):
                return False
        return True
