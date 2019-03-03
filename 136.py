class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        has_set = set()
        single_set = set()
        for i in nums:
            if i in has_set:
                single_set.discard(i)
            else:
                has_set.add(i)
                single_set.add(i)
        return single_set.pop()

tc = [4, 1, 2, 1, 2]

a = Solution()
v = a.singleNumber(tc)
print(v)