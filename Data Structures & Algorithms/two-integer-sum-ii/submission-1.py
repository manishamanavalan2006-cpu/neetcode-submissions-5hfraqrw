class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=0
        for i in range(len(numbers)):
            output=target-numbers[i]
            if output  in numbers:
                value=numbers.index(output)
                return [i+1,value+1]
        return []
