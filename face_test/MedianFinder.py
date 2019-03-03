class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def addNum(self, num: int) -> None:
        index = 0
        while index < len(self.l):
            if self.l[index] > num:
                self.l.insert(index, num)
                return
            index += 1
        self.l.append(num)

    def findMedian(self) -> float:
        l = len(self.l)
        if l % 2 == 0:
            return (self.l[l // 2 - 1] + self.l[l // 2]) / 2
        else:
            return self.l[l // 2]

            # Your MedianFinder object will be instantiated and called as such:
            # obj = MedianFinder()
            # obj.addNum(num)
            # param_2 = obj.findMedian()



a = MedianFinder()
a.addNum(-1)
a.addNum(-1.5)
a.addNum(-3)
a.addNum(-4)

print(a.findMedian())