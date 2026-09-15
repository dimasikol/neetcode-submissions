class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            if (target - nums[i]) in data:
                return [data[(target - nums[i])],i]
            else:
                data[nums[i]] = i
