class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        result=-1

        for i in arr:
            freq[i]=freq.get(i,0)+1
        
        for keys,values in freq.items():
            if values==keys:
                result=max(result,values)
        return result