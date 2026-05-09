class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=0
        for i in range(len(numbers)):
            output=target-numbers[i]
            if output  in numbers[i+1:]:
                value=numbers[i+1:].index(output)+1+i
                return [i+1,value+1]
        return []
