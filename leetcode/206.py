# -*- encoding: utf-8 -*-
'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
        	return None

        if head.next == None:
        	return head

        return self.reverse(head)

    def reverse(self, head):
    	p = head
    	q = head.next
    	r = q.next

    	p.next = None

    	while r != None:
    		q.next = p
    		p = q
    		q = r
    		r = r.next

    	q.next = p
    	p = q

    	return p

