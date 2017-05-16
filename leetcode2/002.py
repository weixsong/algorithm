#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carrier = 0
        head = ListNode(None)
        p = head

        while l1 is not None and l2 is not None:
            x = l1.val + l2.val + carrier
            carrier = x / 10
            x %= 10

            node = ListNode(x)
            p.next = node
            p = node

            l1, l2 = l1.next, l2.next

        if l2 is not None:
            l1 = l2

        while l1 is not None:
            x = l1.val + carrier
            carrier = x / 10
            x %= 10
            node = ListNode(x)
            p.next = node
            p = node
            l1 = l1.next

        if carrier != 0:
            node = ListNode(carrier)
            p.next = node

        return head.next


if __name__ == '__main__':
    so = Solution()
