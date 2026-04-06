class Solution:
    def longestPalindrome(self, s: str) -> str:
        output_string=""
        for i in range(len(s)):
            left=i
            right=i
            while(left>=0) and (right<len(s)) and s[right]==s[left]:
                if (right-left+1)>len(output_string):
                    output_string=s[left:right+1]
                left-=1
                right+=1
            left=i
            right=i+1
            while(left>=0) and (right<len(s)) and s[right]==s[left]:
                if (right-left+1)>len(output_string):
                    output_string=s[left:right+1]
                left-=1
                right+=1
        return output_string