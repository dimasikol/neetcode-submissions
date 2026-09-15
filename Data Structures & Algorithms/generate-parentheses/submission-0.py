class Solution:
    def check(self,l):
        q = []
        d = {'(':')',')':'('}
        for i in l:
            if i == '(':
                q.append('(')
            else:
                if q:
                    q.pop()
                else:
                    return False 
        return True

    def generateParenthesis(self, n: int) -> List[str]:
        import itertools
        s = list(itertools.product('()',repeat=(n*2)))
        res = []
        for i in s:
            if i.count('(') != i.count(')'):
                continue
            if self.check(i):
                res.append(''.join(i))

        return res