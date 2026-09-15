class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import string
        data = {}
        alpha = [0 for i in range(26)]
        for st in strs:
            cur = alpha.copy()
            st.lower()
            for i in st:
                cur[ord(i)-97] += 1
            c = tuple(cur)
            if c in data:
                data[c].append(st)
            else:
                data[c] = [st,]
        return list(sorted(data.values(),key=len))