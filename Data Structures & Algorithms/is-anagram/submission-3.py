class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        data1 = {}
        data2 = {}
        for i in s:
            data1[i] = data1.get(i,0)+1
        for i in t:
            data2[i] = data2.get(i,0)+1
        if data1 == data2:
            return True
        return False
