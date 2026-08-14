class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        outputlist=[]
        for i in arr2:
            count=arr1.count(i)

            for j in range(count):
                outputlist.append(i)
                arr1.remove(i)
        
        arr1.sort()
        return outputlist+arr1