class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=list(s.split())
        value=len(arr[-1])
        return value