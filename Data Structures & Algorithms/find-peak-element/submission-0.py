class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        
        if len(nums)==2:
            return nums.index(max(nums))
        
        for i in range(0,len(nums)-2):
            if nums[i+1]>nums[i] and nums[i+1]>nums[i+2]:
                return i+1
        
        if nums[-1]>nums[-2]:
            return len(nums)-1
        return 0