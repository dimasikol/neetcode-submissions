class Solution:

    def encode(self, strs) -> str:
        res = ''
        for i in strs:
            res += str(len(i))+'?'+i
        return res



    def decode(self, s: str):
        l = 0
        res = []
        while l < len(s):
            num = ''
            while l < len(s) and  s[l]!='?':
                num += s[l]
                l += 1
            if num:
                l += 1
                ss = ''
                for i in range(l,l+int(num)):
                    ss += s[i]
                res.append(ss)
                l += int(num)

        return res
