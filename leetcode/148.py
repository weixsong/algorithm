#!/usr/bin/env python
"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Idea: divide and conquer, merge sort
        divide the linked list into halve by slow and fast pointer.

        Time: O(nlogn)
        Space: O(1)
        """
        if head == None or head.next == None:
            return head

        # step 1. cut the list into two half by slow and fast pointer
        pre = None
        slow, fast = head, head

        # time cost of this, could be count into the merge O(n)
        # then the time complexity still O(nlogn)
        while fast and fast.next != None:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None

        # step 2. recursive call on each half
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # step 3. merge
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        head = ListNode(0)
        p = head

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next

            p = p.next

        p.next = l1 if l1 else l2

        return head.next
