class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s=s.split(" ")
        freq1={}
        freq2={}

        if len(s)!=len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in freq1:
                freq1[pattern[i]]=s[i]
            else:
                if freq1[pattern[i]]!=s[i]:
                    return False

        
        for i in range(len(s)):
            if s[i] not in freq2:
                freq2[s[i]]=pattern[i]
            else:
                if freq2[s[i]]!=pattern[i]:
                    return False
        return True
   