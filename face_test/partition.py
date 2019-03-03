from copy import deepcopy


class Solution(object):
    check = []
    result = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        self.sub_partition(s)
        result = deepcopy(self.result)
        self.result.clear()
        self.check.clear()

        return result

    def sub_partition(self, s):
        if s[::-1] == s:
            self.check.append(s)
            self.result.append(deepcopy(self.check))
            self.check.pop()

        for i in range(0, len(s)):
            if s[:i]:

                if s[:i] == s[:i][::-1]:
                    self.check.append(s[:i])
                    self.sub_partition(s[i:])
                    self.check.pop()



tc = "aab"

a = Solution()
print(a.partition(tc))