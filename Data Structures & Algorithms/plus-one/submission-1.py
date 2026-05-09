class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''value=""
        for i in digits:
            value+=str(i)
        output=int(value)+1
        list_1=[]
        for j in str(output):
            list_1.append(int(j))
        return list_1'''

        #optimized code
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0

        return [1]+digits
        
