#!/usr/bin/env python
"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head == None:
            return None

        node = head
        d = {}
        while node != None:
            d[node] = RandomListNode(node.label)
            node = node.next

        node = head
        while node != None:
            new_node = d[node]
            new_node.next = d.get(node.next, None)
            new_node.random = d.get(node.random, None)
            node = node.next

        return d[head]

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if head == None:
            return None

        cur = head
        while cur != None:
            cur_cp = RandomListNode(cur.label)
            cur_cp.next = cur.next
            cur.next = cur_cp
            cur = cur_cp.next

        cur = head
        while cur != None:
            cur_cp = cur.next
            if cur.random != None:
                cur_cp.random = cur.random.next
            cur = cur_cp.next

        cur = head
        head_cp = head.next

        while cur != None:
            cur_cp = cur.next
            cur.next = cur_cp.next
            cur = cur.next
            if cur != None:
                cur_cp.next = cur.next

        return head_cp


