class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for element in strs:
            res = {}
            for val in element:
                res[val] = res.get(val,0)+1
            key = list(sorted(res.items()))
            data[tuple(key)] = data.get(tuple(key),[])+[element]
        return [list(i) for i in data.values()]
