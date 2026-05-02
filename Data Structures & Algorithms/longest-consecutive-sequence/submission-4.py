class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        long=0
        for i in nums:
            if (i-1) not in nums:
                lenght=1
                while (i+lenght) in nums:
                    lenght+=1
                long=max(lenght,long)
        return long
