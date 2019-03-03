class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nl = len(matrix)
        if nl == 0:
            return False
        ml = len(matrix[0])

        ms = 0
        ns = 0

        if ml == 1 or nl == 1:
            if ml == 1:
                find, _ = self.columnSearch(matrix, target, 0, 0, nl-1)
            else:
                find, _ = self.lineSearch(matrix, target, 0, 0, ml-1)
            return find

        me, ne = ml - 1, nl - 1

        m, n = 0, 0

        find = False

        while not find:
            find, me = self.lineSearch(matrix, target, m, ms, me)
            if find:
                return True
            find, ne = self.columnSearch(matrix, target, n, ns, ne)
            if find:
                return True

            if ms == me and ns == ne:
                return False
            ms = ms + 1 if ms < ml else ms
            ns = ns + 1 if ns < nl else ns
            if ns > ne:
                return False
            if ms > me:
                return False
            m = m+1 if m < nl-1 and m <= ms else m
            n = n+1 if n < nl-1 and n <= ns else n

    def lineSearch(self, matrix, target, line, start, end):
        print("ls", line, start, end)
        index = start
        while index <= end:
            val = matrix[line][index]
            if val == target:
                return True, 0
            if val > target:
                return False, index
            if index == end:
                return False, end

            index += 1
        return False, end

    def columnSearch(self, matrix, target, column, start, end):
        print("cs", column, start, end)
        index = start
        while index <= end:
            val = matrix[index][column]
            if val == target:
                return True, 0
            if val > target:
                return False, index
            if index == end:
                return False, end

            index += 1



tc = []

a = Solution()
# for i in tc:
#     for j in i:
#         v = a.searchMatrix(tc, j)
#
#         print(v)

v = a.searchMatrix(tc, 14)

print(v)
