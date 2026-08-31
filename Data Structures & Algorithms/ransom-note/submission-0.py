class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        freq1={}
        freq2={}

        for i in ransomNote:
            freq1[i]=freq1.get(i,0)+1
        for j in magazine:
            freq2[j]=freq2.get(j,0)+1

        for keys in freq1.keys():
            if keys not in freq2:
                return False
            if freq1[keys]>freq2[keys]:
                return False
        return True