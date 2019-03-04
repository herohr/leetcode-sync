class Tree:
    def __init__(self, word):
        self.sons = []
        self.word = word
        self.val = self.word
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
