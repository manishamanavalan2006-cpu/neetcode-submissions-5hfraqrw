class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        output=[]
        freq={}
        
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for keys,values in freq.items():
            if values==1:
                output.append(keys)
        
        if k<=len(output):
            return output[k-1]
        else:
            return ""