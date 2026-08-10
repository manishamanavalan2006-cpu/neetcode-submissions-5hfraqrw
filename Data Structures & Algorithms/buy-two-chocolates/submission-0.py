class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        minimum=float('inf')
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                sums=prices[i]+prices[j]
                if sums<=money:
                    minimum=min(minimum,sums)

        if minimum==float('inf'): 
            return money
        return money-minimum