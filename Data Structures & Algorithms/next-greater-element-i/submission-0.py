class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
        outputlist=[]
        for i in range(len(nums1)):
            indexes=nums2.index(nums1[i])
            found=False
            for j in range(indexes+1,len(nums2)):
                if nums1[i]<nums2[j]:
                    outputlist.append(nums2[j])
                    found=True
                    break
            if not found:
                outputlist.append(-1)
                    
        return outputlist














        