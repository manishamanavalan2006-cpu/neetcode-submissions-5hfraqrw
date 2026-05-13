class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''temp=[]
        for i in nums:
            if i==val:
                continue
            temp.append(i)
        for j in range(len(temp)):
            nums[j]=temp[j]
        return len(temp)'''
        r=0
        l=0
        while r<len(nums):
            if nums[r]==val:
                r+=1
            else:
                nums[l]=nums[r]
                l+=1
                r+=1
        return l

        