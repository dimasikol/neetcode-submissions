class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        helpify = {'[':']','(':')','{':'}'}
        for i in s:
            if i in '[({':
                q.append(helpify[i])
            else:
                if len(q)==0:
                    return False
                if q.pop()!=i:
                    return False
        if len(q)==0:
            return True
        return False