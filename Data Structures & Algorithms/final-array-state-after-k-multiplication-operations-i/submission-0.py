class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):
            indexvalue=nums.index(min(nums))
            nums[indexvalue]*=multiplier
        return nums
        