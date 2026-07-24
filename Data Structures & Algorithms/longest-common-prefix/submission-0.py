class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        output=""
        for i in range(len(first)):
            chr=first[i]
           
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=chr:
                    return output
            output+=chr
        return output