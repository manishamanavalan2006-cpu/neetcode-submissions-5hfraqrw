class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        output=0
       
        for i in s:
            freq[i]=freq.get(i,0)+1
            if freq[i]%2==0:
                output+=2
        
        for values in freq.values():
            if values%2:
                output+=1
                break
        return output