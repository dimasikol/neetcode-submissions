class MinStack:

    def __init__(self):
        self.data = []
        self.ls = []
        self.len = 0

    def push(self, val: int) -> None:
        self.data.append(val)
        val = min(val,self.ls[-1] if self.ls else val)
        self.ls.append(val)
        self.len +=1


    def pop(self) -> None:
        cur = self.data.pop()
        self.ls.pop()
        self.len-=1
    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.ls[-1]
