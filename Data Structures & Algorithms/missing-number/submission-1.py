class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''for i in range(0,len(nums) + 1):
            flag=False
            for j in range(0,len(nums)):
                if i==nums[j]:
                    flag=True
                    break
            if flag!=True:
                return i 
        return 0'''
        n=len(nums)
        total_Sum=int(((n**2)/2)+(n/2))
        for i in range(0,len(nums)):
            total_Sum-=nums[i]
        return total_Sum
