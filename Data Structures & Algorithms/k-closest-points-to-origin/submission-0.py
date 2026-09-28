class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data=[]
        for i in points:
            x=i[0]
            y=i[1]

            distance=x*x+y*y
            data.append([distance,i])
        data.sort(key=lambda x:x[0])
        output=[]
        for i in range(k):
            output.append(data[i][1])
        return output
        