class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        value=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                result+=nums[i]
                
            else:
                value=max(result,value)
                result=nums[i]
        value=max(value,result)
        return value