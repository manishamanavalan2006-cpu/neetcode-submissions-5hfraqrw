class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq1={}
        freq2={}
        for i in s:
            freq1[i]=freq1.get(i,0)+1
        
        for j in t:
            freq2[j]=freq2.get(j,0)+1
        
        for keys,values in freq2.items():
            if keys not in freq1 or freq2[keys]!=freq1[keys] :
                return keys

