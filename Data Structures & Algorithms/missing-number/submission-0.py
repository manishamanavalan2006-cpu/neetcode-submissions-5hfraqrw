class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0,len(nums) + 1):
            flag=False
            for j in range(0,len(nums)):
                if i==nums[j]:
                    flag=True
                    break
            if flag!=True:
                return i 
        return 0
