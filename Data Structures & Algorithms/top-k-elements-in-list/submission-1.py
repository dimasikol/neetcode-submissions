class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data_set = {}
        for i in nums:
            data_set[i] = data_set.get(i,0)+1
        
        res = []
        for key,val in sorted(data_set.items(),key=lambda x:x[1],reverse = True)[:k]:
            res.append(key)
        return res