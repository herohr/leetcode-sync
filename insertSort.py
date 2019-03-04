from copy import deepcopy


class InsertSort:
    def __init__(self, l):
        self.l = l

    def sort(self, l):
        tl = []
        for i in l:
            tl = self.insert(tl, i)
        return tl

    def insert(self, l: list, val):
        index = 0
        length = len(l)
        while index < length:
            if val < l[index]:
                break
            index += 1
        l.insert(index, val)
        return deepcopy(l)