class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1==s2:
            return True
        
        count=0

        for i in range(len(s1)):
            if s1[i] in s2:
                if s1[i]!=s2[i]:
                    count+=1
                    if count>2:
                        return False
            else:
                return False
        if count==1:
            return False
        return True
            
