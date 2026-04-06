class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        n=len(nums)
        total=(n*(n+1)//2) 
        for i in range (0, n):
            total-=nums[i]
        return total