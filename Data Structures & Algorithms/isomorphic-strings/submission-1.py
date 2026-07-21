class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        freq1={}
        freq2={}
        for i in range(len(s)):
            if s[i] in freq1:
                if freq1[s[i]]!=t[i]:
                    return False
            else:
                freq1[s[i]]=t[i]

            if t[i] in freq2:
                if freq2[t[i]]!=s[i]:
                    return False
            else:
                freq2[t[i]]=s[i]
        return True