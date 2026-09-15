class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(numbers)):
            res[target-numbers[i]] = i
            if numbers[i] in res and target!=2*numbers[i]:
                return [res[numbers[i]]+1,i+1]
            