class MinStack:

    def __init__(self):
        self.actual = []
        self.cur = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        self.actual.append(val)
        self.mini = min(self.mini, val)
        self.cur.append(self.mini)

    def pop(self) -> None:
        self.actual.pop()
        self.cur.pop()
        if self.cur:
            self.mini = self.cur[-1]
        else:
            self.mini = float('inf')

    def top(self) -> int:
        return self.actual[-1]

    def getMin(self) -> int:
        return self.cur[-1]

        
