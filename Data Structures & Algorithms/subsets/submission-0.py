class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_subset=[[]]

        for i in nums:
            temp=[]
            for j in final_subset:
                newdata=j+[i]
                temp.append(newdata)
            final_subset+=temp
        return final_subset
