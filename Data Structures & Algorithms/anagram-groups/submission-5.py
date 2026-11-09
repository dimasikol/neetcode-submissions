class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_dict(s):
            d = {}
            for i in s:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            q = []
            for k,v in d.items():
                q.append((k,v))
            return tuple(sorted(q))
        d = {}
        for s in strs:
            code = get_dict(s)
            if code in d:
                d[code].append(s)
            else:
                d[code] = [s]
        return list(d.values())