# -*- encoding: utf-8 -*-
'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    '''
    time: O(n)
    space: O(n)
    '''
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        e = []
        while head != None:
            e.append(head.val)
            head = head.next

        i, j = 0, len(e) - 1
        while i <= j:
            if e[i] != e[j]:
                return False

            i += 1
            j -= 1

        return True

class Solution1(object):
    '''
    time: O(n)
    space: O(1)
    recursive call will lead to memory limit exceed
    '''
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None:
            return False

        p = head
        q = head
        return self.check(p, q, head)

    def check(self, p, q, head):
        res = None
        if q.next != None and p == head:
            res = self.check(p, q.next, head)

        # trace back of recursive call
        if res == False:
            return res

        if p.val != q.val:
            return False
        else:
            p = p.next
            return True

class Solution(object):
    '''
    time: O(n)
    space: O(1)
    fast and slow pointer, 2x, 1x
    reverse the second half
    '''
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True

        fast, slow = head, head

        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        h = slow.next
        # reverse the second half
        if h != None and h.next != None:
            slow.next = self.reverse(h)

        p1 = head
        p2 = slow.next

        while p2 != None:
            if p1.val != p2.val:
                return False

            p1 = p1.next
            p2 = p2.next

        return True


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



