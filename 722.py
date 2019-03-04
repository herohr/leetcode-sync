from copy import deepcopy


class Solution(object):
    def removeComments(self, source: list):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        # index = 0
        # block = 0
        # while index < len(source):
        #     if block:
        #         r = self.find("*/", source[index])
        #         if r is not None:
        #             source[index] = source[index][r+2:]
        #             while block:
        #                 source.pop(index-block)
        #
        #
        #     r = self.find("//", source[index])
        #     if r is not None:
        #         source[index] = deepcopy(source[index][:r])
        #     index += 1

        index = 0
        result = []
        block_mode = False
        while index < len(source):


            if not block_mode:


                r = self.find("//", source[index])
                if r is not None:
                    source[index] = deepcopy(source[index][:r])
                index += 1


        return source



    def find(self, target, s):
        if s:
            index = 0
            while index < len(s) - 1:
                if s[index] == target[0]:
                    j = 1
                    while j < len(target):
                        if s[index+j] != target[j]:
                            break
                        j += 1
                    if j == len(target):
                        return index


                index += 1

            return None
        return None

a = ["//sasdqwe"]
s = Solution()
print(s.removeComments(a))