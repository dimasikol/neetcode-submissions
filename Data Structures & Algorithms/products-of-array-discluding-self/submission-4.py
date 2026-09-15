class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d1 = [1]
        d2 = [1]
        data = nums
        for i in range(len(data)):
            d1.append(data[i]*d1[-1])
        for i in range(len(data)-1,-1,-1):
            d2.append(data[i]*d2[-1])
        d2 = d2[::-1]
        res = []
        for i in range(len(data)):
            res.append(d2[i+1]*d1[i])
        return res