class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        word_dict = {}
        threshold = len(nums)//2

        for i in nums:
            v = word_dict.get(i, None)
            if v is not None:
                word_dict[i] += 1
                print(word_dict[i])
            else:
                word_dict[i] = 1

            if word_dict[i] > threshold:
                return i

tc = [1]

a = Solution()
print(a.majorityElement(tc))