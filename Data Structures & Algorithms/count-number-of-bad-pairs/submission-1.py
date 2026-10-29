class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        

        freq={}
        goodpair=0
        
        for i,num in enumerate(nums):
            value=num-i

            goodpair+=freq.get(value,0)
            freq[value]=freq.get(value,0)+1
        total=len(nums)*(len(nums)-1)//2
        return total-goodpair
