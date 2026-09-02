class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        count=0
        freq={}
        for i in chars:
            freq[i]=freq.get(i,0)+1
        
        for i in words:
            wordsfreq={}
            for j in i:
                wordsfreq[j]=wordsfreq.get(j,0)+1
            
            result=True

            for keys in wordsfreq.keys():
                if keys not in freq or wordsfreq[keys]>freq[keys]:
                    result=False
                    break
            if result:
                count+=len(i)
        return count


            
        
