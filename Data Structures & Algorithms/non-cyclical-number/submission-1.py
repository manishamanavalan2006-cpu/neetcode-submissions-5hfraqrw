class Solution:
    def isHappy(self, n: int) -> bool:
        #Floyd Cycle Detection Version
        
        #optimal way
        slow=n
        fast=self.sumsquare(n)
        while fast!=1 and slow!=fast:
            slow=self.sumsquare(slow)
            fast=self.sumsquare(self.sumsquare(fast))
        return fast==1
    def sumsquare(self,n):
        output=0
        while n:
            digits=n%10
            output+=digits**2
            n//=10
        return output
    