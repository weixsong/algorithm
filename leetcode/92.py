# -*- encoding: utf-8 -*-
'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        h = ListNode(None)
        h.next = head

        pre, p = h, h.next
        i = 1
        while p != None and i < m:
            pre = p
            p = p.next
            i += 1

        q = p
        p = p.next
        while i < n:
            temp = p.next
            p.next = pre.next
            pre.next = p

            q.next = temp
            p = temp
            i += 1

        return h.next

