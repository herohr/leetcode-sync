class BST:
    def __init__(self, val):
        self.val = val
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @left.setter
    def left(self, value):
        self.__left = value

    @right.setter
    def right(self, value):
        self.__right = value

    def __str__(self):
        return "{}".format(self.val)

    def __repr__(self):
        return self.__str__()

    def search(self, val):
        if self.val == val:
            return self
        if val > self.val:
            if self.right is not None:
                return self.right.search(val)
            else:
                return None
        else:
            if self.left is not None:
                return self.left.search(val)
            else:
                return None

    def insert(self, val):
        if val > self.val:
            if self.right is not None:
                self.right.insert(val)
            else:
                self.right = BST(val)
        else:
            if self.left is not None:
                self.left.insert(val)
            else:
                self.left = BST(val)

    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.val)
        if self.right is not None:
            self.right.in_order_print()



TreeNode = BST


a = BST(9)
a.insert(1)
a.insert(4)
a.insert(5)
a.insert(1)
a.insert(3)
a.insert(6)
a.insert(9)
a.insert(10)

a.in_order_print()
