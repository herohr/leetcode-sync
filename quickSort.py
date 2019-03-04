from copy import deepcopy


class QuickSort:
    def __init__(self, l):
        self.l = l

    def sort(self, l):
        if not l:
            return []
        if len(l) == 1:
            return deepcopy(l)

        new_l = [l[0]]
        base = l[0]
        mid_index = 0
        for i in l[1:]:
            if i <= base:
                new_l.insert(0, i)
                mid_index +=1
            else:
                new_l.append(i)

        left = self.sort(new_l[0:mid_index])
        right = self.sort(new_l[mid_index+1:])
        left.append(base)
        left.extend(right)
        return left