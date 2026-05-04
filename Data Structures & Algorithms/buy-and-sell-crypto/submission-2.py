class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''profit=0
        for i in range(0,len(prices)):
            buydata=prices[i]
            for j in range(i+1,len(prices)):
                if buydata<prices[j]:
                    value=prices[j]-buydata
                    profit=max(profit,value)
        return profit'''

        #optimal soultion

        min_price=float('inf')
        max_profit=0
        for price in prices:
            min_price=min(price,min_price)
            price=price-min_price
            max_profit=max(price,max_profit)
        return max_profit
