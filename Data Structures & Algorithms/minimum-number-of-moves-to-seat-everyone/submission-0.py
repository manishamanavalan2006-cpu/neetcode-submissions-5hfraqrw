class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans=0
         
        if len(seats)!=len(students):
            return 0
        
        for i in range(0,len(students)):
            value=abs(students[i]-seats[i])
            ans+=value
        return ans