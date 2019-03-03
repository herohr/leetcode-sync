class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}".format(self.val)


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        stack = []

        node = head

        tail = None
        while node is not None:
            stack.append(node)
            if node.next is None and node is not None:
                tail = node

            node = node.next

        print(tail)


        while stack:
            a = stack.pop()
            if stack:
                a.next = stack[-1]
            else:
                a.next = None

        return tail


a = ListNode(1)
a.next = ListNode(2)
c = a.next
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

s = Solution()
v = s.reverseList(a)

while v is not None:
    print(v.val)
    v = v.next