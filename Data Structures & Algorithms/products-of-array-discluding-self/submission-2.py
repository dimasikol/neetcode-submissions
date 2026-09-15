class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == 0:
            data = [1]
            r = 1
            for k in nums:
                data.append(k*data[-1])
            data=data[1:]
            for i in range(len(data)):
                data[i] = data[-1]//nums[i]
            return data
        elif nums.count(0) == 1:
            index_0 = nums.index(0)
            data = [0 for i in range(len(nums))]
            r = 1
            for i in nums:
                if i:
                    r*=i
            data[index_0] = r 
            return data
        elif nums.count(0) > 1:
            return [0 for i in range(len(nums))]

