class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        freq={0:1}
        count=0
        prefix=0

        for i in nums:
            if i%2!=0:
                prefix+=1

            required=prefix-k
            count+=freq.get(required,0)
            freq[prefix]=freq.get(prefix,0)+1
        return count
        
        
