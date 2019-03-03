class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.os = OrderStack()

    def push(self, x: int) -> None:
        self.os.push(x)
        self.l.append(x)

    def pop(self) -> None:

        item = self.l.pop()
        self.os.pop(item)

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.os.get_top()

    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()


class OrderStack:
    def __init__(self):
        self.l = []

    def get_top(self):
        return self.l[-1]

    def push(self, x):
        self.l.append(x)
        self.l.sort(reverse=True)

    def pop(self, x):
        self.l.remove(x)