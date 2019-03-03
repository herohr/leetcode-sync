class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def pre_order(self, result: list):
        result.append(self.val)

        if self.left is not None:
            self.left.pre_order(result)
        if self.right is not None:
            self.right.pre_order(result)

    def in_order(self, result: list):
        if self.left is not None:
            self.left.in_order(result)
        result.append(self.val)
        if self.right is not None:
            self.right.in_order(result)

    def post_order(self, result: list):
        if self.left is not None:
            self.left.post_order(result)
        if self.right is not None:
            self.right.post_order(result)
        result.append(self.val)

    def pre_order_noRcs(self):
        root = self
        stack = [(root, False)]
        result = []

        while stack:
            root, visited = stack.pop()
            if not visited:
                result.append(root.val)
            if root.right is not None:
                stack.append((root.right, False))
            if root.left is not None:
                stack.append((root.left, False))
        return result

    def get_depth(self):
        max_l = 1

        def sub_get_depth(self, l):
            nonlocal max_l
            if l > max_l:
                max_l = l
            if self.left is not None:
                sub_get_depth(self.left, l + 1)
            if self.right is not None:
                sub_get_depth(self.right, l + 1)

        sub_get_depth(self, 1)
        return max_l


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)

a.left.left = TreeNode(4)
a.left.right = TreeNode(5)

a.right.left = TreeNode(6)
a.right.right = TreeNode(7)

a.left.left.left = TreeNode(1)
a.left.left.left.left = TreeNode(2)


r = []
a.pre_order(r)
print(r)

r = a.pre_order_noRcs()
print(r)

print(a.get_depth())
