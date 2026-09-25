class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        def backtrack(nums, word):
            if len(digits) == len(word):
                res.append(''.join(word))
            while nums:
                num = nums[0]
                nums = nums[1:]
                for i in digitToChar[num]:
                    word.append(i)
                    backtrack(nums,word)
                    word.pop()
        backtrack(digits,[])
        return res