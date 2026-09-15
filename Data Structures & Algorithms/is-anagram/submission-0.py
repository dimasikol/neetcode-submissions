class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s)==len(t):
            for ss,tt in zip(s,t):
                d1[ss] = d1.get(ss,0)+1
                d2[tt] = d2.get(tt,0)+1
            if d1 == d2:
                return True
            else:
                return False
        else:
            return False