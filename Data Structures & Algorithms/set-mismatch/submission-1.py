class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq={}

        for i in nums:
            freq[i]=freq.get(i,0)+1
        

        for i in range(1,n+1):
            if i not in freq:
                value=i
            if freq.get(i,0)>=2:
                duplicate=i
        return [duplicate,value]