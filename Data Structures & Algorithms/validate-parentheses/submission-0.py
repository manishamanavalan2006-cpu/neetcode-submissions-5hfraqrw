class Solution:
    def isValid(self, s: str) -> bool:
        dict_a={"{":"}","[":"]","(":")"}
        stack=[]
        for i in s:
            if i in dict_a.keys():
                stack.append(i)
            else:
                if stack==[]:
                    return False
                else:
                    if dict_a[stack[-1]]==i:
                        stack.pop()
                    else:
                        return False
        if stack==[]:
            return True
        else:
            return False