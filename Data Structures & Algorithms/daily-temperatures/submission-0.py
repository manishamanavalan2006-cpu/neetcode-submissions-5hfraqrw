class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        for i in range(len(temperatures)):
            count=1
            j=i+1
            while j<len(temperatures):
                if temperatures[i]<temperatures[j]:
                    count=j-i
                    result[i]+=count
                    break
                else:
                    j+=1
        return result