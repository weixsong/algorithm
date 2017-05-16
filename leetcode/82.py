# -*- encoding: utf-8 -*-
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        pre = ListNode(None)
        pre.next = head

        h = pre

        p = pre.next
        while p != None:
            while p.next != None and p.val == p.next.val:
                p = p.next

            if pre.next == p:
                pre = p
                p = p.next
            else:
                pre.next = p.next
                p = pre.next

        return h.next
