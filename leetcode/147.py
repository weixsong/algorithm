#!/usr/bin/env python
"""
Sort a linked list using insertion sort.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        O(n^2)
        """
        
        new_head = ListNode(0)
        curr = head
        next = None

        while curr != None:
            next = curr.next

            p = new_head
            while p.next != None and p.next.val < curr.val:
                p = p.next

            curr.next = p.next;
            p.next = curr

            curr = next

        return new_head.next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        O(nlogn)
        """

        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next

        nums.sort(reverse=True)

        new_head = ListNode(0)

        for num in nums:
            node = ListNode(num)
            node.next = new_head.next
            new_head.next = node

        return new_head.next
