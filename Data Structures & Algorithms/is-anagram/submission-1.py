class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        data_1 = {}
        data_2 = {}
        if len(s)==len(t):
            for i_s,i_t in zip(s,t):
                data_1[i_s] = data_1.get(i_s,0) +1
                data_2[i_t] = data_2.get(i_t,0) +1
            return data_1 == data_2
        return False