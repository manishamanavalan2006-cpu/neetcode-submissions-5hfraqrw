class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxindex=0
        for i in range(len(nums)):
            if i<=maxindex:
                maxindex=max(maxindex,i+nums[i])
                if maxindex>=len(nums)-1:
                    return True
        return False