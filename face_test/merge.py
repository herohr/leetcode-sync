class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        counter = 0
        index2 = 0

        if n == 0:
            return

        while counter < len(nums1):
            if index2 >= n:
                return
            if nums1[counter] < nums2[index2] and counter < m:
                counter += 1
            else:
                nums1.insert(counter, nums2[index2])
                nums1.pop()
                m += 1
                index2 += 1 if index2 < n-1 else n
                counter += 1


nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

a = Solution()
a.merge(nums1, m, nums2, n)
print(nums1)
