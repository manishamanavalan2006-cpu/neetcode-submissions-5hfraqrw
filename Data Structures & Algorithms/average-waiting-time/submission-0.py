class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting=0
        start=0
        for i in range(len(customers)):
            arrival=customers[i][0]
            cookingtime=customers[i][1]
            finishtime=max(start,arrival)+cookingtime
            waiting+=finishtime-arrival
            start=finishtime
        return waiting/len(customers)