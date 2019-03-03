class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_stack = [l1.val, ]
        l2_stack = [l2.val, ]

        while l1.next is not None:
            l1_stack.append(l1.next)

        while l2.next is not None:
            l2_stack.append(l2.next)

