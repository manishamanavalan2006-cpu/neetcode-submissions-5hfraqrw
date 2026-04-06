class Solution:
   
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_a=set()
        for nums in nums:
            if nums in set_a:
                return True
            set_a.add(nums)
        return False