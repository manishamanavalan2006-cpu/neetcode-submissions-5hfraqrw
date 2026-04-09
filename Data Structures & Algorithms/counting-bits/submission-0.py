class Solution:
    def countBits(self, n: int) -> List[int]:
        count=[0]
        
        for i in range(1,n+1):
            b=0
            while i>=1:
                remainder=i%2
                i//=2
                if remainder==1:
                    b+=1
            count.append(b)
        return count
            