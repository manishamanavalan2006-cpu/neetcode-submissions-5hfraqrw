class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            nums1=nums[i+1:]
            nums2=nums[:i]
            left=0
            right=0

            for k in nums2:
                left+=k
            for j in nums1:
                right+=j
            
            if right==left:
                return i
        return -1
