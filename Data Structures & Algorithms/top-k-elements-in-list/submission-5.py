class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        dd = []
        for kk,v in d.items():
            dd.append((v,kk))
        dd.sort()
        print(dd[-k:])
        return list(map(lambda x: x[1],dd[-k:]))