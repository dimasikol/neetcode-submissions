class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.data = [0 for i in range(256)]
        for i in s:
            self.data[ord(i)] +=1
        for i in t:
            self.data[ord(i)] -=1
        if any(self.data) == False:
            return True
        return False