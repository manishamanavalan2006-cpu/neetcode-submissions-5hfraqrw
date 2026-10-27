class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k=k%len(nums)
        if k==0:
            return
        temparr=nums[-k:]+nums[:-k]

        for i in range(0,len(nums)):
            nums[i]=temparr[i]