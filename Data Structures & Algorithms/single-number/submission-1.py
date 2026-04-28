class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_a=set()
        for i in range(0, len(nums)):
            if nums[i]in dict_a:
                dict_a.remove(nums[i])
            else:
                dict_a.add(nums[i])
        return list(dict_a)[0]