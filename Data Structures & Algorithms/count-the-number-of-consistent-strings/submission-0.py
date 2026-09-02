class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count=0
        for i in words:
            output=""
            value=True
            for j in i:
                if j not in output and j in allowed:
                    output+=j
                elif j in allowed:
                    continue
                else:
                    value=False
                    break
            if value:
                count+=1
        return count
            

                    
                    
