import queue
import collections
class Solution:
    def isValid(self, s: str) -> bool:
        l = queue.Queue()
        for i in s:
            l.put(i)
        r = collections.deque()
        d = {'(': ')', "{": "}", "[": "]"}
        while not l.empty():
            if not r:
                r.append(l.get())
            else:
                cur = l.get()
                if cur in d:
                    r.append(cur)
                else:
                    r_cur = r.pop() 
                    if r_cur in d and d[r_cur] == cur:
                        continue
                    else:
                        return False
        if not r:
            return True
        return False