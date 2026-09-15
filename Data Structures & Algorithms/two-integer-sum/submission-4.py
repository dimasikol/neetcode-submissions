class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            d = target - nums[i] 
            if d in data:
                return [data[d],i]
            else:
                data[nums[i]] = i
        return [0,1]