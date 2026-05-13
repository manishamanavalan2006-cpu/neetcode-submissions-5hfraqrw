class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp=[]
        for i in nums:
            if i==val:
                continue
            temp.append(i)
        for j in range(len(temp)):
            nums[j]=temp[j]
        return len(temp)