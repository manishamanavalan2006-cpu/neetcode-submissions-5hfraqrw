class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        output_list=[]
        set_a=set()
        while(right<len(s)):
            while s[right] in set_a:
                set_a.remove(s[left])
                left+=1
            set_a.add(s[right])
            output_list.append(right-left+1)
            right+=1
        return 0 if len(output_list)==0 else max(output_list)