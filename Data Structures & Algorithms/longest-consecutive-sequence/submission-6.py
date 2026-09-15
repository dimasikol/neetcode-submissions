class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        mx = 0
        while sets:
            count = 1
            i = sets.pop()
            cur = i
            while (cur-1) in sets:
                sets.remove((cur-1))
                cur-=1
                count+=1
            cur = i
            while (cur+1) in sets:
                sets.remove((cur+1))
                cur+=1
                count+=1
            mx = max(count,mx)
        return mx