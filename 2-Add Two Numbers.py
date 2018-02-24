# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x0 = l1.val + l2.val
        if x0 > 9:
            flag = 1
            x0 -= 10
        else:
            flag = 0
        l = ListNode(x0)
        p1 = ListNode(x0)
        l = p1
        while (l1.next and l2.next):
            l.next = ListNode(0)
            if l1.next.val + l2.next.val + flag > 9:
                l.next.val = l1.next.val + l2.next.val + flag - 10
                flag = 1
            else:
                l.next.val = l1.next.val + l2.next.val + flag
                flag = 0
            l1 = l1.next
            l2 = l2.next
            l = l.next
        while l1.next:
            l.next = ListNode(0)
            if l1.next.val + flag > 9:
                l.next.val = l1.next.val + flag - 10
                flag = 1
            else:
                l.next.val = l1.next.val + flag
                flag = 0
            l1 = l1.next
            l = l.next
        while l2.next:
            l.next = ListNode(0)
            if l2.next.val + flag > 9:
                l.next.val = l2.next.val + flag - 10
                flag = 1
            else:
                l.next.val = l2.next.val + flag
                flag = 0
            l2 = l2.next
            l = l.next
        if flag == 1:
            l.next = ListNode(0)
            l.next.val = flag
            flag = 0
            l = l.next
        return p1
