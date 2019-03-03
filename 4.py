class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1 and nums2:
            if nums1[0] > nums2[0]:
                wait = Wait(0, nums1, another=Wait(0,nums2, None))
                wait.another.another = wait
            else:
                wait = Wait(0, nums2, another=Wait(0, nums1, None))
                wait.another.another = wait

        n = len(nums1)
        m = len(nums2)
        sum = n+m
        t = sum // 2
        if sum%2 == 0:
            middle1 = t
            cross = True
        else:
            middle1 = t+1
            cross = False

        if not (n and m):
            nempty = nums1 if n else nums2
            if cross:
                return (nempty[middle1-1] + nempty[middle1]) / 2
            else:
                return nempty[middle1-1]

        counter = 0
        l = []

        while counter != middle1+1:
            if wait.another.index == len(wait.another.nums):
                l.append(wait.val())
                wait.index += 1

            if wait.another_val() <= wait.val():
                l.append(wait.another_val())
                wait.another.index += 1
            else:
                l.append(wait.val())
                wait.index += 1
                wait = wait.another

            counter += 1


        print(l)
        if cross:
            return (l[-1] + l[-2]) / 2
        else:
            return l[-2]


class Wait:
    def __init__(self, index, nums, another):
        self.index = index
        self.nums = nums
        self.another = another

    def val(self):
        return self.nums[self.index]

    def another_val(self):
        return self.another.nums[self.another.index]

test1 = [0]
test2 = [1]

a = Solution()
z = a.findMedianSortedArrays(test1, test2)
print(z)