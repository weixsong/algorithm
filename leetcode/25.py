# -*- encoding: utf-8 -*-
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        pre_head = ListNode(0)
        pre_tail = pre_head
        pre_head.next = head

        p = pre_head.next

        while p != None:
            c = k - 1

            h = p
            tail = p
            while c > 0 and tail.next != None:
                tail = tail.next
                c -= 1

            if c > 0:
                pre_tail.next = h
                return pre_head.next

            p = tail.next
            tail.next = None

            pre_tail.next = self.reverse(h)
            pre_tail = h
            

        return pre_head.next

    def reverse(self, head):
        if head == None or head.next == None:
            return head

        p, q = head, head.next
        r = q.next

        p.next = None

        while r != None:
            q.next = p
            p = q
            q = r
            r = r.next

        q.next = p
        p = q

        return q

