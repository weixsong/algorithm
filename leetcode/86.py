# -*- encoding: utf-8 -*-
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        q1 = ListNode(None)
        q2 = ListNode(None)
        h1, h2 = q1, q2

        p = head
        while p != None:
            if p.val < x:
                q1.next = ListNode(p.val)
                q1 = q1.next
            else:
                q2.next = ListNode(p.val)
                q2 = q2.next

            p = p.next

        q1.next = h2.next

        return h1.next





