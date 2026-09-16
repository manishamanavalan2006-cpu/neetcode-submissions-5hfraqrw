class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        output=[]
        freq={}

        for i in words[0]:
            freq[i]=freq.get(i,0)+1
        

        for j in words[1:]:
            temp={}

            for k in j:
                temp[k]=temp.get(k,0)+1
            
            for ch in freq:
                freq[ch]=min(freq[ch],temp.get(ch,0))
        
        for ch in freq:
            for j in range(freq[ch]):
                output.append(ch)
        return output


