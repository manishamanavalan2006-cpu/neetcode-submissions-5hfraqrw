class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #burzt force
        '''value=set()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        output=[nums[i],nums[j],nums[k]]
                        value.add(tuple(output))
        return [list(i) for i in value]'''

        #better way
        '''for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                data=-(nums[i]+nums[j])
                if data in nums[j+1:]:
                        output=(nums[i],nums[j],data)
                        value.add(output)
        return [] if len(value)==0 else list(x for x in value)'''

        #optimal way
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1

                elif total<0:
                    left+=1
                else:
                    right-=1
        return result




              

                