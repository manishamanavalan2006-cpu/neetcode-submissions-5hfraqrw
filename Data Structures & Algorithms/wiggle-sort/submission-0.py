class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n=len(nums)-1
        mid=n//2
        high=n

        result=[0]*len(nums)

        for i in range(0,len(nums),2):
            data=nums[mid]
            result[i]=data
            mid-=1
        
        for j in range(1,len(nums),2):
            data=nums[high]
            result[j]=data
            high-=1

        nums[:]=result
        
