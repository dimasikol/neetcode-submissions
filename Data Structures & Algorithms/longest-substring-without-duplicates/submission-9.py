class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        q = dict()
        res = 0
        l=0
        if len(s)!=len(set(s)):
            for i in range(len(s)):
                if s[i] in q:
                    l = max(q[s[i]]+1,l)
                q[s[i]] = i
                res = max(res,i-l+1)
            return res
        else:
            return len(s)