class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_a={}
        for i in nums:
            dict_a[i]=dict_a.get(i,0)+1
        sorted_values=sorted(dict_a,key=lambda x:dict_a[x],reverse=True)
        values=sorted_values[:k]
        return values
