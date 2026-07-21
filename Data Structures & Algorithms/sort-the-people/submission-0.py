class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        freq={}
        output=[]
        k=0
        for i in range(len(names)):
            if heights[i] not in freq:
                freq[heights[i]]=names[i]
        output=sorted(heights,reverse=True)
        for j in output:
            values=freq[j]
            names[k]=values
            k+=1
        return names