class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0 if nums[0]==target   else -1 
        while r>=l:
            m = l+((r-l)//2)
            if nums[m]==target:
                return m 
            elif nums[m]<target:
                l = m + 1
            else:
                r = m -1
        return -1