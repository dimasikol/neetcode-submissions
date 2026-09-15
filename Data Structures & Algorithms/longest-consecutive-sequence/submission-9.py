
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        dd = {}
        mx = 0
        while d:
            cur = d.pop()
            s = 1
            cur0 = cur
            while cur-1 in d:
                cur = cur - 1
                d.remove(cur)
                s+=1
            cur = cur0
            while cur+1 in d:
                cur = cur + 1
                s+=1
                d.remove(cur)
            mx = max(mx,s)
            
        return mx
