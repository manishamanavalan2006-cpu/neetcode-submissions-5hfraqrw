class Solution:
    def heightChecker(self, heights: List[int]) -> int:
      
        sortedarray=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=sortedarray[i]:
                count+=1
       
        return count
        