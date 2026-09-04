class Solution:
    def candy(self, ratings: List[int]) -> int:
        output=[1]*len(ratings)
        #left to right

        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                output[i]=output[i-1]+1
        
        #right to left
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                output[i]=max(output[i],output[i+1]+1)
        sums=0
        for i in output:
            sums+=i
        return sums
     