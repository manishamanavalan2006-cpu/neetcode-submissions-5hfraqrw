class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table={}
        for i,nums in enumerate(nums):
            complement=target-nums
            if complement in hash_table:
                return [hash_table[complement],i]
            hash_table[nums]=i
       
        