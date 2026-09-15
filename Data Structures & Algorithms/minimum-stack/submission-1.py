class MinStack:

    def __init__(self):
        self.data = []
        self.minn = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.minn:
            self.minn.append(min(val,self.minn[-1]))
        else:
            self.minn.append(val)
    def pop(self) -> None:
        self.data.pop()
        self.minn.pop()


    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.minn[-1]
