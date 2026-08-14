class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        oddlist=[]
        evenlist=[]

        for i in nums:
            if i%2==0:
                evenlist.append(i)
            else:
                oddlist.append(i)
        oddlist.sort()
        evenlist.sort()

        return evenlist+oddlist