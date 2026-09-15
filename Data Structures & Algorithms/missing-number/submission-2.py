class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = set()
        for i in range(len(nums)):
            res.add(nums[i])
        for i in range(len(nums)+1):
            if not( i in res):
                return i