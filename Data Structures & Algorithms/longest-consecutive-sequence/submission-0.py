class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res= set(nums)
        mx = 0
        for i in res:
            ans = 1
            l = -1
            r = 1
            while (i+l) in res:
                ans+=1
                l-=1
            while (i+r) in res:
                r+=1
                ans+=1
            mx = max(mx,ans)
        return mx