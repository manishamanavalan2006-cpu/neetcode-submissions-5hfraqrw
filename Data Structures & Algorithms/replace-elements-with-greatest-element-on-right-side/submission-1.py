class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxvalue=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i]
            arr[i]=maxvalue
            if current>maxvalue:
                maxvalue=current
        return arr
        
            