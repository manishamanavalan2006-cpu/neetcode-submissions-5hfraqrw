class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
        return count'''

        hashmap={}
        count=0
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=1
            else:
                count+=hashmap[nums[i]]
                hashmap[nums[i]]+=1
    
        return count

 









