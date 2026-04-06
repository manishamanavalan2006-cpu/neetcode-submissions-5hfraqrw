class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            index_value=nums.index(target)
            return index_value
        return -1
    