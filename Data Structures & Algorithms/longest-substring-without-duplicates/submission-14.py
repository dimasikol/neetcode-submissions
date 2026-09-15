class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in data: 
                l = max(data.pop(s[r])+1,l)
            data[s[r]] = r
            res = max(res,r-l+1)
        return res
