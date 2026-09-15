class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        r = 1
        hashed = {}
        for i in nums:
            hashed[i] = hashed.get(i,0)+1

        res = set()
        while l < len(nums):
            r = l+1
            while  r < len(nums):
                if l!=r:

                    if -(nums[l]+nums[r]) in hashed:
                        new =  tuple(sorted([nums[l],nums[r],-(nums[l]+nums[r])]))
                        check = {}
                        for i in new:
                            check[i] = check.get(i,0)+1
                        for k,v in check.items():
                            if hashed[k]<v:
                                break
                        else:
                            res.add(new) 
                r+=1
            l+=1
        return list([list(i) for i in res])