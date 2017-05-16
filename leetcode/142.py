#!/usr/bin/env python
"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None

        slow, fast = head, head
        step = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                # find cycle
                while head != slow:
                    slow = slow.next
                    head = head.next

                return slow

        return None
