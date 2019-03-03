class MergeSort:
    def sort(self, l):
        if len(l) <= 2:  # 当长度小于2，不进行分区而直接进行归并
            l = self.merge(l[:1], l[1:])
            return l
        else:
            l[:len(l) // 2] = self.sort(l[:len(l)//2])  # 对左分区归并，保证有序
            l[len(l) // 2:] = self.sort(l[len(l) // 2:])  # 对右分区归并，保证有序
            l = self.merge(l[:len(l)//2], l[len(l) // 2:])  # 前两个操作保障有序后，对这两个分区归并
            return l

    def merge(self, l1, l2):
        len1 = len(l1)
        len2 = len(l2)
        new_l = []
        index1 = 0
        index2 = 0

        while index1 < len1 and index2 < len2:
            if l1[index1] > l2[index2]:
                new_l.append(l2[index2])
                index2 += 1
            else:
                new_l.append(l1[index1])
                index1 += 1
        if index1 == len1:
            new_l.extend(l2[index2:])
        else:
            new_l.extend(l1[index1:])

        return new_l

a = MergeSort()

l1 = []
l2 = []

print(a.sort([1, 3, 4, 2, 2, 1, 3, 4]))


