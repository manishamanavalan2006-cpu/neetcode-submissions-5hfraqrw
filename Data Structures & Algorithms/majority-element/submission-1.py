class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_A={}
        for i in range(len(nums)):
            if nums[i] not in dict_A:
                dict_A[nums[i]]=1
            else:
                dict_A[nums[i]]+=1
        sorted_value=dict(sorted(dict_A.items(),key=lambda x:x[1],reverse=True))
        print(sorted_value)
        for key in sorted_value:
            return key 