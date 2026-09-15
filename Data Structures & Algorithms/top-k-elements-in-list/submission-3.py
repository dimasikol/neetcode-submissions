class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = Counter(nums)
        res = list(sorted(counters.items(),key=lambda x: -x[1]))            

        return list(map(lambda x: x[0],res[:k]))
        