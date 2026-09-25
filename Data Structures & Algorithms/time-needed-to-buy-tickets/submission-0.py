class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        value=tickets[k]
        time=0
        for i in range(len(tickets)):
            if i<=k:
                time+=min(tickets[i],value)
            else:
                time+=min(tickets[i],value-1)
        return time