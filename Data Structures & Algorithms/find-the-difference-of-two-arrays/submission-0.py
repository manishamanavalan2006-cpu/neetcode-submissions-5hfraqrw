class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1=[]
        ans2=[]
       
        for i in nums1:
            if i not in nums2 and i not in ans1:
                ans1.append(i)
        
        for j in nums2:
            if j not in nums1 and j not in ans2:
                ans2.append(j)
        
        return [ans1,ans2]
        