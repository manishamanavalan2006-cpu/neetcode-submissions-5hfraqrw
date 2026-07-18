class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=x
        value=""
        if x==0:
            return True
        elif x<0:
            return False
        while x!=0:
            rem=x%10
            value+=str(rem)
            x//=10
        return original==int(value)