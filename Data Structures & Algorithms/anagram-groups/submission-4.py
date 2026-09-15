class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        
        for s in strs:
            q = Counter(s)
            v = tuple(sorted(q.items()))
            data[v] = data.get(v,[]) + [s]
        res = []
        for i in data:
            res.append(data[i])

        return res