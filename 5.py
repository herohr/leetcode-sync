class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s

        result = set()
        m = ""
        self.get_subs(s, result)
        for i in result:
            if i == i[::-1] and len(i) > len(m):
                m = i

        return m




    def get_subs(self, s, result):
        if s:
            result.add(s)
            self.get_subs(s[0:-1], result)
            self.get_subs(s[1:], result)



a = Solution()
r = a.longestPalindrome("babaddtattarrattatddetartrateedredividerb")
print(r)