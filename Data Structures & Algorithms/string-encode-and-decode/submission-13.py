class Solution:

    def encode(self, strs: List[str]) -> str:
        data = []
        for i in strs:
            data.append(str(len(i))+'?'+i)
        return ''.join(data)


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            num = ''
            j = i
            while len(s)>j and s[j]!='?':
                num+=s[j]
                print(num)
                j+=1
            if num:
                res.append(s[j+1:j+1+int(num)])
                i = j+int(num)
            i+=1
        return res

