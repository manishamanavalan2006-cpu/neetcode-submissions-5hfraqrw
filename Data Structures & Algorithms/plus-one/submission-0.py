class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value=""
        for i in digits:
            value+=str(i)
        output=int(value)+1
        list_1=[]
        for j in str(output):
            list_1.append(int(j))
        return list_1
        
