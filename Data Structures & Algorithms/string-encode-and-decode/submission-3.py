import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        q = 0
        res = ""
        for i in strs:
            q = len(i)
            res= res+f"#{q}#"+i
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            if s[i]=='#':
                i+=1
                ln = ''
                while len(s)>i and s[i].isdigit():
                    ln = ln+s[i]
                    i+=1
                res.append(s[i+1:i+int(ln)+1])
                i=i+int(ln)
            i+=1
        return res
