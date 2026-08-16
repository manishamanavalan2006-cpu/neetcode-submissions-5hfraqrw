class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = {}
        
        for i in words:
            for j in i:
                freq[j] = freq.get(j, 0) + 1
        
        for key, values in freq.items():
            if values % len(words) != 0:
                return False
        
        return True