class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq={}
        result=[]
        for i in nums:
            freq[i]=freq.get(i, 0)+1
        for j in freq.keys():
            if freq[j]==1:
               result.append(j)
        return result