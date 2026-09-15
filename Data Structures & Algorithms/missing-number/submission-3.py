class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        summer = 0
        for i in range(len(nums)):
            res+=nums[i]
            summer+=i
        return summer - res + len(nums)