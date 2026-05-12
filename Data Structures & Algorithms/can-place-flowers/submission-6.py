class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        values=[0]+flowerbed+[0]
        i=1
       
        while i<len(values)-1 and n!=0:
            if values[i-1]==0 and values[i]==0 and values[i+1]==0:
                values[i]=1
                n-=1
            i+=1
        return n==0