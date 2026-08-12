class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq={}
        listes=[]

        for i in nums:
            freq[i]=freq.get(i,0)+1
        

        mydict=dict(sorted(freq.items(), key=lambda x:(x[1],-x[0])))

        for values,frequency in mydict.items():
            listes.extend([values]*frequency)
        return listes

        