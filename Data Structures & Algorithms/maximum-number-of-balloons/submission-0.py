class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        listvalue=[]

        for i in text:
            if i in "balloon":
                freq[i]=freq.get(i,0)+1
                
        if len(freq)<5:
            return 0
        
        freq2={"b":1,"a":1,"l":2,"o":2,"n":1}
        
        for keys,values in freq2.items():
            data1=freq[keys]
            output=data1//values
            listvalue.append(output) 

        return min(listvalue)
