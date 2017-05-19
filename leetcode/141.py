# -*- encoding: utf-8 -*-
'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        p_slow, p_fast = head, head

        while p_fast != None and p_fast.next != None and p_fast.next.next != None:
            p_slow = p_slow.next
            p_fast = p_fast.next.next

            if p_slow == p_fast:
                return True


        return False