class Solution:
    def arrangeCoins(self, n: int) -> int:
        row=1
        coins=n
        count=0

        while coins>=row:
            coins-=row
            count+=1
            row+=1
        return count
