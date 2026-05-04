class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(0,len(prices)):
            buydata=prices[i]
            for j in range(i+1,len(prices)):
                if buydata<prices[j]:
                    value=prices[j]-buydata
                    profit=max(profit,value)
        return profit