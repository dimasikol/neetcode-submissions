class Solution:
    def get_set(self,string:str):
        new = {}
        for i in string:
            new[i] = new.get(i,0)+1
        result = []
        for u in sorted(new.keys()):
            result.append((u,new[u]))
        return tuple(result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        if len(strs):
            for st in range(len(strs)):
                tupl = self.get_set(strs[st])
                dicts[tupl] = dicts.get(tupl,[])+[strs[st]]
            
            return sorted(list(dicts.values()),key=len)