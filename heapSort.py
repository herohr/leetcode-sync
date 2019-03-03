class HeapSort:
    def __init__(self, l):
        self.l = l

        for i in range(0, len(l)):  # 每一次调整，都会将最大的数放在根
            self.adjust(0, len(l) - i)  # 进行调整
            self.l[0], self.l[len(l) - 1 - i] = self.l[len(l) - 1 - i], self.l[0]  # 将最大数放在尾部

    def adjust(self, start, offset):
        left = start * 2 + 1
        right = start * 2 + 2  # 左右边界
        left_changed = False
        right_changed = False  # 左右节点是否被调整

        if left < offset:  # 如果存在左节点
            self.adjust(left, offset)  # 调整左子树
            if self.l[left] > self.l[start]:  # 当左比根大，则交换
                left_changed = True
                self.l[left], self.l[start] = self.l[start], self.l[left]

        if right < offset:  # 如果存在右节点
            self.adjust(right, offset)  # 调整右子树
            if self.l[right] > self.l[start]:
                if left_changed:
                    self.l[left], self.l[start] = self.l[start], self.l[left]  # 换回来
                self.l[right], self.l[start] = self.l[start], self.l[right]
                right_changed = True
                left_changed = False
        if left_changed:
            self.adjust(self.l[left], offset)
        if right_changed:  # 当左右节点被交换，则调整左右子树
            self.adjust(self.l[right], offset)


a = HeapSort([4, 6, 8, 5, 9, 1, 4, 5, 1, 2, 31, 4])
print(a.l)
