# -*- encoding: utf-8 -*-
'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        h = ListNode(0)
        pre = h
        h.next = head
        p = head
        while p != None and p.next != None:
            q = p.next
            pre.next = q
            p.next = q.next
            q.next = p

            pre = p
            p = p.next

        return h.next

if __name__ == '__main__':
    so = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    head = n1

    h = so.swapPairs(head)

    while h != None:
        print h.val
        h = h.next


