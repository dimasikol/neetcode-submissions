class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        hight = prices[0]
        mx = 0
        for i in range(1,len(prices)):
            if l > prices[i]:
                l = prices[i]
            hight = prices[i]
            mx = max(hight-l,mx)
        return mx