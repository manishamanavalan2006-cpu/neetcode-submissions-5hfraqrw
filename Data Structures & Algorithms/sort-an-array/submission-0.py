class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            value=nums[i]
            j=i-1
            while j>=0 and nums[j]>value:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=value
        return nums