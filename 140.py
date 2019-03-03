test_str = "catsanddog"
test_list = ["cat", "cats", "and", "sand", "dog"]
from Tree import Tree

class Tree:
    def __init__(self, word):
        self.sons = []
        self.word = word
        self.broke = False

    def add_son(self, tree):
        if tree is None:
            return self

        self.sons.append(tree)
        return self

    def is_leaf(self):
        return len(self.sons) == 0

    def __getitem__(self, item):
        return self.sons.__getitem__(item)

    def __str__(self):
        return "Word: " + self.word

    def __repr__(self):
        return self.__str__()

    def set_broke(self):
        self.broke = True

    def is_broke(self):
        return self.broke


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        Solution.words = wordDict

        tree = self.get_son_tree(s, 0, Tree(""), words=wordDict)
        # print(tree.sons)
        # for i in tree.sons:
        #     print(i)

        return iter_tree(tree)

    def get_son_tree(self, s: str, offset, tree=None, words=()):

        # print(s)
        has = False
        for i in words:
            if s.startswith(i, offset):
                son = Tree(i)
                tree.add_son(son)
                has = True
        else:
            if not has and offset != len(s):
                tree.set_broke()

        for i in tree.sons:
            self.get_son_tree(s, offset+len(i.word), i, words)

        return tree


def iter_tree(tree, content=None, strs=""):
    if content is None:
        content = []

    if len(tree.sons) == 0:
        strs = strs[0:-1]
        if strs:
            content.append(strs)

        return content

    for i in tree:
        if not i.is_broke():
            iter_tree(i, content, strs+i.word+" ")

    return content

a = Solution()

z = "aaaaaaaaaaa"
c = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(a.wordBreak(z, c))

