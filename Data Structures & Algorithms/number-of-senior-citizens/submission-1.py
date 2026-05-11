class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details:
            value=int(i[11:13])
       
            if value>60:
                count+=1
        return count