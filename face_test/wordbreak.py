from copy import deepcopy


class Solution(object):
    result = []
    check = []

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.dic = set(wordDict)
        self.sub(s)
        result = deepcopy(self.result)
        self.result.clear()
        self.check.clear()

        r = []
        for i in result:
            r.append(" ".join(i))

        return r

    def sub(self, s):
        if s in self.dic:
            self.check.append(s)
            self.result.append(deepcopy(self.check))
            self.check.pop()

        for i in range(0, len(s)):
            if s[:i]:
                if s[:i] in self.dic:
                    self.check.append(s[:i])
                    self.sub(s[i:])
                    self.check.pop()


tc1 = "aaaaaab"
tc2 = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

a = Solution()
print(a.wordBreak(tc1, tc2))