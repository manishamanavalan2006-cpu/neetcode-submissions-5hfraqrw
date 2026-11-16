class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        value=sentence.split(" ")

        if value[0][0]!=value[-1][-1]:
            return False
        
        for i in range(0,len(value)-1):
            if value[i][-1] != value[i+1][0]:
                return False
        return True