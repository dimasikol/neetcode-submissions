class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        result = 0
        for i in res:
            m = 1
            l = -1
            r = 1
            while (i+l) in res:
                m+=1
                l-=1
            while (i+r) in res:
                m+=1
                r+=1
            result = max(result,m)
        return result