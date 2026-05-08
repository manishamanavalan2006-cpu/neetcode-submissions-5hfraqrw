class Solution:
    def isHappy(self, n: int) -> bool:
        hashset=set()
        while n not in hashset:
            hashset.add(n)
            n=self.sumSquare(n)
            if n==1:
                return True
        return False
    def sumSquare(self,n):
        output=0
        while n:
            digits=n%10
            output+=(digits**2)
            n=n//10
        return output