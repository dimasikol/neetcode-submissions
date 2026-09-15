class Solution:
    def trap(self, height: List[int]) -> int:
        
        mx = -1
        index = 0
        for i in range(len(height)):
            if mx <= height[i]:
                mx = height[i]
                index = i
        l = 0
        res = 0 
        for r in range(1,index):
            if height[r] > height[l]:
                l = r
            if height[r]<height[l]:
                res+=height[l]-height[r]
        l = len(height)-1
        for r in range(len(height)-1,index-1,-1):
            if height[l]>height[r]:
                res+=height[l]-height[r]
            elif height[l]<height[r]:
                l = r
        return res