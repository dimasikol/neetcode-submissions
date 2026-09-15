class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        mxx = 0
        for i in range(1,len(prices)):
            minn  = min(minn, prices[i])
            mx = prices[i]        
            mxx = max(mxx ,prices[i] - minn )
        return mxx