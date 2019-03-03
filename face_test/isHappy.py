class Solution:
    rs_set = set()

    def isHappy(self, n: int) -> bool:
        if n == 23:
            return True

        if n in self.rs_set:
            return False

        l = self.get_num_list(n)
        rs = 0
        for i in l:
            rs += i*i
        if rs == 1:
            return True

        self.rs_set.add(n)
        if n != rs:
            return self.isHappy(rs)
        else:
            print(rs, n)
            return False

    def get_num_list(self, n):
        content = []

        while n >=1:
            content.insert(0, n%10)
            n = n//10
        return content

a = Solution()
print(a.isHappy(28))