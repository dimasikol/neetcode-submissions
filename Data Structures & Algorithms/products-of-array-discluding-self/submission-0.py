class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = []
        last = 1
        count_0 =0
        for i in nums:
            if i:
                last = last*i
            else:
                count_0+=1
        for i in nums:
            if count_0==0:
                d.append(last//i)
            elif count_0 == 1:
                if i == 0:
                    d.append(last)
                else:
                    d.append(0)
            else:
                d.append(0)
        return d