class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        
        ans=""

        for j in order:
            if j in freq:
                value=freq[j]*j
                freq[j]=0
                ans+=value
        
        for key, value in freq.items():
            if value!=0:
                data=key*value
                ans+=data
        return ans