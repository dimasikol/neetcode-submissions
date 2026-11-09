class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for ss in s:
            if ss in ds:
                ds[ss] +=1
            else:
                ds[ss] = 1
        for tt in t:
            if tt in dt:
                dt[tt] +=1
            else:
                dt[tt] = 1
        qs = set()
        qt = set()
        for i in ds:
            qs.add((i,ds[i]))
        for i in dt:
            qt.add((i,dt[i]))
        #print(qt,qs)
        return not(qt^qs)