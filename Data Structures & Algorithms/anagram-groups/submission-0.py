class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            dict_a={}
            for i in range(0,len(strs)):
                a=str((sorted(strs[i])))
                if a not in dict_a:
                    dict_a[a]=[strs[i]]
                else:
                    dict_a[a].append(strs[i])
            return list(dict_a.values())
          