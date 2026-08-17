class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq={}
        missingno=0
        grids=[]
        for i in grid:
            for k in i:
                grids.append(k)
                freq[k]=freq.get(k,0)+1
            
        for key, values in freq.items():
            if values>1:
                missingno=key
        
        for i in range(1,len(grid)*len(grid)+1):
            if i not in freq:
                return [missingno,i]
        







