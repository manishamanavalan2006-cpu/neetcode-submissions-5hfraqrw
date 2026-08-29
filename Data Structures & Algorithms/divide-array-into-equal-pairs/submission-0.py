class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        for keys,values in freq.items():
            if values%2!=0:
                return False
        return True