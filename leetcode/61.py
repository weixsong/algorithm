# -*- encoding: utf-8 -*-
'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None or k == 0:
            return head

        count = 0
        p = head
        tail = p
        while p != None:
            count += 1
            tail = p
            p = p.next

        k = k % count
        if k == 0:
            return head

        p = head
        n = count - k

        while n > 1:
            n -= 1
            p = p.next

        q = p.next

        new_head = q
        p.next = None
        tail.next = head

        return new_head


if __name__ == '__main__':
    n1 = ListNode(1)
    n1.next = ListNode(2)
    n1.next.next = ListNode(3)
    n1.next.next.next = ListNode(4)
    n1.next.next.next.next = ListNode(5)

    so = Solution()
    res = so.rotateRight(n1, 2)

    while res != None:
        print res.val, 
        res = res.next