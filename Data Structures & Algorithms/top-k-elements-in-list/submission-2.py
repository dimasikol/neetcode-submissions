class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for i in nums:
            data[i] = data.get(i,0)+1
        res =[]
        for i in sorted(data.items(),key=lambda x: -x[1]):
            res.append(i[0])
            k-=1
            if k == 0:
                break
        return res