class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)-1):
            value=arr[i]
            slicing=max(arr[i+1:])
            arr[i]=slicing
        arr[-1]=-1
        return arr
        
            