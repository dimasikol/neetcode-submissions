class Solution:
    def characterReplacement(self, s: str, k: int) -> int:    
        data = [0 for i in range(26)]
        string = s.upper()
        s_indx = ord('A')
        mx = 0
        l = 0
        res = 0
        for r in range(len(string)):
            indx = s_indx - ord(string[r]) 
            data[indx] += 1
            mx = max(mx,data[indx])
            while (r - mx - l + 1) > k and  l < len(string):
                l_index = s_indx - ord(string[l])
                data[l_index] -= 1
                l += 1
            res = max(res,r-l+1)
        return res