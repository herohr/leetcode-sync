class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True

        s = self.preduce(s)

        index1 = 0
        index2 = len(s) - 1

        while index1 <= index2:
            if s[index1] == s[index2]:
                index1 +=1
                index2 -=1
            else:
                return False
        return True


    def preduce(self, s):
        l = []
        j = list("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890")
        for i in list(s):
            if i in j:
                l.append(i.lower())
        return "".join(l)


a = Solution()
print(a.isPalindrome("r"))