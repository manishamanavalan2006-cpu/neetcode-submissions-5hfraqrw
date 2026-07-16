class Solution:
    def maxDifference(self, s: str) -> int:

        freq = {}

        # Count frequencies
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        maxOdd = -1
        minEven = float('inf')

        for count in freq.values():
            if count % 2 == 1:
                maxOdd = max(maxOdd, count)
            else:
                minEven = min(minEven, count)

        return maxOdd - minEven