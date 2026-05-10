class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        value=set()
        '''for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        output=[nums[i],nums[j],nums[k]]
                        value.add(tuple(output))
        return [list(i) for i in value]'''

        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                data=-(nums[i]+nums[j])
                if data in nums[j+1:]:
                        output=(nums[i],nums[j],data)
                        value.add(output)
        return [] if len(value)==0 else list(x for x in value)

                
                